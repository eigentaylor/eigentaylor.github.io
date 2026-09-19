"""Copied, with one small addition, from the `vse_sim` Python package at
https://github.com/electionscience/vse-sim. Extracted verbatim from section 1 of
`vse_simulation.ipynb` (cell 17); see that notebook for the original prose.
"""

from ..core import CandidateWithCount, Method, rememberBallot


# ---- methods/irv.py ----
from collections.abc import Set as _Set
from operator import index as _index


def build_preference_schedule(ballots):
    """Count identical candidate rankings."""
    preferences = {}
    for ballot in ballots:
        ranking = tuple(ballot)
        preferences[ranking] = preferences.get(ranking, 0) + 1
    return preferences


def eliminate_candidate(preferences, candidate_id):
    """Return a schedule with the indexed candidate removed from every ranking."""
    candidate_id = _index(candidate_id)
    updated_preferences = {}
    for ranking, votes in preferences.items():
        updated_ranking = tuple(candidate for candidate in ranking if candidate != candidate_id)
        if updated_ranking:
            updated_preferences[updated_ranking] = (
                updated_preferences.get(updated_ranking, 0) + votes
            )
    return updated_preferences


def candidate_votes(preference_schedule, remaining_candidates=None):
    """Return active candidates ordered from most to fewest first choices.

    remaining_candidates -- the set of candidate indices still in the race (not yet
    eliminated), if known: any of THOSE candidates absent from EVERY ranking entirely (not
    just absent as a first choice) still gets a 0-vote placeholder. This matters once
    ballots can be genuinely partial (see Irv.honBallotFor's participation-friction
    exhaustion below): a candidate every remaining voter happened to leave off their ballot
    would otherwise never surface as a trackable candidate at all, and runIrv's fixed
    ncand-round elimination loop would run out of candidates to eliminate partway through.
    Deliberately scoped to remaining_candidates rather than range(ncand): a candidate
    already eliminated in an earlier round is correctly absent from every ranking too (
    eliminate_candidate stripped it out), and must NOT be resurrected as a fresh 0-vote
    placeholder here, or runIrv would "eliminate" the same already-gone candidate over and
    over. A no-op when every ranking already covers every candidate (the ordinary,
    no-friction case) or remaining_candidates isn't passed.
    """
    candidates = {}
    for ranking, votes in preference_schedule.items():
        candidate = ranking[0]
        if candidate in candidates:
            candidates[candidate].votes += votes
        else:
            candidates[candidate] = CandidateWithCount(candidate, votes)

    # VSE needs a complete ranking even for candidates with no active first choices.
    alternates = []
    tracked_alternates = set()
    for ranking in preference_schedule:
        for alternate in ranking[1:]:
            if alternate not in candidates and alternate not in tracked_alternates:
                alternates.append(CandidateWithCount(alternate, 0))
                tracked_alternates.add(alternate)
    if remaining_candidates is not None:
        for c in remaining_candidates:
            if c not in candidates and c not in tracked_alternates:
                alternates.append(CandidateWithCount(c, 0))
                tracked_alternates.add(c)

    active = sorted(
        candidates.values(),
        key=lambda candidate: (candidate.votes, candidate.candidate),
        reverse=True,
    )
    return active + alternates


def least_candidate(vote_ranking, keep=None):
    """Return the lowest-ranked candidate not in the set-like keep."""
    if keep is None:
        keep = frozenset()
    elif not isinstance(keep, _Set):
        raise TypeError("keep must be a set-like collection")
    for candidate in reversed(vote_ranking):
        if candidate.candidate not in keep:
            return candidate
    return None


def rank_vector_to_preference(ballot):
    """Return candidate IDs in descending preference order from a rank vector.

    Skips any candidate still at the -1 "unranked" sentinel (see Irv.honBallotFor below) --
    a no-op when every candidate got a real rank, as in the ordinary complete-ranking case.
    """
    return sorted((c for c in range(len(ballot)) if ballot[c] != -1),
                  key=lambda candidate: ballot[candidate], reverse=True)


def finish_order_to_results(finish_order):
    """Convert winner-first finish order to high-is-better candidate scores."""
    results = [-1] * len(finish_order)
    for score, candidate in enumerate(reversed(finish_order)):
        results[candidate] = score
    return results


