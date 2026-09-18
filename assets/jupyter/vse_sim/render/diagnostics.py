"""Tables for the runoff diagnostics: betrayal, Coma corruption, primary noise.

These read the accumulators folded into the main simulation runs rather than re-simulating
anything of their own -- see `engine.run_vse_simulation`'s `betrayal_targets` /
`coma_targets` / `primary_cost_targets` arguments.

From cells 134, 140, 153 and 159 of `vse_simulation.ipynb`."""

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Markdown, display

from .. import config as cfg
from . import context
from .significance import _classify_gap, _verdict_text
from .theme import FG_COLOR, MUTED_COLOR

from ..config import SWEEP_VALUES
from ..engine import reduce_primary_corruption_summary


__all__ = [
    "_at2_runoff_cost_table",
    "_primary_noise_cost_table",
    "_betrayal_table",
    "_betrayal_breakdown_table",
    "_corruption_by_param_table",
]


def _at2_runoff_cost_table(stats_by_key, key_header, key_fmt=str):
    """Same partition as _betrayal_breakdown_table above, but for Approval Top-2's own runoff
    variants instead of STAR: "true" (the honest reference) is Approval Top-2 (Clear-Eyed)'s own
    decision -- true_upset's sign already IS that decision, since Clear-Eyed's runoff electorate
    is the true electorate itself (see Top2Base._runoff_electorate). Groggy and Coma each get
    their own bad-flip/silent-lock-in split against that same reference; "Coma vs Groggy" is a
    single net cost, not bucketed -- there is no one "primary's raw leader" once both sides are
    corrupted relative to true, only relative to each other."""
    header = [key_header, "Groggy: bad flip (pp)", "Groggy: silent lock-in (pp)",
              "Coma: bad flip (pp)", "Coma: silent lock-in (pp)", "Coma vs Groggy (pp)"]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for key, stats in stats_by_key.items():
        lines.append("| " + " | ".join([
            key_fmt(key),
            f"{stats['groggy_bad_flip_vse_cost'] * 100:+.2f}",
            f"{stats['groggy_silent_lockin_vse_cost'] * 100:+.2f}",
            f"{stats['coma_bad_flip_vse_cost'] * 100:+.2f}",
            f"{stats['coma_silent_lockin_vse_cost'] * 100:+.2f}",
            f"{stats['coma_vs_groggy_vse_cost'] * 100:+.2f}",
        ]) + " |")
    display(Markdown("\n".join(lines)))


def _primary_noise_cost_table(stats_by_key, key_header, key_fmt=str):
    """How much Approval Top-2 (Groggy) loses from primary-stage noise alone: compares the real
    (noisy-primary) Groggy winner against a counterfactual Groggy winner between the finalists an
    honest primary would have picked instead, holding the runoff's own information level (Groggy)
    fixed. finalist_set_changed_rate is a companion diagnostic, not part of the cost sum: how
    often primary noise alone swapped who even reached the runoff."""
    header = [key_header, "Primary-noise VSE cost (pp)", "Finalist set changed"]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for key, stats in stats_by_key.items():
        lines.append("| " + " | ".join([
            key_fmt(key),
            f"{stats['primary_noise_vse_cost'] * 100:+.2f}",
            f"{stats['finalist_set_changed_rate'] * 100:.1f}%",
        ]) + " |")
    display(Markdown("\n".join(lines)))


