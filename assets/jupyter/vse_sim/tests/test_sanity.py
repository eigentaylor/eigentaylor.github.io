"""The notebook's own sanity checks, as tests.

Sections 2, 3 and 4 of `vse_simulation.ipynb` each end with a block of `assert`s that
verify a mechanism behaves as documented -- that `rho=1.0` really is a no-op, that
floored candidates really are tied rather than arbitrarily ordered, that Coma really
reuses the primary's awareness instead of redrawing it. Those blocks are reproduced here
verbatim, one per test, so they run in CI instead of only when someone re-executes an
80-minute notebook.

Nothing here is new: each test body is copied from the cell named in its docstring.
"""
import math
import random

import numpy as np
from numpy import isclose
from numpy.lib.scimath import sqrt

from vse_sim.friction import (FRICTION_TIE_EPSILON, _floor_to_genuine,
                              apply_participation_friction)
from vse_sim.noise import draw_noise, make_perceived_electorate
from vse_sim.condorcet import true_condorcet_winner
from vse_sim.top2 import ApprovalTop2, PluralityTop2
from vse_sim.vendored.methods.irv import (Irv, build_preference_schedule,
                                          candidate_votes, eliminate_candidate,
                                          least_candidate, rank_vector_to_preference)
from vse_sim.vendored.methods.schulze import Schulze
from vse_sim.vendored.methods.score import Score
from vse_sim.vendored.voter_models import Electorate, RandomModel, Voter
from numpy import sign as _sign2

# Quick sanity check on a small hand-built electorate: a classic vote-splitting setup where
# the primary leader (candidate 0, "A") is NOT the pairwise-preferred candidate overall, so the
# runoff should flip the outcome to the primary's runner-up (candidate 1, "B").
#   group 1 (4 voters): utils [10, 5, 0]  -- favorite A, 2nd B, least C
#   group 2 (3 voters): utils [0, 10, 5]  -- favorite B, 2nd C, least A
#   group 3 (2 voters): utils [0, 5, 10]  -- favorite C, 2nd B, least A
# Primary (favorite-vote) tally: A=4, B=3, C=2 -- top-2 = {A, B}, C is eliminated.
# Pairwise A vs. B: group 1 (4 voters) prefers A; groups 2+3 (3+2=5 voters) prefer B. B wins the
# pairwise runoff 5-4 even though A led the primary -- the runoff should flip the winner to B.
_sanity_electorate = Electorate(
    [Voter([10, 5, 0])] * 4 + [Voter([0, 10, 5])] * 3 + [Voter([0, 5, 10])] * 2
)


def test_epistemic_noise():
    """`rho=1.0` is an exact no-op; `rho<1` produces a distinct, perturbed electorate.
    Reusing the same `noise` at two different `rho` values reproduces the formula
    exactly by hand; omitting `noise` still draws independent randomness per call.

    Copied from cell 23 of `vse_simulation.ipynb` (lines 34-55).
    """
    # Sanity check: rho=1.0 must be an exact no-op; rho<1 must actually perturb utilities.
    _test_electorate = RandomModel()(5, 3)
    assert make_perceived_electorate(_test_electorate, 1.0) is _test_electorate
    _perceived_partial = make_perceived_electorate(_test_electorate, 0.5)
    assert _perceived_partial is not _test_electorate
    assert _perceived_partial != _test_electorate

    # Sanity check for the new `noise` param: reusing the SAME noise at two different rho values must
    # match the formula applied by hand (deterministic given noise), and omitting `noise` must still
    # draw independent randomness each call (so every existing caller is unaffected).
    _noise_electorate = RandomModel()(4, 3)
    _shared_noise = draw_noise(_noise_electorate)
    _perceived_t3 = make_perceived_electorate(_noise_electorate, 0.3, noise=_shared_noise)
    _perceived_t7 = make_perceived_electorate(_noise_electorate, 0.7, noise=_shared_noise)
    for _voter, _z_row, _v3, _v7 in zip(_noise_electorate, _shared_noise, _perceived_t3, _perceived_t7, strict=True):
        _sigma = np.std(_voter)
        for _u, _z, _p3, _p7 in zip(_voter, _z_row, _v3, _v7, strict=True):
            assert isclose(_p3, 0.3 * _u + sqrt(1 - 0.3 * 0.3) * _sigma * _z)
            assert isclose(_p7, 0.7 * _u + sqrt(1 - 0.7 * 0.7) * _sigma * _z)
    _fresh_a = make_perceived_electorate(_noise_electorate, 0.5)
    _fresh_b = make_perceived_electorate(_noise_electorate, 0.5)
    assert _fresh_a != _fresh_b, "omitting noise= should still draw independent randomness each call"


