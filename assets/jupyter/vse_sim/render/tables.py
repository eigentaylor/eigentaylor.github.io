"""Paired-gap tables.

Every comparison in this project is paired: both methods see the identical election, so
the difference is measured election by election rather than as the distance between two
independently noisy averages. That is what these tables report, and why their confidence
intervals are so much tighter than differencing the two columns would suggest.

From cells 89, 127, 146 and 168 of `vse_simulation.ipynb`."""

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Markdown, display

from .. import config as cfg
from . import context
from .significance import _classify_gap, _verdict_text
from .theme import FG_COLOR, MUTED_COLOR

from ..config import COMPARE_LABELS, METHOD_COLORS, NCAND_SWEEP_LABELS


__all__ = [
    "display_paired_gap_table",
    "display_paired_gap_matrix",
    "display_paired_gap_by_sweep_value",
    "candidate_comparison_table",
]


def display_paired_gap_table(label, baseline_label, label_short=None, baseline_short=None,
                              label_better_name=None, baseline_better_name=None, title=None,
                              spotlight=False):
    """Display a "paired VSE gap by joint-friction scenario" markdown table for `label` vs
    `baseline_label`, reading off the already-computed `joint_results`/`paired_diff_by_scenario`
    (the main joint-scenario run above) -- no new simulation is run here.

    To add a NEW comparison: add the (label, baseline_label) pair to `_paired_diff_pairs` in the
    main run cell above and re-run it (this is where the actual per-election data gets collected,
    since it has to happen DURING the simulation pass to stay paired), then call this function.

    label_short/baseline_short: optional shorter names for the table header (VSE columns), e.g.
    "AT2"/"PT2" for "Approval Top-2"/"Plurality Top-2"; default to the full label.
    label_better_name/baseline_better_name: optional separate override for the "(X better)" text
    in the Significant? column, in case that should read differently than the column header (e.g.
    a fuller name there than the short header); default to label_short/baseline_short.
    title: optional heading override; defaults to "{label} vs {baseline_label}".
    """
    R = context.current()
    joint_results = R.joint_results
    paired_diff_by_scenario = R.paired_diff_by_scenario
    _scenario_names = R.scenario_names
    _register_significance = R.significance.register
    label_short = label_short or label
    baseline_short = baseline_short or baseline_label
    label_better_name = label_better_name or label_short
    baseline_better_name = baseline_better_name or baseline_short
    title = title or f"{label} vs {baseline_label}"
    missing = [name for name in _scenario_names
               if (label, baseline_label) not in paired_diff_by_scenario.get(name, {})]
    if missing:
        raise KeyError(
            f"({label!r}, {baseline_label!r}) missing from paired_diff_by_scenario for {missing} -- "
            "add this pair to _paired_diff_pairs in the main joint-scenario run cell above and "
            "re-run it before calling display_paired_gap_table for this pair."
        )
    lines = [
        f"#### {title}: paired VSE gap by joint-friction scenario",
        "",
        f"| Scenario | {label_short} VSE (%) | {baseline_short} VSE (%) | Gap vs {baseline_short} (pp) | 95% CI (paired, pp) | Significant? |",
        "|---|---|---|---|---|---|",
    ]
    for name in _scenario_names:
        label_vse = joint_results[name][(label, "honBallot")][0] * 100
        baseline_vse = joint_results[name][(baseline_label, "honBallot")][0] * 100
        gap = label_vse - baseline_vse
        ci = paired_diff_by_scenario[name][(label, baseline_label)][1] * 100
        _register_significance(title, name, gap, ci, label_better_name, baseline_better_name, spotlight)
        _, sig = _verdict_text(gap, ci, label_better_name, baseline_better_name)
        lines.append(f"| {name} | {label_vse:.1f} | {baseline_vse:.1f} | {gap:+.1f} | [{gap-ci:+.1f}, {gap+ci:+.1f}] | {sig} |")
    display(Markdown("\n".join(lines)))