def _betrayal_table(stats_by_key, key_header, star_vse_lookup, at2_vse_lookup, key_fmt=str):
    """star_vse_lookup(key) -> STAR's own already-computed honest-ballot VSE (a 0..1 fraction) at
    this scenario/epistemic_rho value, pulled from Sections 13/16 data -- not recomputed here. The
    "honest/delayed-perfect runoff" column is derived as actual + population_vse_cost, so the two
    VSE columns are guaranteed to differ by exactly the "VSE gap" column.

    at2_vse_lookup(key) -> "Approval Top-2 (Clear-Eyed)"'s already-computed honest-ballot
    VSE (a 0..1 fraction) at the SAME scenario/epistemic_rho value, also pulled from Sections 13/16
    data (COMPARE_LABELS/METHODS_NO_COMA already include it -- no new simulation). Placed next
    to STAR's own two VSE columns so a coarse (Approval) vs. fine-grained (0..5 Score) noisy
    primary ballot can be compared directly once BOTH have a perfect delayed runoff available to
    correct their pick -- STAR's "honest/delayed-perfect" column IS exactly that comparison for
    the Score primary, restricted to the decisive runoff pairs."""
    header = [key_header, "Betrayal rate", "Voter corruption rate",
              "VSE (STAR's actual runoff)", "VSE (honest/delayed-perfect runoff)",
              "VSE (AT2 Clear-Eyed runoff)"]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for key, stats in stats_by_key.items():
        n_dec = stats["n_decisive"]
        actual_vse = star_vse_lookup(key) * 100
        gap = stats["population_vse_cost"] * 100 if n_dec else 0.0
        honest_vse = actual_vse + gap
        at2_vse = at2_vse_lookup(key) * 100
        at2_star_gap = at2_vse - actual_vse
        lines.append("| " + " | ".join([
            key_fmt(key),
            f"{stats['betrayal_rate'] * 100:.1f}%" if n_dec else "n/a",
            f"{stats['voter_corruption_rate'] * 100:.2f}%",
            f"{actual_vse:.1f}%",
            f"{honest_vse:.1f}% ({gap:+.1f} pts over actual)" if n_dec else "n/a",
            #f"{gap:+.1f} pts" if n_dec else "n/a",
            f"{at2_vse:.1f}% ({at2_star_gap:+.1f} pts over STAR)" if n_dec else "n/a",
        ]) + " |")
    display(Markdown("\n".join(lines)))


def _betrayal_breakdown_table(stats_by_key, key_header, key_fmt=str):
    """Exhaustive partition of every election into: aligned (no flip, honestly correct), bad flip
    (flip, honestly wrong), silent lock-in (no flip, honestly WRONG -- "garbage in, garbage out"),
    good flip (flip, honestly correct), and other (a small residual: exact noisy ties, plus
    elections with no clear honest preference between the two finalists). The five share columns
    sum to 100% per row. The two cost columns sum to the same population_vse_cost already shown
    in the betrayal table earlier in this section."""
    header = [key_header, "Aligned", "Bad flip (betrayal)", "Silent lock-in (betrayal)",
              "Good flip", "Other", "VSE cost: bad flips (pp)", "VSE cost: silent lock-in (pp)"]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for key, stats in stats_by_key.items():
        lines.append("| " + " | ".join([
            key_fmt(key),
            f"{stats['aligned_share'] * 100:.1f}%",
            f"{stats['bad_flip_share'] * 100:.1f}%",
            f"{stats['silent_lockin_share'] * 100:.1f}%",
            f"{stats['good_flip_share'] * 100:.1f}%",
            f"{stats['other_share'] * 100:.1f}%",
            f"{stats['bad_flip_vse_cost'] * 100:+.2f}",
            f"{stats['silent_lockin_vse_cost'] * 100:+.2f}",
        ]) + " |")
    display(Markdown("\n".join(lines)))


def _corruption_by_param_table(sink_by_value, param_name):
    lines = [
        f"#### Primary-vote corruption by `{param_name}`",
        "",
        f"| `{param_name}` | Aligned | Awareness-caused | Noise-caused | Total corruption |",
        "|---|---|---|---|---|",
    ]
    for value in SWEEP_VALUES:
        r = reduce_primary_corruption_summary(sink_by_value[value])
        lines.append(
            f"| {value:.2f} | {r['aligned_rate']*100:.1f}% | {r['awareness_caused_rate']*100:.1f}% | "
            f"{r['noise_caused_rate']*100:.1f}% | {r['corruption_rate']*100:.1f}% |"
        )
    display(Markdown("\n".join(lines)))