def test_top2_runoff_can_flip_the_primary_winner():
    """A leads the primary (4 of 9 votes) but loses the runoff to runner-up B, because B
    beats A pairwise 5-4 once C's voters' second choices count.

    Copied from cell 25 of `vse_simulation.ipynb` (lines 259-278).
    """
    # Quick sanity check on a small hand-built electorate: a classic vote-splitting setup where
    # the primary leader (candidate 0, "A") is NOT the pairwise-preferred candidate overall, so the
    # runoff should flip the outcome to the primary's runner-up (candidate 1, "B").
    #   group 1 (4 voters): utils [10, 5, 0]  -- favorite A, 2nd B, least C
    #   group 2 (3 voters): utils [0, 10, 5]  -- favorite B, 2nd C, least A
    #   group 3 (2 voters): utils [0, 5, 10]  -- favorite C, 2nd B, least A
    # Primary (favorite-vote) tally: A=4, B=3, C=2 -- top-2 = {A, B}, C is eliminated.
    # Pairwise A vs. B: group 1 (4 voters) prefers A; groups 2+3 (3+2=5 voters) prefer B. B wins the
    # pairwise runoff 5-4 even though A led the primary -- the runoff should flip the winner to B.
    _sanity_electorate = Electorate(
        [Voter([10, 5, 0])] * 4 + [Voter([0, 10, 5])] * 3 + [Voter([0, 5, 10])] * 2
    )
    _plur_top2 = PluralityTop2()
    _hon_ballot_fn = _plur_top2.honBallotFor(_sanity_electorate)
    _ballots = [_hon_ballot_fn(PluralityTop2, voter, None) for voter in _sanity_electorate]
    _plur_top2._current_voters = _sanity_electorate
    _primary_scores = list(map(_plur_top2.candScore, zip(*_ballots, strict=False)))
    _final_scores = _plur_top2.results(_ballots)
    assert _plur_top2.winner(_primary_scores) == 0, "sanity: candidate 0 (A) should lead the primary"
    assert _plur_top2.winner(_final_scores) == 1, "expected the pairwise runoff to flip the winner to candidate 1 (B)"


def test_participation_friction():
    """`1.0/1.0` is an exact no-op (and returns `genuine_sets=aware_sets=None`); partial
    friction perturbs the electorate and returns one genuine set and one
    (always-superset) aware set per voter; maximum friction leaves no voter with an
    empty set; and `aware_sets` is bit-identical across `fatigue_beta` values at fixed
    `awareness_alpha` -- a direct proof that fatigue cannot affect a choose-one method.

    Copied from cell 27 of `vse_simulation.ipynb` (lines 96-135).
    """
    # Sanity checks.
    _test_electorate2 = RandomModel()(20, 6)
    _noop_result, _noop_genuine, _noop_aware = apply_participation_friction(_test_electorate2, _test_electorate2, 1.0, 1.0)
    assert _noop_result is _test_electorate2 and _noop_genuine is None and _noop_aware is None
    _friction_partial, _friction_partial_genuine, _friction_partial_aware = apply_participation_friction(_test_electorate2, _test_electorate2, 0.3, 1.0)
    assert _friction_partial != _test_electorate2
    assert len(_friction_partial_genuine) == len(_test_electorate2)
    assert len(_friction_partial_aware) == len(_test_electorate2)
    # genuine requires BOTH awareness AND not-fatigued, so genuine_sets must always be a subset of
    # aware_sets for the same voter -- the invariant Top2Base's runoff_coma fix depends on.
    for _g, _a in zip(_friction_partial_genuine, _friction_partial_aware, strict=True):
        assert _g <= _a, "genuine_sets must always be a subset of aware_sets for the same voter"

    # Edge-case guarantee: even at maximum friction on both mechanisms, every voter ends up with
    # at least one genuinely-evaluated (non-floored) candidate -- i.e. min() never sees an empty set.
    _extreme_electorate = RandomModel()(200, 6)
    _extreme_friction, _extreme_genuine, _extreme_aware = apply_participation_friction(_extreme_electorate, _extreme_electorate, 0.0, 0.0)
    for _voter_before, _voter_after in zip(_extreme_electorate, _extreme_friction, strict=True):
        assert len(set(_voter_after)) >= 1  # trivially true, but confirms construction didn't raise/crash
    for _genuine in _extreme_genuine:
        assert len(_genuine) >= 1
    for _aware in _extreme_aware:
        assert len(_aware) >= 1

    # Fatigue-invariance proof (see Section 24, "Diagnosing the Plurality Bump"): favorite_known is
    # guaranteed genuine and is always the max-utility AWARE candidate -- a fact that never reads
    # fatigue_beta at all (p_aware depends only on awareness_alpha/prominence_rank). So aware_sets,
    # and therefore any choose-one method's honest vote, must be bit-identical regardless of
    # fatigue_beta, given the same random stream position -- proven directly here, not just observed
    # statistically: snapshot the RNG state, run at fatigue_beta=1.0, restore the snapshot, run again
    # at fatigue_beta=0.0 (same awareness_alpha, same electorate), and require aware_sets to match
    # exactly (genuine_sets are NOT required to match -- fatigue affects those, correctly).
    _fatigue_test_electorate = RandomModel()(30, 6)
    _rng_snapshot = random.getstate()
    _, _, _fatigue_test_aware_hi = apply_participation_friction(_fatigue_test_electorate, _fatigue_test_electorate, 0.5, 1.0)
    random.setstate(_rng_snapshot)
    _, _, _fatigue_test_aware_lo = apply_participation_friction(_fatigue_test_electorate, _fatigue_test_electorate, 0.5, 0.0)
    assert _fatigue_test_aware_hi == _fatigue_test_aware_lo, (
        "aware_sets must be identical regardless of fatigue_beta -- fatigue only affects genuine_sets"
    )


