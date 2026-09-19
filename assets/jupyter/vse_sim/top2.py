"""Top-2 hybrid methods (section 3 of `vse_simulation.ipynb`, cell 25).

A primary tally picks two finalists, then a runoff decides between them under its
own information assumptions. Original to this project, not part of vse-sim.
"""

import random

from numpy import mean

from .friction import _floor_to_genuine, apply_participation_friction
from .noise import make_perceived_electorate
from .vendored.core import Method, rememberBallot
from .vendored.methods.ranked import RankedMethod
from .vendored.methods.score import Score
from .vendored.voter_models import Electorate, Voter


def _top2_runoff_suffix(runoff_rho, runoff_awareness_alpha):
    """__str__ suffix shared by the Top2Base subclasses below -- describes the
    runoff's information assumptions in one short, unambiguous label fragment."""
    if runoff_rho is None:
        return ""
    suffix = "ClearEyed" if runoff_rho >= 1.0 else f"RunoffT{runoff_rho:.2f}"
    if runoff_awareness_alpha < 1.0:
        suffix += f"Aware{runoff_awareness_alpha:.2f}"
    return suffix


class Top2Base(Method):
    """Shared plumbing for 'primary method picks the top-2, a pairwise utility
    comparison between them decides the winner' hybrids.

    runoff_rho=None (default): the pairwise runoff check uses the same epistemic-noise level as
    the primary ballots (self._perceived_voters, stashed by resultsTable/vseOn above -- the
    primary's electorate BEFORE participation friction was applied). runoff_rho=<a float>: the
    runoff check uses a FRESH perceived electorate drawn from the *true* electorate
    (self._scoring_voters) at that knowledge level -- NOT the primary's own noise, and not
    compounded on top of it, since rho is defined as correlation with true utility (see
    make_perceived_electorate above). runoff_rho=1.0 draws the true electorate itself (a
    documented no-op of make_perceived_electorate), modeling the idea that a two-candidate
    choice is easy enough that voters can get it right even if they were poorly informed
    during the primary; runoff_rho strictly between the primary's own rho and 1.0 models a runoff
    where voters have partially, but not perfectly, caught up.

    runoff_awareness_alpha=1.0 (default, meaningful regardless of runoff_rho): ballot fatigue is
    pinned at 1.0 (no fatigue) for the runoff unconditionally -- a 2-candidate choice isn't a
    long ballot to get tired scanning through, regardless of this parameter. Awareness is a
    separate, real assumption worth testing explicitly (concentrated runoff media coverage
    plausibly restores it, but that's a modeling choice, not a certainty): runoff_awareness_alpha=
    1.0 (the default, including when runoff_rho=None) assumes voters become aware of both
    finalists by runoff time, so the primary's own participation friction is NOT carried into
    the runoff by default; passing the primary's own awareness_alpha instead assumes awareness
    carries over unchanged.

    runoff_coma=True (default False, ignores runoff_rho/runoff_awareness_alpha when set): models a
    voter who gets zero new information or exposure between the primary and the runoff -- same
    epistemic noise level AND same awareness as the primary -- but still casts a genuine runoff
    ballot, unlike STAR's automatic same-ballot runoff. Reuses the primary's own REALIZED
    awareness outcome directly (self._aware_sets, stashed by resultsTable/vseOn -- the set of
    candidates this voter was actually aware of in the primary, independent of whether they ALSO
    got fatigued out of rating one) rather than redrawing awareness at the primary's rate: a
    voter aware of a finalist in the primary but fatigued past it on the long primary ballot
    still gets to vote for it here, since fatigue is ballot-instance-specific and never re-enters
    the runoff (matching every other runoff_awareness_alpha case below, which also unconditionally
    pins fatigue to 1.0). A voter never aware of a finalist at all in the primary stays unaware.
    If both finalists are unknown to a voter, they abstain (tied, contributing to neither side of
    the pairwise comparison below).

    runoff_kappa=None (default, ignores runoff_rho/runoff_awareness_alpha when set, like
    runoff_coma -- mutually exclusive with runoff_coma, enforced below): generalizes Coma into a
    genuine "chance to learn" sweep. A voter aware of a candidate in the primary (self._aware_sets)
    stays aware -- no regression, no re-rolling what's already known. A voter NOT already aware
    of a given candidate gets one fresh, independent Bernoulli(runoff_kappa) roll for THAT
    candidate to become aware of it by runoff day (concentrated runoff media coverage, etc.).
    runoff_kappa=0.0 therefore reduces to EXACTLY the runoff_coma=True result (no roll can ever
    succeed); runoff_kappa=1.0 reduces to EXACTLY the default Groggy result (every roll is
    certain to succeed, so every voter ends up aware of everyone) -- both exact boundary matches,
    not approximations, since the same _floor_to_genuine helper does the work either way. Rolls
    happen over every candidate a voter isn't already aware of (not just the two eventual
    finalists, since this method has no way to know which two those are yet) -- harmless, since
    only the finalists' resulting values are ever read by results() below.
    """

    def __init__(self, runoff_rho=None, runoff_awareness_alpha=1.0, runoff_coma=False, runoff_kappa=None):
        super().__init__()
        self.runoff_rho = runoff_rho
        self.runoff_awareness_alpha = runoff_awareness_alpha
        self.runoff_coma = runoff_coma
        self.runoff_kappa = runoff_kappa
        if runoff_coma and runoff_kappa is not None:
            raise ValueError("runoff_coma and runoff_kappa are mutually exclusive")
        self._runoff_electorate_cache = None
        self._runoff_noise = None  # optional: set directly by a caller pairing noise across
        # a runoff_rho sweep (see Section 21 sweep_runoff_rho) -- None means draw fresh, same
        # as before this existed.

    def resultsFor(self, voters, chooser, tally=None, **kwargs):
        if voters is not getattr(self, "_current_voters", None):
            self._runoff_electorate_cache = None  # new election -- invalidate the cache below
        self._current_voters = voters  # electorate ballots were generated from (perceived, usually)
        return super().resultsFor(voters, chooser, tally, **kwargs)

    def _runoff_electorate(self):
        """The electorate used ONLY for the pairwise runoff check -- see runoff_rho,
        runoff_awareness_alpha, runoff_coma, and runoff_kappa above. Cached per election
        (invalidated in resultsFor whenever `voters` changes identity): multiResults calls
        resultsFor -> results() 7 times per method per election (honest, strategic,
        one-sided-strategic, and 4 baseRuns Prob/OssChooser variants), and without caching this
        redraws fresh on every one of those 7 calls even though they're all the same election's
        same runoff -- wasteful, and arguably wrong: the runoff's information state shouldn't
        plausibly differ across hypothetical strategic-behavior scenarios. For runoff_kappa
        specifically, caching isn't just a performance nicety -- without it, each of those 7
        calls would redraw different "who learned" outcomes for the SAME election, which would
        be actively wrong, not just slow.

        runoff_coma=True is handled first, separately from the runoff_rho axis below -- it
        always reuses the primary's own epistemic-noise level (self._perceived_voters) AND the
        primary's own realized awareness outcome (self._aware_sets), floored via
        _floor_to_genuine with no new randomness drawn -- regardless of runoff_rho/
        runoff_awareness_alpha.

        runoff_kappa is handled next, also independent of the runoff_rho axis below -- reuses
        self._aware_sets (the primary's own realized awareness outcome, no new prominence draw)
        and layers one independent "did they learn this new candidate" roll on top, per
        not-yet-aware candidate. See Top2Base's class docstring above for the exact-boundary-
        match property at 0.0/1.0.

        runoff_rho=None reuses the primary's own epistemic-noise level (self._perceived_voters --
        the primary's ballots BEFORE participation friction was applied, not self._current_voters,
        which has friction already baked in) rather than the true electorate at some fresh rho --
        then, exactly like the runoff_rho=<float> branch, optionally reapplies friction based on
        runoff_awareness_alpha. This is what lets runoff_awareness_alpha=1.0 (the default) mean "same
        noise as the primary, but full runoff awareness" instead of silently inheriting whatever
        friction the primary happened to have."""
        if self.runoff_coma:
            if self._runoff_electorate_cache is not None:
                return self._runoff_electorate_cache
            base = getattr(self, "_perceived_voters", None)
            if base is None:
                base = self._current_voters
            aware_sets = getattr(self, "_aware_sets", None)
            result = base if aware_sets is None else _floor_to_genuine(base, aware_sets)
            self._runoff_electorate_cache = result
            return result
        if self.runoff_kappa is not None:
            if self._runoff_electorate_cache is not None:
                return self._runoff_electorate_cache
            base = getattr(self, "_perceived_voters", None)
            if base is None:
                base = self._current_voters
            aware_sets = getattr(self, "_aware_sets", None)
            if aware_sets is None:
                # Unlike runoff_coma, a swept runoff_kappa silently degrading to the p=1.0/
                # Groggy answer for every point is almost never intentional (it means whatever
                # loop is driving this forgot to pass aware_sets=aware_sets into resultsTable) --
                # fail loudly instead of quietly producing a flat, wrong sweep.
                raise RuntimeError(
                    "runoff_kappa is set but self._aware_sets is None -- resultsTable(...) "
                    "wasn't given aware_sets=aware_sets. Continuing silently would make every "
                    "runoff_kappa value in a sweep produce the same (Groggy) result."
                )
            ncand = len(base[0])
            runoff_aware_sets = []
            for aware in aware_sets:
                new_aware = set(aware)
                for c in range(ncand):
                    if c not in aware and random.random() < self.runoff_kappa:
                        new_aware.add(c)
                runoff_aware_sets.append(new_aware)
            result = _floor_to_genuine(base, runoff_aware_sets)
            self._runoff_electorate_cache = result
            return result
        true_electorate = getattr(self, "_scoring_voters", None)
        needs_friction = self.runoff_awareness_alpha < 1.0 and true_electorate is not None
        if self.runoff_rho is None and not needs_friction:
            # Cheap fast path -- no computation happens, so nothing worth caching, and it must
            # stay uncached: callers that manipulate _current_voters directly without ever
            # going through resultsFor (e.g. the hand-built sanity-check cells below, which
            # reuse one instance across multiple different hand-built electorates) never
            # invalidate _runoff_electorate_cache, so caching here would silently return a
            # stale electorate from a PREVIOUS call.
            base = getattr(self, "_perceived_voters", None)
            return base if base is not None else self._current_voters
        if self._runoff_electorate_cache is not None:
            return self._runoff_electorate_cache
        if self.runoff_rho is None:
            base = getattr(self, "_perceived_voters", None)
            if base is None:
                base = self._current_voters
        elif true_electorate is not None:
            base = make_perceived_electorate(true_electorate, self.runoff_rho, noise=self._runoff_noise)
        else:
            return self._current_voters
        if needs_friction:
            base, _, _ = apply_participation_friction(base, true_electorate, self.runoff_awareness_alpha, 1.0)  # runoff electorate never feeds Irv, so genuine_sets/aware_sets are discarded here
        self._runoff_electorate_cache = base
        return base

    def results(self, ballots, **kwargs):
        if type(ballots) is not list:
            ballots = list(ballots)
        primary = list(map(self.candScore, zip(*ballots, strict=False)))
        ranked = sorted(range(len(primary)), key=lambda i: primary[i])
        runnerUp, top = ranked[-2], ranked[-1]
        electorate = self._runoff_electorate()
        upset = sum(_sign4(voter[runnerUp] - voter[top]) for voter in electorate)
        results = list(primary)
        if upset > 0:
            results[runnerUp] = results[top] + 0.01
        return results


