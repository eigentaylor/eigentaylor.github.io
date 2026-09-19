"""How many more elections would it actually take? (cell 215 of `vse_simulation.ipynb`)

Section 29 turns every inconclusive comparison into a number: given the interval we have,
how many elections would be needed to resolve it. Because a confidence half-width scales
as n^(-1/2), the answer is

    n_required = n_current * (ci_current / ci_target)^2

which is why chasing a gap four times narrower costs sixteen times the compute -- and why
some comparisons in this project are reported as unresolved rather than chased."""

from IPython.display import Markdown, display

from ..config import GAP_THRESHOLD_PP, JOINT_NITER, NCAND_SWEEP_NITER, RUNOFF_SWEEP_NITER
from .significance import TAXONOMY_LABELS, _classify_gap


__all__ = [
    "_NITER_KNOB_KEYWORDS",
    "_DEFAULT_NITER_KNOB",
    "_niter_knob_for",
    "_required_n",
    "_next_tier_ci_target",
    "_fmt_n",
]


_NITER_KNOB_KEYWORDS = [
    ("kappa threshold", "RUNOFF_SWEEP_NITER", RUNOFF_SWEEP_NITER),
    ("candidate count", "NCAND_SWEEP_NITER", NCAND_SWEEP_NITER),
]
_DEFAULT_NITER_KNOB = ("JOINT_NITER", JOINT_NITER)


def _niter_knob_for(table_title):
    for keyword, name, value in _NITER_KNOB_KEYWORDS:
        if keyword in table_title:
            return name, value
    return _DEFAULT_NITER_KNOB


def _required_n(n_current, ci_current, ci_target):
    if ci_target <= 0 or ci_current <= 0:
        return float("inf")
    return n_current * (ci_current / ci_target) ** 2


def _next_tier_ci_target(bucket, gap):
    if bucket == "INCONCLUSIVE":
        return abs(gap)
    if bucket == "AMBIGUOUS_EDGE":
        return abs(abs(gap) - GAP_THRESHOLD_PP)
    return None


def _fmt_n(n_for, n_current):
    if n_for <= n_current:
        return "already there"
    return "very large" if n_for == float("inf") else f"{n_for:,.0f}"
