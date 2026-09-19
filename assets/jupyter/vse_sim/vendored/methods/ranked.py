"""Copied, with one small addition, from the `vse_sim` Python package at
https://github.com/electionscience/vse-sim. Extracted verbatim from section 1 of
`vse_simulation.ipynb` (cell 14); see that notebook for the original prose.
"""

from ..core import Method, rememberBallot


# ---- methods/ranked.py ----

class RankedMethod(Method):
    """Base class for methods that use candidate-aligned rank vectors.
    Larger ballot values represent stronger preferences."""

    @staticmethod
    def fillPrefOrder(voter, ballot, whichCands=None, lowSlot=0, nSlots=None, remainderScore=None):
        """Fill ballot with candidates ordered by decreasing utility."""
        venum = list(enumerate(voter))
        if whichCands:
            venum = [venum[c] for c in whichCands]
        prefOrder = sorted(venum, key=lambda x: -x[1])
        RankedMethod.fillCands(ballot, prefOrder, lowSlot, nSlots, remainderScore)

    @staticmethod
    def fillCands(ballot, whichCands, lowSlot=0, nSlots=None, remainderScore=None):
        """Assign descending ranks to candidate tuples in whichCands.

        Candidates with EXACTLY EQUAL values (whichCands is presorted by fillPrefOrder, so
        ties are always adjacent) get the SAME rank, not distinct sequential ones -- needed
        so a genuine tie in the input (e.g. participation friction's floored/unaware
        candidates, which now all share one value -- see apply_participation_friction) is
        preserved as a real tie in the ballot for Schulze's sign()-based pairwise comparison
        to read as indifference, rather than being silently broken into an arbitrary strict
        order by whichCands's position. Ranks are consumed by GROUP SIZE, not by count, so
        the ranking stays consistent (e.g. a 3-way tie at the bottom occupies 3 slots' worth
        of "room" even though every tied candidate gets the same rank number). A tie that
        straddles the nSlots/remainderScore boundary is not specially handled -- rare enough
        (only possible when nSlots truncates a ranking, e.g. strategic ballots) not to be
        worth the extra complexity here.
        """
        if nSlots is None:
            nSlots = len(whichCands)
        cur = lowSlot + nSlots - 1
        i = 0
        while i < nSlots:
            j = i
            while j + 1 < nSlots and whichCands[j + 1][1] == whichCands[i][1]:
                j += 1
            for k in range(i, j + 1):
                ballot[whichCands[k][0]] = cur
            cur -= (j - i + 1)
            i = j + 1
        if remainderScore is not None:
            for candidate, *_ in whichCands[nSlots:]:
                ballot[candidate] = remainderScore

    @staticmethod
    @rememberBallot
    def honBallot(cls, utils):
        """Return a complete rank vector ordered by utility."""
        ballot = [0] * len(utils)
        cls.fillPrefOrder(utils, ballot)
        return ballot

    @classmethod
    def fillStratBallot(cls, voter, polls, places, n, stratGap, ballot,
                        frontId, frontResult, targId, targResult):
        """Mutate ballot with the default strategy for ranked methods."""
        nRanks = min(cls.nRanks, n)
        if stratGap <= 0:
            ballot[frontId], ballot[targId] = (nRanks - 1), 0
        else:
            ballot[frontId], ballot[targId] = 0, (nRanks - 1)
        nRanks -= 2
        if nRanks > 0:
            cls.fillCands(ballot, places[2:][::-1], lowSlot=1, nSlots=nRanks, remainderScore=0)


RatedMethod = RankedMethod