from numpy import sign as _sign4


class PluralityTop2(Top2Base, RankedMethod):
    """Plurality primary (most first-choice votes) among all candidates, top-2
    advance, pairwise utility comparison decides the winner."""

    candScore = staticmethod(mean)
    stratTargetFor = Method.stratTarget3

    def __str__(self):
        if self.runoff_coma:
            return "PluralityTop2Coma"
        return "PluralityTop2" + _top2_runoff_suffix(self.runoff_rho, self.runoff_awareness_alpha)

    @staticmethod  # cls is provided explicitly, not through binding
    @rememberBallot
    def honBallot(cls, utils):
        """Honest primary ballot: vote for your true favorite among all candidates."""
        ballot = [0] * len(utils)
        cls.fillPrefOrder(utils, ballot, nSlots=1, lowSlot=1, remainderScore=0)
        return ballot

    @classmethod
    def fillStratBallot(cls, voter, polls, places, n, stratGap, ballot,
                        frontId, frontResult, targId, targResult):
        """Strategic primary ballot: vote for your favorite among the current top 3 in the polls."""
        top3 = [c for c, _ in places[:3]]
        cls.fillPrefOrder(voter, ballot, whichCands=top3, nSlots=1, lowSlot=1, remainderScore=0)


class ApprovalTop2(Top2Base, Score(1, True)):
    """Approval primary (most approvals) among all candidates, top-2 advance,
    pairwise utility comparison decides the winner. honBallot/fillStratBallot/
    candScore are unchanged from Score(1) -- only stratTargetFor differs."""

    stratTargetFor = Method.stratTarget3

    def __str__(self):
        if self.runoff_coma:
            return "ApprovalTop2Coma"
        return "ApprovalTop2" + _top2_runoff_suffix(self.runoff_rho, self.runoff_awareness_alpha)


def ScoreTop2(topRank=10, **kwargs):
    """Score(topRank) primary among all candidates, top-2 advance, pairwise utility
    comparison decides the winner -- the Top2Base analogue of Srv/STAR (Section 1.6),
    using a runoff drawn from a separate (optionally clear-eyed) electorate instead of
    STAR's same-ballot runoff. honBallot/fillStratBallot/candScore come from Score(topRank);
    only stratTargetFor/__str__ differ, same convention as ApprovalTop2/PluralityTop2 above."""
    score0to = Score(topRank, True)

    class ScoreTop2Cls(Top2Base, score0to):
        stratTargetFor = Method.stratTarget3

        def __str__(self):
            if self.runoff_coma:
                return "ScoreTop2" + str(self.topRank) + "Coma"
            return "ScoreTop2" + str(self.topRank) + _top2_runoff_suffix(self.runoff_rho, self.runoff_awareness_alpha)

    return ScoreTop2Cls(**kwargs)