class Irv(Method):
    """Instant-Runoff Voting over complete ranked ballots. Ballots are
    candidate-aligned rank vectors (larger = stronger preference).
    Tabulation repeatedly eliminates the candidate with the fewest active
    first preferences."""

    stratTargetFor = Method.stratTarget3

    buildPreferenceSchedule = staticmethod(build_preference_schedule)
    eliminateCandidate = staticmethod(eliminate_candidate)
    candidateVotes = staticmethod(candidate_votes)
    getLeast = staticmethod(least_candidate)
    rankVectorToPreference = staticmethod(rank_vector_to_preference)
    finishOrderToResults = staticmethod(finish_order_to_results)

    def runIrv(self, remaining, ncand):
        results = [-1] * ncand
        still_in = set(range(ncand))
        for i in range(ncand):
            votes = self.candidateVotes(remaining, still_in)
            toEliminate = self.getLeast(votes)
            results[ncand - i - 1] = toEliminate.candidate
            still_in.discard(toEliminate.candidate)
            remaining = self.eliminateCandidate(remaining, toEliminate.candidate)
        return results

    def results(self, ballots, **kwargs):
        if type(ballots) is not list:
            ballots = list(ballots)
        rankings = [self.rankVectorToPreference(ballot) for ballot in ballots]
        finishOrder = self.runIrv(self.buildPreferenceSchedule(rankings), len(ballots[0]))
        return self.finishOrderToResults(finishOrder)

    @staticmethod  # cls is provided explicitly, not through binding
    @rememberBallot
    def honBallot(cls, voter):
        """Takes utilities and returns an honest ballot (a full ranking)."""
        ballot = [-1] * len(voter)
        order = sorted(enumerate(voter), key=lambda x: x[1])
        for i, cand in enumerate(order):
            ballot[cand[0]] = i
        return ballot

    def honBallotFor(self, voters):
        """Override: when participation friction produced per-voter genuine-evaluation sets
        (self._genuine_sets, stashed by Method.resultsTable/vseOn -- see apply_participation_
        friction and Method above), rank ONLY each voter's genuinely-evaluated candidates;
        every other candidate is left at the ballot's -1 "unranked" sentinel rather than being
        floored-and-ranked. That's the real ballot-exhaustion analogue of leaving a bubble
        blank: eliminate_candidate already drops a ranking once it empties out, so a voter
        whose every ranked candidate gets eliminated simply stops transferring a vote, instead
        of falling through to a candidate they never evaluated. Falls back to the ordinary
        complete-ranking honBallot when friction wasn't applied (self._genuine_sets is None) --
        i.e. this is a no-op in every case except IRV honest ballots under participation
        friction. Scoped to honest ballots only: fillStratBallot is untouched, and strategic
        IRV ballots keep ranking every candidate (using the shared-epsilon floored utilities
        from apply_participation_friction, same as Plurality/Schulze's strategic ballots).
        """
        genuine_sets = getattr(self, "_genuine_sets", None)
        if genuine_sets is None:
            return self.honBallot
        genuine_by_voter = {id(v): g for v, g in zip(voters, genuine_sets, strict=True)}

        @staticmethod  # cls is provided explicitly, not through binding
        @rememberBallot
        def honBallot(cls, voter):
            genuine = genuine_by_voter[id(voter)]
            ballot = [-1] * len(voter)
            order = sorted(genuine, key=lambda c: voter[c])
            for i, cand in enumerate(order):
                ballot[cand] = i
            return ballot

        return honBallot

    @classmethod
    def fillStratBallot(cls, voter, polls, places, n, stratGap, ballot,
                        frontId, frontResult, targId, targResult):
        i = n - 1
        winnerQ = voter[frontId]
        targQ = voter[targId]
        placesToFill = list(range(n - 1, 0, -1))
        if targQ > winnerQ:
            ballot[targId] = i
            i -= 1
            del placesToFill[-2]
        for j in placesToFill:
            nextLoser, loserScore = places[j]  # all but winner, low to high
            if voter[nextLoser] > winnerQ:
                ballot[nextLoser] = i
                i -= 1
        ballot[frontId] = i
        i -= 1
        for j in placesToFill:
            nextLoser, loserScore = places[j]
            if voter[nextLoser] <= winnerQ:
                ballot[nextLoser] = i
                i -= 1
        assert i == -1
