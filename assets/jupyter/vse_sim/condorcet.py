"""Ground-truth Condorcet-winner detection (section 7 of `vse_simulation.ipynb`, cell 36).

Computed from the TRUE electorate's utilities, independent of any method, chooser,
epistemic noise, or participation friction.
"""

from numpy import sign as _sign7


from numpy import sign as _sign7


def true_condorcet_winner(true_electorate):
    """Ground-truth Condorcet-winner detection against the TRUE electorate -- independent of
    method, chooser, epistemic noise, and participation friction. A true CW strictly beats
    EVERY other candidate on raw vote count; an exact pairwise tie (cmat[i][j] == 0) counts as
    neither candidate winning that pairing (unlike Schulze.results's own numWins, whose i<j
    tiebreak exists only to force a total order for picking a winner, not to decide whether one
    exists). Returns the winning candidate's index, or None if no such candidate exists this
    election.
    """
    n = len(true_electorate[0])
    cmat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                cmat[i][j] = sum(_sign7(voter[i] - voter[j]) for voter in true_electorate)
    for i in range(n):
        if all(cmat[i][j] > 0 for j in range(n) if j != i):
            return i
    return None
