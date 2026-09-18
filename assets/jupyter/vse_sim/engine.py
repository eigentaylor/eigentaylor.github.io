"""The per-election simulation loop and its reducers (section 8 of
`vse_simulation.ipynb`, cell 38).

For each election: build the *true* electorate, derive a *perceived* electorate at
`epistemic_rho`, then apply participation friction at `awareness_alpha`/`fatigue_beta`
to get the electorate voters actually form ballots from. VSE is always scored against
the true electorate. Only `count`, `sum(vse)` and `sum(vse**2)` are accumulated per
`(method, chooser)` -- not the raw per-election rows -- so this scales to large `niter`
without holding everything in memory.

Deliberately single-threaded/no multiprocessing: parallelizing would need worker
functions importable from a real module, which fought notebook-defined functions,
especially on Windows. (Now that this *is* a real module, that constraint has lifted --
but the loop is left as-is so results stay bit-identical to the notebook's.)"""

import math
import time
from collections import defaultdict

from numpy import isclose, mean
from numpy import sign as _sign4

from .condorcet import true_condorcet_winner
from .friction import apply_participation_friction
from .noise import make_perceived_electorate
from .vendored.methods.score import Score

# Running total of elections simulated in this process, for the notebook's own
# "how much compute did this take" readout. Incremented by run_vse_simulation below.
TOTAL_ELECTIONS_RUN = 0