def test_ranked_ballot_friction_keeps_floored_candidates_tied():
    """Floored/unaware candidates end up genuinely TIED with each other (Schulze) or
    genuinely EXCLUDED from the ranking (IRV) -- not in an arbitrarily broken strict
    order.

    Copied from cell 29 of `vse_simulation.ipynb` (lines 1-69).
    """
    # Sanity checks for the ranked-ballot friction fix above: floored/unaware candidates should be
    # genuinely TIED with each other (Schulze) or genuinely EXCLUDED from the ranking (IRV) -- not
    # an arbitrarily broken strict order.

    # --- Schulze: two candidates floored for every voter -> tied pairwise margin, both still
    # strictly below the worst genuinely-evaluated candidate. ---
    random.seed(12345)
    _sch_voters = Electorate([Voter([10.0, 7.0, 4.0, 1.0]) for _ in range(20)])
    _forced_ballots = []
    for _v in _sch_voters:
        _tie_floor = min(_v[0], _v[1])  # candidates 0,1 ("A","B") genuine; 2,3 ("C","D") floored
        _floored = {c: _tie_floor - FRICTION_TIE_EPSILON for c in (2, 3)}
        _forced_ballots.append(Voter(_v[c] if c in (0, 1) else _floored[c] for c in range(4)))
    _forced_electorate = Electorate(_forced_ballots)

    _schulze = Schulze()
    _hon_ballots = [_schulze.honBallot(Schulze, v) for v in _forced_electorate]
    _cmat = [[0] * 4 for _ in range(4)]
    for _i in range(4):
        for _j in range(4):
            if _i != _j:
                _cmat[_i][_j] = sum(_sign2(b[_i] - b[_j]) for b in _hon_ballots)
    assert _cmat[2][3] == 0 and _cmat[3][2] == 0, "C and D should be exactly tied (0 pairwise margin)"
    assert _cmat[1][2] == len(_forced_electorate) and _cmat[1][3] == len(_forced_electorate), (
        "B (genuine, worse than A) should strictly beat both floored C and D on every ballot"
    )
    assert _cmat[0][1] == len(_forced_electorate), "A should strictly beat B (both genuine)"

    # --- IRV: a voter whose only two genuinely-evaluated candidates both get eliminated should
    # have their ballot EXHAUST (drop out), not fall through to an unranked candidate. ---
    random.seed(999)
    _irv = Irv()
    _irv_true = Electorate(
        [Voter([10.0, 5.0, 1.0, 0.0])] * 3     # genuine {0,1}: prefers 0 over 1
        + [Voter([0.0, 1.0, 10.0, 5.0])] * 2    # genuine {2,3}: prefers 2 over 3
        + [Voter([0.0, 1.0, 5.0, 10.0])] * 4    # fully genuine: prefers 3 > 2 > 1 > 0
    )
    _irv._genuine_sets = [{0, 1}] * 3 + [{2, 3}] * 2 + [{0, 1, 2, 3}] * 4
    _hon_fn = _irv.honBallotFor(_irv_true)
    _irv_ballots = [_hon_fn(Irv, v, None) for v in _irv_true]
    assert _irv_ballots[0][2] == -1 and _irv_ballots[0][3] == -1, "candidates 2,3 should be unranked for voter 0"
    assert _irv_ballots[3][0] == -1 and _irv_ballots[3][1] == -1, "candidates 0,1 should be unranked for voter 3"
    assert _irv_ballots[8][0] != -1, "the fully-genuine voter should have every candidate ranked"

    _rankings = [rank_vector_to_preference(b) for b in _irv_ballots]
    assert _rankings[0] == [0, 1], "voter 0's preference should be exactly [0, 1] (truncated)"
    assert _rankings[3] == [2, 3], "voter 3's preference should be exactly [2, 3] (truncated)"
    _irv_final = _irv.runIrv(build_preference_schedule(_rankings), 4)
    # Candidate 1 is never anyone's first choice and gets eliminated round 1; group-1 voters' only
    # other candidate (0) is eliminated round 3, at which point their ballots EXHAUST -- they never
    # fall through to 2 or 3, which they never evaluated. Candidate 3 wins on the votes that
    # survive. This is a real elimination trace, not just a no-crash check.
    assert _irv_final == [3, 0, 2, 1], f"expected finish order [3, 0, 2, 1] (winner first), got {_irv_final}"

    # --- Extreme friction (AWARENESS_ALPHA=FATIGUE_BETA=0.0): a candidate can end up absent from EVERY
    # voter's genuine set at once -- confirms candidate_votes' remaining_candidates backfill keeps
    # runIrv's fixed ncand-round elimination loop from crashing in that case. ---
    random.seed(7)
    _extreme_true = RandomModel()(40, 6)
    _extreme_ballot_electorate, _extreme_genuine, _extreme_aware = apply_participation_friction(
        make_perceived_electorate(_extreme_true, 1.0), _extreme_true, 0.0, 0.0
    )
    _irv2 = Irv()
    _irv2._genuine_sets = _extreme_genuine
    _extreme_hon_fn = _irv2.honBallotFor(_extreme_ballot_electorate)
    _extreme_ballots = [_extreme_hon_fn(Irv, v, None) for v in _extreme_ballot_electorate]
    _extreme_rankings = [rank_vector_to_preference(b) for b in _extreme_ballots]
    _extreme_result = _irv2.runIrv(build_preference_schedule(_extreme_rankings), 6)
    assert set(_extreme_result) == set(range(6)), f"expected all 6 candidates accounted for, got {_extreme_result}"