def display_paired_gap_matrix(labels, baseline_label, title=None, sort_desc=True):
    """Same layout as Section 19's CE-gap-vs-Schulze tables: one table per _scenario_names
    scenario, every label in `labels` as a row (sorted by gap) vs the SAME baseline_label. Reads
    joint_results/paired_diff_by_scenario (already computed by the main joint-scenario run) -- no
    new simulation. Every (label, baseline_label) pair must already be in _paired_diff_pairs
    (cell defining it, Section 16) with the main run re-executed since."""
    R = context.current()
    joint_results = R.joint_results
    paired_diff_by_scenario = R.paired_diff_by_scenario
    _scenario_names = R.scenario_names
    _register_significance = R.significance.register
    title = title or f"{baseline_label} vs {', '.join(labels)}"
    missing = [
        (name, label) for name in _scenario_names for label in labels
        if (label, baseline_label) not in paired_diff_by_scenario.get(name, {})
    ]
    if missing:
        raise KeyError(
            f"missing pairs in paired_diff_by_scenario: {missing} -- add (label, {baseline_label!r}) "
            "to _paired_diff_pairs and re-run the main joint-scenario cell first."
        )
    lines = [f"### {title}", ""]
    for name in _scenario_names:
        baseline_vse = joint_results[name][(baseline_label, "honBallot")][0] * 100
        sorted_labels = sorted(
            labels, reverse=sort_desc,
            key=lambda l: paired_diff_by_scenario[name][(l, baseline_label)][0],
        )
        lines += [
            f"#### {name}", "",
            f"| Method | {baseline_label} VSE (%) | Method VSE (%) | Gap (pp) | 95% CI | Significant? |",
            "|---|---|---|---|---|---|",
        ]
        for label in sorted_labels:
            if name == "Ideal" and ('Coma' in label or 'Clear-Eyed' in label):
                continue
            label_vse = joint_results[name][(label, "honBallot")][0] * 100
            gap, ci = paired_diff_by_scenario[name][(label, baseline_label)]
            gap *= 100
            ci *= 100
            _register_significance(f"{title}: {name}", label, gap, ci, "runoff", "no runoff")
            _, sig = _verdict_text(gap, ci, "runoff", "no runoff")
            lines.append(f"| {label} | {baseline_vse:.1f} | {label_vse:.1f} | {gap:+.1f} | [{gap-ci:+.1f}, {gap+ci:+.1f}] | {sig} |")
        lines.append("")
    display(Markdown("\n".join(lines)))


def display_paired_gap_by_sweep_value(label, baseline_label, sweep_param, results_by_value, paired_diff_by_value,
                                       label_short=None, baseline_short=None, title=None):
    """Same table shape as display_paired_gap_table (Section 18), but keyed by a swept parameter
    value instead of a joint-friction scenario name -- reads sweep_results_by_param/
    sweep_paired_diff_by_param (Section 13) rather than joint_results/paired_diff_by_scenario."""
    R = context.current()
    _register_significance = R.significance.register
    label_short = label_short or label
    baseline_short = baseline_short or baseline_label
    title = title or f"{label} vs {baseline_label}"
    values = sorted(results_by_value)
    lines = [
        f"#### {title}: paired VSE gap by `{sweep_param}`",
        "",
        f"| {sweep_param} | {label_short} VSE (%) | {baseline_short} VSE (%) | Gap vs {baseline_short} (pp) | 95% CI (paired, pp) | Significant? |",
        "|---|---|---|---|---|---|",
    ]
    for v in values:
        label_vse = results_by_value[v][(label, "honBallot")][0] * 100
        baseline_vse = results_by_value[v][(baseline_label, "honBallot")][0] * 100
        gap = label_vse - baseline_vse
        ci = paired_diff_by_value[v][(label, baseline_label)][1] * 100
        _register_significance(title, f"{sweep_param}={v:.2f}", gap, ci, label_short, baseline_short)
        _, sig = _verdict_text(gap, ci, label_short, baseline_short)
        lines.append(f"| {v:.2f} | {label_vse:.1f} | {baseline_vse:.1f} | {gap:+.1f} | [{gap-ci:+.1f}, {gap+ci:+.1f}] | {sig} |")
    display(Markdown("\n".join(lines)))


def candidate_comparison_table(results_by_ncand, labels, ncand_key):
    """Display a Markdown table comparing VSE by candidate count (NCAND) for the given labels.

    results_by_ncand: {ncand: {(label, chooser): (mean, ci)}}
    labels: list of method labels to include in the table
    ncand_key: string label for the candidate count column
    """
    header = [ncand_key] + [f"{label} VSE (%)" for label in labels] + ["Gap (pp)"]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for ncand in sorted(results_by_ncand):
        row = [str(ncand)]
        for label in labels:
            mean_, ci = results_by_ncand[ncand][(label, "honBallot")]
            row.append(f"{mean_ * 100:.1f}% (+/-{ci * 100:.1f})")
        if len(labels) == 2:
            gap = (results_by_ncand[ncand][(labels[0], "honBallot")][0] -
                   results_by_ncand[ncand][(labels[1], "honBallot")][0]) * 100
            row.append(f"{gap:+.1f}")
        lines.append("| " + " | ".join(row) + " |")
    display(Markdown("\n".join(lines)))