def run_vse_simulation(model, methods, nvot, ncand, niter, chooser_funs, media,
                       epistemic_rho=1.0, awareness_alpha=1.0, fatigue_beta=1.0, electorates=None,
                       paired_diff_pairs=None, paired_diff_chooser="honBallot", paired_ce_pairs=None,
                       raw_vse_sink=None, honest_only=False,
                       betrayal_targets=None, betrayal_sink=None, coma_targets=None, coma_sink=None,
                       primary_corruption_sink=None, primary_cost_targets=None, primary_cost_sink=None):
    """Run niter elections; return (vse_summary, ce_raw, paired_diff_summary, paired_ce_summary).

    Each election's voters cast ballots on their *perceived* utilities (true
    utility blended with epistemic noise at knowledge level epistemic_rho -- see
    make_perceived_electorate above), further masked by participation friction
    (awareness_alpha, fatigue_beta -- see apply_participation_friction above), while
    VSE is always scored against the *true* electorate's social utilities.

    electorates: optional pre-generated list of >= niter true electorates to reuse instead of
      drawing niter fresh ones -- common random numbers: pass the SAME list to multiple calls
      that vary epistemic_rho/awareness_alpha/fatigue_beta (e.g. across a parameter sweep) so they're all
      comparing the same underlying "worlds" under different friction assumptions, rather than
      each assumption seeing independently-drawn worlds. Falls back to drawing fresh electorates
      when not given (unchanged default behavior).

    paired_diff_pairs: optional list of (label, baseline_label) pairs, e.g. [("Approval", "STAR"),
      ("Plurality Top-2", "Approval Top-2")]. For each pair, label's paired_diff_chooser-VSE is
      diffed against baseline_label's, election by election -- since every method within one call
      here sees the identical election (same true/perceived/friction draws), this is a genuine
      paired comparison, not an independent-samples one. A label can appear in more than one pair
      (e.g. diffed against both STAR and a same-family baseline), since diffs are keyed by the
      (label, baseline_label) pair, not by label alone.
      paired_diff_summary[(label, baseline_label)] accumulates [count, sum_d, sum_d_sq] of
      (VSE[label] - VSE[baseline_label]). Always returned (empty dict when paired_diff_pairs is
      None/empty), so callers can unpack a 4-tuple unconditionally. reduce_to_mean_ci (below)
      applies to it directly -- same [count, sum, sum_sq] shape as vse_summary, just keyed by
      (label, baseline_label) instead of (label, chooser).

    paired_ce_pairs: optional list of (label, baseline_label) pairs, same convention as
      paired_diff_pairs, but diffing the binary "did this method pick the TRUE Condorcet winner"
      indicator instead of VSE -- election by election, restricted to elections where a true CW
      exists (see true_condorcet_winner above). Since every method within one call here sees the
      identical election, a method's and baseline_label's CW-hit outcomes are correlated, not
      independent -- this is a matched-pairs (McNemar's-test-style) comparison, the CE analogue
      of paired_diff_pairs, reusing cw/row["winner"] already computed below at essentially no
      extra cost. paired_ce_summary[(label, baseline_label)] accumulates [count, sum_d, sum_d_sq]
      of (cw_hit[label] - cw_hit[baseline_label]) -- same shape as paired_diff_summary, so
      reduce_to_mean_ci applies unchanged.

    raw_vse_sink: optional defaultdict(list) that, when given, also collects every individual
      election's row["vse"] under raw_vse_sink[(label, chooser)] -- the per-election values behind
      vse_summary's running [count, sum, sum_sq], which are otherwise discarded the instant they're
      folded into that accumulator. Used by Section 26's per-election VSE histograms, which need
      the underlying distribution rather than just its mean/CI. None (default): no extra
      bookkeeping, no behavior change for any other caller.

    betrayal_targets / betrayal_sink: optional list of (label, topRank) pairs (e.g.
      [("STAR", STAR_TOP_RANK)]) and a caller-supplied dict to accumulate into, same
      caller-owns-the-container convention as raw_vse_sink (populated in place; None/empty means
      no extra bookkeeping, no behavior change). For each target, on the SAME true_electorate/
      ballot_electorate this call already drew for every method above, recomputes that primary's
      own top-2 pair from a Score(topRank, True) scoring of the ACTUAL (noisy/friction-affected)
      ballots, then compares the resulting pairwise upset sign against the same-format upset sign
      from HONEST ballots on the TRUE electorate -- this is Section 23's "runoff betrayal"
      diagnostic (does the runoff's actual decision for this pair agree with what honest ballots
      would have decided?) plus its flip-direction bucketing (does the runoff change the winner
      away from the primary's raw top-score pick, and if so is that flip "good" or "bad"?) --
      folded into this loop instead of each redrawing its own separate batch of elections.
      betrayal_sink[label] accumulates the running sums reduce_betrayal_summary (below) turns
      into betrayal_rate/voter_corruption_rate/decisive_vse_cost/population_vse_cost/flip rates.
      Raises ValueError if betrayal_targets is given without betrayal_sink (fail loud rather than
      silently produce an empty diagnostic).

    coma_targets / coma_sink: same convention as betrayal_targets/betrayal_sink, but for the
      Approval Top-2 (Coma) primary-awareness diagnostic (topRank is normally 1, Approval's own
      scale): classifies every voter's Coma-runoff vote against their true preference, bucketed by
      whether awareness alone would have fixed it, PLUS the election-level aggregate-sign accuracy
      comparison between Coma and a "full awareness" (Groggy) counterfactual on the same noise.
      coma_sink[label] accumulates the running counts reduce_coma_summary (below) turns into rates.
      Raises ValueError if coma_targets is given without coma_sink.

    primary_cost_targets / primary_cost_sink: same convention as betrayal_targets/betrayal_sink,
      for Approval Top-2's own primary-noise isolation diagnostic. Holds the runoff information
      level fixed at Groggy (the runoff pairwise check uses perceived_electorate, the same
      pre-friction perceived electorate every Groggy comparison above uses) and asks how much
      utility is lost from the PRIMARY tally alone being noisy: compares the real (noisy-primary)
      Groggy winner against a counterfactual Groggy winner between the finalists an honest
      (zero-noise, zero-friction) primary would have selected instead. Not bucketed into bad
      flip/silent lock-in like betrayal_targets -- once the finalist SET itself can differ between
      the real and counterfactual primary, there is no single "primary's raw leader" to flip away
      from or lock in on, so this is one net cost per scenario, plus n_finalist_set_changed (how
      often primary noise alone swapped who even reached the runoff). primary_cost_sink[label]
      accumulates the running sums reduce_primary_cost_summary (below) turns into
      finalist_set_changed_rate/primary_noise_vse_cost. Raises ValueError if primary_cost_targets
      is given without primary_cost_sink.

    primary_corruption_sink: optional caller-supplied dict (e.g. {}) to accumulate into, same
      caller-owns-the-container convention as raw_vse_sink/betrayal_sink -- unlike those, this
      needs no "targets" list, since it's a property of the shared ballot_electorate/aware_sets
      themselves (built once per election, before any method-specific scoring), not of any one
      method's own top-2/scoring rule. For every voter, every election, classifies their actual
      vote (favorite_known: the max-perceived-utility candidate among their aware set) against
      their true favorite (max-true-utility candidate, unrestricted): aligned (matches),
      awareness_caused (would match if fully aware, same noisy perception -- their favorite just
      wasn't in their aware set), or noise_caused (still wouldn't match even with full awareness --
      their OWN perceived-utility noise misranks their true favorite). Feeds Section 24's
      "Diagnosing the Plurality Bump". None (default): no extra bookkeeping, no behavior change.

    honest_only: passed straight through to each method's resultsTable/multiResults (see
      Method.multiResults' own docstring) -- skips computing strategic/one-sided/smart-one-sided
      ballots entirely when True, since nothing past the Section 9 baseline run reads them.
      Default False (unchanged behavior) for callers like sweep_methods (Section 13) that still
      need the full chooser battery.

    vse_summary: {(label, chooser): [count, sum_vse, sum_vse_sq]} -- unchanged shape from
      before the checkpoint-4 Condorcet-efficiency addition below.
    ce_raw: (cw_exists_count, {(label, chooser): cw_wins_count}) -- ground-truth Condorcet
      bookkeeping. Whether a true CW exists in a given election is a property of the true
      electorate alone (see true_condorcet_winner above), not of any method or chooser, so it's
      a single shared scalar denominator rather than a per-key value like vse_summary's.
    """
    global TOTAL_ELECTIONS_RUN; TOTAL_ELECTIONS_RUN += niter
    if betrayal_targets and betrayal_sink is None:
        raise ValueError("betrayal_targets given but betrayal_sink is None -- pass a dict to collect into.")
    if coma_targets and coma_sink is None:
        raise ValueError("coma_targets given but coma_sink is None -- pass a dict to collect into.")
    if primary_cost_targets and primary_cost_sink is None:
        raise ValueError("primary_cost_targets given but primary_cost_sink is None -- pass a dict to collect into.")

    def _new_betrayal_acc():
        return dict(
            n_elections=0, n_decisive=0, n_betrayals=0, n_voter_corrupt=0, n_voter_decisive=0,
            sum_util_honest=0.0, sum_util_actual=0.0,
            sum_best_decisive=0.0, sum_rand_decisive=0.0, sum_best_all=0.0, sum_rand_all=0.0,
            n_flips=0, n_good_flips=0, n_bad_flips=0, n_honest_tied_flips=0,
            # "no flip" (noisy_upset < 0, decisive) analogue of n_aligned/n_silent_lockin below --
            # splits every DECISIVE betrayal into whether the runoff actively flipped to the wrong
            # finalist (that's n_bad_flips, tallied in the flip-direction block below) or silently
            # confirmed the noisy primary's own top pick even though it was honestly wrong
            # (n_silent_lockin -- "garbage in, garbage out": no flip occurs because the runoff has
            # no independent information source, so a corrupted primary pick just survives
            # unchallenged). n_aligned is the non-betrayal counterpart: the confirmed pick was
            # honestly right too.
            n_aligned=0, n_silent_lockin=0,
            sum_util_honest_bad_flip=0.0, sum_util_actual_bad_flip=0.0,
            sum_util_honest_lockin=0.0, sum_util_actual_lockin=0.0,
        )

    def _new_coma_acc():
        return dict(
            n_decisive_voters=0, n_decisive_elections=0,
            aligned=0, wrong_awareness_fixable=0, wrong_noise_unfixable=0,
            abstained_awareness_fixable=0, abstained_noise_unfixable=0,
            both_correct=0, coma_only_correct=0, groggy_only_correct=0, both_wrong=0,
            # VSE-cost fields (NEW) -- same population-denominator convention as
            # _new_betrayal_acc above, applied to the true_upset/coma_upset/groggy_upset signs
            # this function's caller already computes below, just also weighted by true utility.
            sum_best_all=0.0, sum_rand_all=0.0,
            n_groggy_bad_flip=0, n_groggy_silent_lockin=0,
            sum_util_true_groggy_bad_flip=0.0, sum_util_actual_groggy_bad_flip=0.0,
            sum_util_true_groggy_lockin=0.0, sum_util_actual_groggy_lockin=0.0,
            n_coma_bad_flip=0, n_coma_silent_lockin=0,
            sum_util_true_coma_bad_flip=0.0, sum_util_actual_coma_bad_flip=0.0,
            sum_util_true_coma_lockin=0.0, sum_util_actual_coma_lockin=0.0,
            sum_util_groggy_vs_coma=0.0,  # sum of (u_groggy_winner - u_coma_winner), net, unbucketed
        )

    def _new_primary_cost_acc():
        return dict(
            n_elections=0, n_decisive=0, n_finalist_set_changed=0,
            sum_util_ideal=0.0, sum_util_actual=0.0,
            sum_best_all=0.0, sum_rand_all=0.0,
        )

    def _new_primary_corruption_acc():
        return dict(n_elections=0, n_voters=0, aligned=0, awareness_caused=0, noise_caused=0)

    betrayal_scorers = {}
    for label, topRank in (betrayal_targets or []):
        betrayal_sink.setdefault(label, _new_betrayal_acc())
        betrayal_scorers[label] = Score(topRank, True)
    coma_scorers = {}
    for label, topRank in (coma_targets or []):
        coma_sink.setdefault(label, _new_coma_acc())
        coma_scorers[label] = Score(topRank, True)
    primary_cost_scorers = {}
    for label, topRank in (primary_cost_targets or []):
        primary_cost_sink.setdefault(label, _new_primary_cost_acc())
        primary_cost_scorers[label] = Score(topRank, True)
    if primary_corruption_sink is not None:
        primary_corruption_sink.update(_new_primary_corruption_acc())

    sim_start = time.time()
    summary = defaultdict(lambda: [0, 0.0, 0.0])
    cw_wins = defaultdict(int)
    cw_exists_count = 0
    paired_diff_summary = defaultdict(lambda: [0, 0.0, 0.0])
    paired_ce_summary = defaultdict(lambda: [0, 0.0, 0.0])
    for i in range(niter):
        true_electorate = electorates[i] if electorates is not None else model(nvot, ncand)
        perceived_electorate = make_perceived_electorate(true_electorate, epistemic_rho)
        ballot_electorate, genuine_sets, aware_sets = apply_participation_friction(
            perceived_electorate, true_electorate, awareness_alpha, fatigue_beta
        )
        if primary_corruption_sink is not None:
            acc = primary_corruption_sink
            acc["n_elections"] += 1
            for v in range(nvot):
                true_voter, perceived_voter = true_electorate[v], perceived_electorate[v]
                aware = aware_sets[v] if aware_sets is not None else set(range(ncand))
                true_favorite = max(range(ncand), key=lambda c: true_voter[c])
                voted_for = max(aware, key=lambda c: perceived_voter[c])
                acc["n_voters"] += 1
                if voted_for == true_favorite:
                    acc["aligned"] += 1
                elif max(range(ncand), key=lambda c: perceived_voter[c]) == true_favorite:
                    acc["awareness_caused"] += 1  # full awareness would have fixed this vote
                else:
                    acc["noise_caused"] += 1      # even full awareness wouldn't have -- perception itself is off
        if betrayal_targets:
            for label, _topRank in betrayal_targets:
                acc = betrayal_sink[label]
                score0to = betrayal_scorers[label]
                acc["n_elections"] += 1
                ballots = [score0to.honBallot(score0to, voter, None) for voter in ballot_electorate]
                honest_ballots = [score0to.honBallot(score0to, voter, None) for voter in true_electorate]
                base_results = list(map(score0to.candScore, zip(*ballots, strict=False)))
                runnerUp, top = sorted(range(len(base_results)), key=lambda ci: base_results[ci])[-2:]

                noisy_upset = sum(_sign4(b[runnerUp] - b[top]) for b in ballots)
                honest_upset = sum(_sign4(hb[runnerUp] - hb[top]) for hb in honest_ballots)

                utils = true_electorate.socUtils
                best, rand = max(utils), mean(utils)
                acc["sum_best_all"] += best
                acc["sum_rand_all"] += rand

                if noisy_upset != 0 and honest_upset != 0:
                    acc["n_decisive"] += 1
                    actual_winner = runnerUp if noisy_upset > 0 else top
                    honest_winner = runnerUp if honest_upset > 0 else top
                    acc["sum_util_honest"] += utils[honest_winner]
                    acc["sum_util_actual"] += utils[actual_winner]
                    acc["sum_best_decisive"] += best
                    acc["sum_rand_decisive"] += rand
                    if _sign4(noisy_upset) != _sign4(honest_upset):
                        acc["n_betrayals"] += 1
                        # A decisive betrayal is exactly one of two mechanically distinct cases:
                        # noisy_upset>0 (the runoff actively flipped to the wrong finalist -- also
                        # tallied as a "bad flip" in the flip-direction block below), or
                        # noisy_upset<0 (the runoff did nothing -- silently confirmed a finalist
                        # who was already honestly wrong). n_betrayals == n_bad_flips +
                        # n_silent_lockin exactly, since there's no third way for a decisive sign
                        # mismatch to happen.
                        if noisy_upset < 0:
                            acc["n_silent_lockin"] += 1
                            acc["sum_util_honest_lockin"] += utils[honest_winner]
                            acc["sum_util_actual_lockin"] += utils[actual_winner]
                    elif noisy_upset < 0:
                        acc["n_aligned"] += 1  # confirmed pick (top) was honestly right too

                for b, hb in zip(ballots, honest_ballots):
                    honest_sign = _sign4(hb[runnerUp] - hb[top])
                    if honest_sign != 0:
                        acc["n_voter_decisive"] += 1
                        if _sign4(b[runnerUp] - b[top]) != honest_sign:
                            acc["n_voter_corrupt"] += 1

                if noisy_upset > 0:
                    acc["n_flips"] += 1
                    if honest_upset > 0:
                        acc["n_good_flips"] += 1
                    elif honest_upset < 0:
                        acc["n_bad_flips"] += 1
                        acc["sum_util_honest_bad_flip"] += utils[top]        # honest_winner = top (honest_upset<0)
                        acc["sum_util_actual_bad_flip"] += utils[runnerUp]   # actual_winner = runnerUp (noisy_upset>0)
                    else:
                        acc["n_honest_tied_flips"] += 1
        if coma_targets:
            for label, _topRank in coma_targets:
                acc = coma_sink[label]
                score_obj = coma_scorers[label]
                ballots = [score_obj.honBallot(score_obj, voter, None) for voter in ballot_electorate]
                approval_scores = list(map(score_obj.candScore, zip(*ballots, strict=False)))
                runnerUp, top = sorted(range(len(approval_scores)), key=lambda ci: approval_scores[ci])[-2:]

                true_upset = coma_upset = groggy_upset = 0
                for v in range(nvot):
                    true_pref = _sign4(true_electorate[v][runnerUp] - true_electorate[v][top])
                    groggy_pref = _sign4(perceived_electorate[v][runnerUp] - perceived_electorate[v][top])
                    aware = aware_sets[v] if aware_sets is not None else {top, runnerUp}
                    if top in aware and runnerUp in aware:
                        coma_pref = groggy_pref
                    elif top in aware:
                        coma_pref = -1  # runnerUp floored to worst -- always loses this pair
                    elif runnerUp in aware:
                        coma_pref = 1
                    else:
                        coma_pref = 0  # abstains -- Top2Base's own documented behavior
                    true_upset += true_pref
                    coma_upset += coma_pref
                    groggy_upset += groggy_pref

                    if true_pref == 0:
                        continue  # no genuine preference -- excluded from the per-voter denominator
                    awareness_would_fix_it = (groggy_pref == true_pref)
                    if coma_pref == true_pref:
                        acc["aligned"] += 1
                    elif coma_pref == 0:
                        bucket = "abstained_awareness_fixable" if awareness_would_fix_it else "abstained_noise_unfixable"
                        acc[bucket] += 1
                    else:
                        bucket = "wrong_awareness_fixable" if awareness_would_fix_it else "wrong_noise_unfixable"
                        acc[bucket] += 1
                    acc["n_decisive_voters"] += 1

                if true_upset != 0:  # a genuine TRUE aggregate preference exists between these two finalists
                    acc["n_decisive_elections"] += 1
                    true_sign = _sign4(true_upset)
                    coma_correct = _sign4(coma_upset) == true_sign
                    groggy_correct = _sign4(groggy_upset) == true_sign
                    if coma_correct and groggy_correct:
                        acc["both_correct"] += 1
                    elif coma_correct:
                        acc["coma_only_correct"] += 1
                    elif groggy_correct:
                        acc["groggy_only_correct"] += 1
                    else:
                        acc["both_wrong"] += 1

                # VSE-cost bucketing (NEW) -- same fixed top/runnerUp finalist pair as above,
                # reusing true_upset/coma_upset/groggy_upset instead of re-simulating anything.
                # "true" stands in for Approval Top-2 (Clear-Eyed) here: its own runoff decision
                # is the true electorate directly (make_perceived_electorate at rho=1.0 is a
                # documented no-op), so true_upset's sign already IS Clear-Eyed's own decision --
                # see Top2Base._runoff_electorate. Same for groggy_upset vs "Approval Top-2".
                utils = true_electorate.socUtils
                best, rand = max(utils), mean(utils)
                acc["sum_best_all"] += best
                acc["sum_rand_all"] += rand
                if true_upset != 0:
                    true_winner = runnerUp if true_upset > 0 else top
                    if groggy_upset != 0:
                        groggy_winner = runnerUp if groggy_upset > 0 else top
                        if _sign4(groggy_upset) != _sign4(true_upset):
                            if groggy_upset > 0:
                                acc["n_groggy_bad_flip"] += 1
                                acc["sum_util_true_groggy_bad_flip"] += utils[true_winner]
                                acc["sum_util_actual_groggy_bad_flip"] += utils[groggy_winner]
                            else:
                                acc["n_groggy_silent_lockin"] += 1
                                acc["sum_util_true_groggy_lockin"] += utils[true_winner]
                                acc["sum_util_actual_groggy_lockin"] += utils[groggy_winner]
                    if coma_upset != 0:
                        coma_winner = runnerUp if coma_upset > 0 else top
                        if _sign4(coma_upset) != _sign4(true_upset):
                            if coma_upset > 0:
                                acc["n_coma_bad_flip"] += 1
                                acc["sum_util_true_coma_bad_flip"] += utils[true_winner]
                                acc["sum_util_actual_coma_bad_flip"] += utils[coma_winner]
                            else:
                                acc["n_coma_silent_lockin"] += 1
                                acc["sum_util_true_coma_lockin"] += utils[true_winner]
                                acc["sum_util_actual_coma_lockin"] += utils[coma_winner]
                if groggy_upset != 0 and coma_upset != 0:
                    groggy_winner_net = runnerUp if groggy_upset > 0 else top
                    coma_winner_net = runnerUp if coma_upset > 0 else top
                    acc["sum_util_groggy_vs_coma"] += utils[groggy_winner_net] - utils[coma_winner_net]
        if primary_cost_targets:
            for label, _topRank in primary_cost_targets:
                acc = primary_cost_sink[label]
                score_obj = primary_cost_scorers[label]
                # actual: real (noisy-primary) finalists, Groggy runoff -- same runoff
                # electorate (perceived_electorate) as the coma_targets block above uses for
                # groggy_upset, so this reproduces "Approval Top-2"'s own actual decision.
                actual_ballots = [score_obj.honBallot(score_obj, voter, None) for voter in ballot_electorate]
                actual_scores = list(map(score_obj.candScore, zip(*actual_ballots, strict=False)))
                runnerUp_a, top_a = sorted(range(len(actual_scores)), key=lambda ci: actual_scores[ci])[-2:]
                groggy_upset_actual = sum(_sign4(perceived_electorate[v][runnerUp_a] - perceived_electorate[v][top_a]) for v in range(nvot))

                # ideal: honest (zero-noise, zero-friction) primary tally picks its own finalist
                # pair -- possibly different from the actual pair above -- then the SAME Groggy
                # runoff electorate decides between THOSE finalists. Holds the runoff mechanism
                # fixed while isolating primary-noise-alone cost.
                honest_ballots = [score_obj.honBallot(score_obj, voter, None) for voter in true_electorate]
                honest_scores = list(map(score_obj.candScore, zip(*honest_ballots, strict=False)))
                runnerUp_h, top_h = sorted(range(len(honest_scores)), key=lambda ci: honest_scores[ci])[-2:]
                groggy_upset_ideal = sum(_sign4(perceived_electorate[v][runnerUp_h] - perceived_electorate[v][top_h]) for v in range(nvot))

                acc["n_elections"] += 1
                if {top_a, runnerUp_a} != {top_h, runnerUp_h}:
                    acc["n_finalist_set_changed"] += 1
                utils = true_electorate.socUtils
                acc["sum_best_all"] += max(utils)
                acc["sum_rand_all"] += mean(utils)
                if groggy_upset_actual != 0 and groggy_upset_ideal != 0:
                    acc["n_decisive"] += 1
                    actual_winner = runnerUp_a if groggy_upset_actual > 0 else top_a
                    ideal_winner = runnerUp_h if groggy_upset_ideal > 0 else top_h
                    acc["sum_util_ideal"] += utils[ideal_winner]
                    acc["sum_util_actual"] += utils[actual_winner]
        cw = true_condorcet_winner(true_electorate)
        if cw is not None:
            cw_exists_count += 1
        paired_vse_this_election = {}
        paired_cw_hit_this_election = {}
        for label, method in methods:
            for row in method.resultsTable(
                i, str(model), ncand, ballot_electorate, chooser_funs,
                media=media, scoring_voters=true_electorate, perceived_voters=perceived_electorate,
                genuine_sets=genuine_sets, aware_sets=aware_sets, primary_awareness_alpha=awareness_alpha,
                honest_only=honest_only,
            ):
                acc = summary[(label, row["chooser"])]
                acc[0] += 1
                acc[1] += row["vse"]
                acc[2] += row["vse"] ** 2
                if raw_vse_sink is not None:
                    raw_vse_sink[(label, row["chooser"])].append(row["vse"])
                if cw is not None and row["winner"] == cw:
                    cw_wins[(label, row["chooser"])] += 1
                if paired_diff_pairs and row["chooser"] == paired_diff_chooser:
                    paired_vse_this_election[label] = row["vse"]
                if paired_ce_pairs and cw is not None and row["chooser"] == paired_diff_chooser:
                    paired_cw_hit_this_election[label] = int(row["winner"] == cw)
        if paired_diff_pairs:
            for label, baseline_label in paired_diff_pairs:
                if label not in paired_vse_this_election or baseline_label not in paired_vse_this_election:
                    continue
                d = paired_vse_this_election[label] - paired_vse_this_election[baseline_label]
                acc = paired_diff_summary[(label, baseline_label)]
                acc[0] += 1
                acc[1] += d
                acc[2] += d ** 2
        if paired_ce_pairs and cw is not None:
            for label, baseline_label in paired_ce_pairs:
                if label not in paired_cw_hit_this_election or baseline_label not in paired_cw_hit_this_election:
                    continue
                d = paired_cw_hit_this_election[label] - paired_cw_hit_this_election[baseline_label]
                acc = paired_ce_summary[(label, baseline_label)]
                acc[0] += 1
                acc[1] += d
                acc[2] += d ** 2
        if (i + 1) % 100 == 0:
            print(f"Simulated {i + 1}/{niter} elections in {time.time() - sim_start:.1f}s")
    print(f"Simulation done in {time.time() - sim_start:.1f}s")
    return dict(summary), (cw_exists_count, dict(cw_wins)), dict(paired_diff_summary), dict(paired_ce_summary)