def test_coma_runoff_reuses_the_primarys_own_awareness():
    """`runoff_coma=True` reuses the primary's own realized `aware_sets` with no new
    randomness: it reduces to the baseline runoff when there was no friction, and
    otherwise implements 'vote for whichever finalist you knew, abstain if neither'.

    Copied from cell 30 of `vse_simulation.ipynb` (lines 1-68).
    """
    # Sanity check for Top2Base's runoff_coma=True (Section 3): reuses the primary's own realized
    # aware_sets directly (no new randomness), rather than the previous (buggy) behavior of
    # re-drawing awareness fresh at the primary's rate. Three things to confirm: (1) with no
    # aware_sets at all (a primary that had no friction), Coma reduces to exactly Baseline's runoff
    # electorate; (2) same when every voter is aware of every candidate; (3) with a hand-picked
    # aware_sets fixing which finalist(s) each voter actually knew, Coma implements "vote for
    # whichever finalist you knew, abstain if neither" exactly -- not just "differs from Baseline
    # somewhere," which is all the old version of this check verified.
    _frozen_true = Electorate([Voter([10.0, 8.0, 3.0, 1.0]) for _ in range(4)])
    _frozen_perceived = _frozen_true  # no epistemic noise needed here -- friction alone is under test

    _baseline_at2 = ApprovalTop2(runoff_rho=None)
    _baseline_at2._current_voters = _frozen_perceived
    _baseline_at2._scoring_voters = _frozen_true
    _baseline_at2._perceived_voters = _frozen_perceived
    _baseline_electorate = [list(v) for v in _baseline_at2._runoff_electorate()]

    # (1) aware_sets=None -- no primary friction happened at all.
    _coma_no_friction = ApprovalTop2(runoff_rho=None, runoff_coma=True)
    _coma_no_friction._current_voters = _frozen_perceived
    _coma_no_friction._scoring_voters = _frozen_true
    _coma_no_friction._perceived_voters = _frozen_perceived
    _coma_no_friction._aware_sets = None
    _coma_no_friction_electorate = [list(v) for v in _coma_no_friction._runoff_electorate()]
    assert _baseline_electorate == _coma_no_friction_electorate, (
        "Coma with aware_sets=None (no primary friction) should reduce to exactly Baseline's runoff electorate"
    )

    # (2) every voter aware of every candidate -- same result via the "real" path instead of the
    # None fast path.
    _coma_all_aware = ApprovalTop2(runoff_rho=None, runoff_coma=True)
    _coma_all_aware._current_voters = _frozen_perceived
    _coma_all_aware._scoring_voters = _frozen_true
    _coma_all_aware._perceived_voters = _frozen_perceived
    _coma_all_aware._aware_sets = [{0, 1, 2, 3}] * 4
    _coma_all_aware_electorate = [list(v) for v in _coma_all_aware._runoff_electorate()]
    assert _baseline_electorate == _coma_all_aware_electorate, (
        "Coma with every voter aware of every candidate should also match Baseline exactly"
    )

    # (3) the actual semantics, at fixed finalists 0 and 1 (testing _runoff_electorate() directly
    # against a hand-picked aware_sets -- not re-deriving the primary's top-2 here):
    #   voter 0: aware of BOTH finalists (0, 1) -> sees their real preference (0 > 1: 10 > 8)
    #   voter 1: aware of finalist 0 only ({0, 2}) -> finalist 0 keeps its real value, 1 is floored
    #   voter 2: aware of finalist 1 only ({1, 3}) -> finalist 1 keeps its real value, 0 is floored
    #   voter 3: aware of NEITHER finalist ({2, 3}) -> both floored to the exact same value (abstains)
    _semantics_aware_sets = [{0, 1}, {0, 2}, {1, 3}, {2, 3}]
    _coma_semantics = ApprovalTop2(runoff_rho=None, runoff_coma=True)
    _coma_semantics._current_voters = _frozen_true
    _coma_semantics._scoring_voters = _frozen_true
    _coma_semantics._perceived_voters = _frozen_true
    _coma_semantics._aware_sets = _semantics_aware_sets
    _semantics_electorate = list(_coma_semantics._runoff_electorate())

    assert _semantics_electorate[0][0] == 10.0 and _semantics_electorate[0][1] == 8.0, (
        "voter 0 (aware of both finalists) should see their real, unfloored preference"
    )
    assert _semantics_electorate[1][0] == 10.0, "voter 1 (aware of finalist 0 only) should see finalist 0's real value"
    assert _semantics_electorate[1][1] < _semantics_electorate[1][0], (
        "voter 1 should have finalist 1 floored below finalist 0 -- they never evaluated it"
    )
    assert _semantics_electorate[2][1] == 8.0, "voter 2 (aware of finalist 1 only) should see finalist 1's real value"
    assert _semantics_electorate[2][0] < _semantics_electorate[2][1], (
        "voter 2 should have finalist 0 floored below finalist 1 -- they never evaluated it"
    )
    assert _semantics_electorate[3][0] == _semantics_electorate[3][1], (
        "voter 3 (aware of neither finalist) should have both floored to the SAME tied value -- abstains"
    )


def test_true_condorcet_winner():
    """Finds the sole true CW in a clear-winner electorate, and correctly reports `None`
    for both a genuine cycle and a pure-tie electorate.

    Copied from cell 36 of `vse_simulation.ipynb` (lines 25-35).
    """
    # Sanity checks: a clear CW (reusing Top2Base's hand-built electorate above -- B beats both A
    # and C pairwise), a genuine 3-way Condorcet cycle, and an electorate with only exact ties.
    assert true_condorcet_winner(_sanity_electorate) == 1  # B beats A (5-4) and C (7-2)

    _cycle_electorate = Electorate(
        [Voter([3, 2, 1])] * 3 + [Voter([1, 3, 2])] * 3 + [Voter([2, 1, 3])] * 3
    )  # rock-paper-scissors: 0 beats 1 (6-3), 1 beats 2 (6-3), 2 beats 0 (6-3) -- no true CW
    assert true_condorcet_winner(_cycle_electorate) is None

    _tie_electorate = Electorate([Voter([1, 0, -1])] * 2 + [Voter([-1, 0, 1])] * 2)  # every pair ties 2-2
    assert true_condorcet_winner(_tie_electorate) is None
