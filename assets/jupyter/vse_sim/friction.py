"""Participation friction (section 4 of `vse_simulation.ipynb`, cell 27).

Unfamiliarity and ballot fatigue decide which candidates a voter genuinely
evaluates. Original to this project, not part of vse-sim.
"""

import random

from .vendored.voter_models import Electorate, Voter


FRICTION_TIE_EPSILON = 1e-9  # fixed, not random -- see the comment inside the function below.


def _floor_to_genuine(electorate, genuine_sets):
    """Build the ballot electorate a voter would submit given an ALREADY-KNOWN set of
    genuinely-evaluated candidates per voter -- no randomness drawn here at all. Shared by
    apply_participation_friction (which draws genuine_sets fresh below) and Top2Base's
    runoff_coma path (which reuses the primary's own already-realized aware_sets directly, with
    zero new draws -- see Top2Base._runoff_electorate). Every non-genuine candidate is floored
    to the same (min genuine util - EPSILON) value -- a real, indifferent tie, not an arbitrarily
    broken one; see the comment inside apply_participation_friction below for why."""
    ncand = len(electorate[0])
    out = []
    for voter, genuine in zip(electorate, genuine_sets, strict=True):
        if len(genuine) == ncand:
            out.append(voter)
            continue
        floor = min(voter[c] for c in genuine)
        floored_utils = {c: floor - FRICTION_TIE_EPSILON for c in range(ncand) if c not in genuine}
        out.append(Voter(voter[c] if c in genuine else floored_utils[c] for c in range(ncand)))
    return Electorate(out)


def apply_participation_friction(perceived_electorate, true_electorate, awareness_alpha, fatigue_beta):
    """Build the electorate voters actually form ballots from, given which candidates
    each voter has genuinely evaluated (see the two mechanisms described above).

    At awareness_alpha >= 1.0 and fatigue_beta >= 1.0, returns (perceived_electorate, None, None)
    unchanged (no randomness drawn) -- same no-op property make_perceived_electorate has at rho=1.0.

    Returns (ballot_electorate, genuine_sets, aware_sets). Both genuine_sets and aware_sets are
    lists of sets (one per voter, parallel-indexed to ballot_electorate), or None when no
    friction was applied (the no-op case above).

    genuine_sets -- candidates a voter both recognized (awareness lottery) AND didn't fatigue out
    of (fatigue lottery); this is what ballot_electorate is actually floored against. Every
    method except Irv only reads the floored utility values in ballot_electorate and never looks
    at genuine_sets -- it exists specifically for Irv.honBallotFor's honest-ballot exhaustion.

    aware_sets -- candidates a voter recognized, IGNORING fatigue entirely (always a superset of
    genuine_sets for that same voter). Awareness/unfamiliarity is a persistent property of what a
    voter actually knows; fatigue is specific to the act of filling out THIS ballot (attention
    running out scanning a long candidate list) and has no reason to recur on a fresh, short
    ballot. This is exactly what Top2Base's runoff_coma path needs: a voter who recognized a
    candidate but got fatigued past them on the long primary ballot should still get to properly
    evaluate that candidate on the short 2-candidate runoff ballot, since runoff fatigue is
    (correctly, unconditionally) treated as impossible everywhere in this notebook's runoff code.
    """
    if awareness_alpha >= 1.0 and fatigue_beta >= 1.0:
        return perceived_electorate, None, None

    ncand = len(true_electorate[0])
    # Prominence is an independent per-election draw, NOT derived from true_electorate.socUtils.
    # An earlier version ranked candidates by their true social utility -- i.e. exactly the same
    # quantity that defines VSE's "best" reference. That makes the single guaranteed-known
    # candidate (prominence_rank 0) deterministically the socially optimal one, so at extreme
    # AWARENESS_ALPHA every voter's honest ballot converges on the true best candidate "for free" --
    # VSE shoots toward 100% at MAXIMUM friction, backwards from the intended direction, and not a
    # real finding: a real-world front-runner's fame doesn't guarantee they're the best choice for
    # the whole electorate. Decoupling prominence from true quality avoids that artifact; it costs
    # the "popular candidates tend to be more visible" intuition, which is a documented
    # simplification, not a load-bearing part of the mechanism.
    prominence_order = list(range(ncand))
    random.shuffle(prominence_order)
    prominence_rank = {c: r for r, c in enumerate(prominence_order)}  # 0 = most prominent

    genuine_sets = []
    aware_sets = []
    for voter in perceived_electorate:
        fatigue_order = list(range(ncand))
        random.shuffle(fatigue_order)  # this voter's own random ballot-processing order
        fatigue_position = {c: p for p, c in enumerate(fatigue_order)}  # 0 = processed first

        p_aware = {c: awareness_alpha ** prominence_rank[c] for c in range(ncand)}
        p_not_fatigued = {c: fatigue_beta ** fatigue_position[c] for c in range(ncand)}
        # Awareness and fatigue are drawn as two INDEPENDENT Bernoulli trials (rather than one
        # combined-probability trial against p_aware*p_not_fatigued, as before) so the
        # awareness-only outcome can be inspected on its own -- this doesn't change genuine_sets'
        # statistics at all (P(aware AND not_fatigued) is identical either way), it just also
        # produces aware_sets.
        aware = set()
        genuine = set()
        for c in range(ncand):
            if random.random() < p_aware[c]:
                aware.add(c)
                if random.random() < p_not_fatigued[c]:
                    genuine.add(c)
        favorite_known = max(aware, key=lambda c: voter[c])
        genuine.add(favorite_known)  # guarantee at least one genuinely-evaluated candidate per voter
        aware_sets.append(aware)
        genuine_sets.append(genuine)

    return _floor_to_genuine(perceived_electorate, genuine_sets), genuine_sets, aware_sets