def reduce_to_mean_ci(summary):
    """Turn {(label, chooser): (count, sum, sum_sq)} into {(label, chooser): (mean, ci95_half_width)}."""
    reduced = {}
    for key, (count, total, total_sq) in summary.items():
        avg = total / count
        if count < 2:
            ci = 0.0
        else:
            variance = max(0.0, (total_sq - total ** 2 / count) / (count - 1))
            ci = 1.96 * math.sqrt(variance / count)
        reduced[key] = (avg, ci)
    return reduced


def reduce_to_ce(ce_raw, keys):
    """(cw_exists_count, {(label,chooser): cw_wins}) -> {(label,chooser): raw_ce} for every
    key in `keys` (pass e.g. reduce_to_mean_ci(...).keys()), so a method with a true 0% CE
    still gets an explicit entry rather than being silently absent. NaN if no election in this
    run ever had a true Condorcet winner at all (CE is undefined, not zero, in that case)."""
    cw_exists_count, cw_wins = ce_raw
    if cw_exists_count == 0:
        return {key: float("nan") for key in keys}
    return {key: cw_wins.get(key, 0) / cw_exists_count for key in keys}


def relative_ce(raw_ce, baseline_label="Condorcet (Schulze)"):
    """{(label,chooser): raw_ce} -> {(label,chooser): raw_ce / raw_ce[(baseline_label,chooser)]}.
    Omits a key if this run didn't include baseline_label with a matching chooser, or if the
    baseline's own raw CE is missing, exactly 0 (avoids a ZeroDivisionError), or NaN (`x == x`
    is False only for NaN -- bool(nan) alone is True, so a plain truthiness check isn't enough)."""
    out = {}
    for (label, chooser), val in raw_ce.items():
        base_val = raw_ce.get((baseline_label, chooser))
        if base_val and base_val == base_val:
            out[(label, chooser)] = val / base_val
    return out


