"""Four ways to collapse multi-scenario performance into one ranking (cell 103).

They are kept separate on purpose: a mean hides a method that collapses at one scenario, a
worst case ignores everything else, regret normalizes away scenarios that are simply harder
for everyone, and average rank throws away magnitude. A method that wins all four is
robust in a way no single one of them can establish."""

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Markdown, display

from .. import config as cfg
from . import context
from .significance import _classify_gap, _verdict_text
from .theme import FG_COLOR, MUTED_COLOR


__all__ = [
    "compute_robustness_rankings",
    "display_rankings",
]


def compute_robustness_rankings(scores_by_method):
    """scores_by_method: {label: [(mean, ci), (mean, ci), ...]} -- one (mean, ci) per axis
    point (a scenario, or a chooser/strategy level), same order/count for every method.

    Four methodologically distinct ways to collapse multi-point performance into one ranking:

    1. Mean across axis -- simplest, most transparent. Can hide a method that's great at one
       axis point and collapses at another, if the average still looks fine.
    2. Worst-case, using each axis point's 95% CI LOWER BOUND (not the raw point estimate) --
       the classic Rawlsian/robust-optimization "floor" framing. Using the lower bound rather
       than the raw min avoids the "min of several noisy estimates is biased downward" trap:
       whichever axis point got unlucky sampling would otherwise look artificially worse.
    3. Average regret vs. the best-performing method AT THAT SAME axis point -- normalizes
       away the fact that some axis points (e.g. Heavy friction) have a lower ceiling for
       EVERYONE, so raw VSE comparisons across axis points conflate "hard scenario" with
       "bad method." Lower is better (0 = always tied the best available option).
    4. Average rank across axis points (Borda-style) -- robust to VSE scores compressing
       together at harder axis points (a real effect under friction), since it only uses
       *ordering* within each axis point, not magnitude. Lower is better (1 = always best).
    """
    labels = list(scores_by_method)
    n_axis = len(next(iter(scores_by_method.values())))
    assert all(len(v) == n_axis for v in scores_by_method.values()), "mismatched axis lengths"

    mean_across = {label: sum(m for m, _ in vals) / n_axis for label, vals in scores_by_method.items()}

    worst_case = {label: min(m - ci for m, ci in vals) for label, vals in scores_by_method.items()}

    best_per_axis = [max(scores_by_method[l][j][0] for l in labels) for j in range(n_axis)]
    avg_regret = {
        label: sum(best_per_axis[j] - scores_by_method[label][j][0] for j in range(n_axis)) / n_axis
        for label in labels
    }

    avg_rank = {label: 0.0 for label in labels}
    for j in range(n_axis):
        order = sorted(labels, key=lambda l: -scores_by_method[l][j][0])
        for rank, label in enumerate(order, start=1):
            avg_rank[label] += rank
    avg_rank = {label: total / n_axis for label, total in avg_rank.items()}

    return {
        "1. Mean VSE across axis (higher better)": sorted(mean_across.items(), key=lambda x: -x[1]),
        "2. Worst-case VSE, CI lower bound (higher better)": sorted(worst_case.items(), key=lambda x: -x[1]),
        "3. Avg. regret vs. best-at-that-point (lower better)": sorted(avg_regret.items(), key=lambda x: x[1]),
        "4. Avg. rank across axis (lower better)": sorted(avg_rank.items(), key=lambda x: x[1]),
    }


def display_rankings(title, rankings, as_percent=True):
    lines = [f"### {title}", ""]
    for metric_name, ranked in rankings.items():
        lines.append(f"**{metric_name}**")
        lines.append("")
        lines.append("| Rank | Method | Score |")
        lines.append("|---|---|---|")
        for i, (label, score) in enumerate(ranked, start=1):
            score_str = f"{score * 100:.1f}%" if not metric_name.startswith("4.") else f"{score:.2f}"
            lines.append(f"| {i} | {label} | {score_str} |")
        lines.append("")
    display(Markdown("\n".join(lines)))