def reduce_betrayal_summary(acc):
    """Turn one betrayal_sink[label] running-sum dict (see run_vse_simulation's betrayal_targets
    doc) into the same rate/cost fields the old (now-removed) runoff_betrayal_stats/
    runoff_flip_stats functions used to compute at the end of their own standalone loops --
    betrayal_rate, voter_corruption_rate, decisive_vse_cost, population_vse_cost, plus
    flip-direction rates. Same "ratio of means, not mean of ratios" denominator convention as
    before -- see run_vse_simulation's betrayal_targets docstring for why.

    n_aligned/n_silent_lockin (NEW): the "no flip" analogue of n_good_flips/n_bad_flips -- among
    DECISIVE elections where the runoff did NOT flip away from the noisy primary's own top pick,
    whether that confirmed pick was honestly correct (aligned) or honestly WRONG (silent_lockin --
    the runoff has no independent information source, so a primary corrupted by epistemic_rho/
    awareness_alpha/fatigue_beta just gets rubber-stamped rather than corrected: the "garbage in,
    garbage out" failure mode). n_betrayals == n_bad_flips + n_silent_lockin exactly.

    aligned_share/silent_lockin_share/bad_flip_share/good_flip_share/other_share (NEW): the same
    four buckets plus a residual "other" (exact noisy ties, plus elections with no clear honest
    preference between the two finalists -- expected to be a small share), each as a fraction of
    ALL elections (not just decisive/flip ones) -- these five sum to 1.0 exactly, by construction
    (other_share is defined as the leftover, not derived from a separate condition).

    bad_flip_vse_cost/silent_lockin_vse_cost (NEW): population_vse_cost split between its two
    contributing failure modes -- aligned/good-flip elections contribute zero net cost (same
    winner either way), so these two sum to population_vse_cost exactly."""
    n_decisive = acc["n_decisive"]
    n_voter_decisive = acc["n_voter_decisive"]
    n_flips = acc["n_flips"]
    n_elections = acc["n_elections"]
    decisive_denom = acc["sum_best_decisive"] - acc["sum_rand_decisive"]
    population_denom = acc["sum_best_all"] - acc["sum_rand_all"]
    decisive_vse_cost = ((acc["sum_util_honest"] - acc["sum_util_actual"]) / decisive_denom) if not isclose(decisive_denom, 0) else float("nan")
    population_vse_cost = ((acc["sum_util_honest"] - acc["sum_util_actual"]) / population_denom) if not isclose(population_denom, 0) else float("nan")
    n_other = n_elections - acc["n_aligned"] - acc["n_silent_lockin"] - acc["n_bad_flips"] - acc["n_good_flips"]
    bad_flip_vse_cost = ((acc["sum_util_honest_bad_flip"] - acc["sum_util_actual_bad_flip"]) / population_denom) if not isclose(population_denom, 0) else float("nan")
    silent_lockin_vse_cost = ((acc["sum_util_honest_lockin"] - acc["sum_util_actual_lockin"]) / population_denom) if not isclose(population_denom, 0) else float("nan")
    return dict(
        n_decisive=n_decisive, n_betrayals=acc["n_betrayals"],
        betrayal_rate=(acc["n_betrayals"] / n_decisive if n_decisive else float("nan")),
        voter_corruption_rate=(acc["n_voter_corrupt"] / n_voter_decisive if n_voter_decisive else float("nan")),
        decisive_vse_cost=decisive_vse_cost, population_vse_cost=population_vse_cost,
        n_elections=n_elections, n_flips=n_flips,
        flip_rate=(n_flips / n_elections if n_elections else float("nan")),
        n_good_flips=acc["n_good_flips"], n_bad_flips=acc["n_bad_flips"],
        n_honest_tied_flips=acc["n_honest_tied_flips"],
        good_flip_rate=(acc["n_good_flips"] / n_flips if n_flips else float("nan")),
        bad_flip_rate=(acc["n_bad_flips"] / n_flips if n_flips else float("nan")),
        n_aligned=acc["n_aligned"], n_silent_lockin=acc["n_silent_lockin"], n_other=n_other,
        aligned_share=(acc["n_aligned"] / n_elections if n_elections else float("nan")),
        silent_lockin_share=(acc["n_silent_lockin"] / n_elections if n_elections else float("nan")),
        bad_flip_share=(acc["n_bad_flips"] / n_elections if n_elections else float("nan")),
        good_flip_share=(acc["n_good_flips"] / n_elections if n_elections else float("nan")),
        other_share=(n_other / n_elections if n_elections else float("nan")),
        bad_flip_vse_cost=bad_flip_vse_cost,
        silent_lockin_vse_cost=silent_lockin_vse_cost,
    )


def reduce_coma_summary(acc):
    """Turn one coma_sink[label] running-count dict (see run_vse_simulation's coma_targets doc)
    into the same rate fields the old (now-removed) at2_coma_corruption_stats function used to
    compute at the end of its own standalone loop."""
    n_decisive_voters = acc["n_decisive_voters"]
    n_decisive_elections = acc["n_decisive_elections"]
    rates = {k: (acc[k] / n_decisive_voters if n_decisive_voters else float("nan"))
             for k in ["aligned", "wrong_awareness_fixable", "wrong_noise_unfixable",
                       "abstained_awareness_fixable", "abstained_noise_unfixable"]}
    rates["awareness_attributable"] = rates["wrong_awareness_fixable"] + rates["abstained_awareness_fixable"]
    rates["noise_unfixable"] = rates["wrong_noise_unfixable"] + rates["abstained_noise_unfixable"]
    rates["n_decisive_voters"] = n_decisive_voters

    election_rates = {k: (acc[k] / n_decisive_elections if n_decisive_elections else float("nan"))
                       for k in ["both_correct", "coma_only_correct", "groggy_only_correct", "both_wrong"]}
    rates["coma_accuracy_rate"] = election_rates["both_correct"] + election_rates["coma_only_correct"]
    rates["groggy_accuracy_rate"] = election_rates["both_correct"] + election_rates["groggy_only_correct"]
    rates["both_correct_rate"] = election_rates["both_correct"]
    rates["coma_only_correct_rate"] = election_rates["coma_only_correct"]
    rates["groggy_only_correct_rate"] = election_rates["groggy_only_correct"]
    rates["both_wrong_rate"] = election_rates["both_wrong"]
    rates["n_decisive_elections"] = n_decisive_elections

    population_denom = acc["sum_best_all"] - acc["sum_rand_all"]

    def _cost(numer):
        return (numer / population_denom) if not isclose(population_denom, 0) else float("nan")

    rates["groggy_bad_flip_vse_cost"] = _cost(acc["sum_util_true_groggy_bad_flip"] - acc["sum_util_actual_groggy_bad_flip"])
    rates["groggy_silent_lockin_vse_cost"] = _cost(acc["sum_util_true_groggy_lockin"] - acc["sum_util_actual_groggy_lockin"])
    rates["coma_bad_flip_vse_cost"] = _cost(acc["sum_util_true_coma_bad_flip"] - acc["sum_util_actual_coma_bad_flip"])
    rates["coma_silent_lockin_vse_cost"] = _cost(acc["sum_util_true_coma_lockin"] - acc["sum_util_actual_coma_lockin"])
    rates["coma_vs_groggy_vse_cost"] = _cost(acc["sum_util_groggy_vs_coma"])
    return rates


def reduce_primary_cost_summary(acc):
    """Turn one primary_cost_sink[label] running-sum dict (see run_vse_simulation's
    primary_cost_targets doc) into finalist_set_changed_rate/primary_noise_vse_cost -- same
    population-denominator convention as reduce_betrayal_summary, but comparing the real
    (noisy-primary) Groggy winner against a counterfactual Groggy winner between the finalists
    an honest primary would have picked instead, holding the runoff's own information level
    (Groggy) fixed."""
    n_elections = acc["n_elections"]
    n_decisive = acc["n_decisive"]
    population_denom = acc["sum_best_all"] - acc["sum_rand_all"]
    primary_noise_vse_cost = ((acc["sum_util_ideal"] - acc["sum_util_actual"]) / population_denom) if not isclose(population_denom, 0) else float("nan")
    return dict(
        n_elections=n_elections, n_decisive=n_decisive,
        finalist_set_changed_rate=(acc["n_finalist_set_changed"] / n_elections if n_elections else float("nan")),
        primary_noise_vse_cost=primary_noise_vse_cost,
    )


def reduce_primary_corruption_summary(acc):
    """Turn one primary_corruption_sink running-count dict (see run_vse_simulation's
    primary_corruption_sink doc) into rate fields -- the noise-vs-awareness split behind Section
    24's "Diagnosing the Plurality Bump": of all voters, what fraction voted for their true
    favorite (aligned), couldn't have even with full awareness (noise_caused -- their own
    perceived-utility noise misranked their true favorite), or simply didn't know about their true
    favorite (awareness_caused -- full awareness, same noisy perception, would have fixed it)."""
    n = acc["n_voters"]
    return dict(
        n_elections=acc["n_elections"], n_voters=n,
        aligned_rate=(acc["aligned"] / n if n else float("nan")),
        awareness_caused_rate=(acc["awareness_caused"] / n if n else float("nan")),
        noise_caused_rate=(acc["noise_caused"] / n if n else float("nan")),
        corruption_rate=((acc["awareness_caused"] + acc["noise_caused"]) / n if n else float("nan")),
    )
