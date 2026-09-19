"""Line charts: VSE against a swept parameter, and against the joint scenarios.

From cells 60 and 77 of `vse_simulation.ipynb`. `comparison_chart`'s second panel is the
"flip it round and subtract the baseline" view -- the same data, but showing the gap
directly rather than asking the reader to difference two lines by eye."""

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Markdown, display

from .. import config as cfg
from . import context
from .significance import _classify_gap, _verdict_text
from .theme import FG_COLOR, MUTED_COLOR

from ..config import (COMPARE_LABELS, JOINT_NITER, JOINT_SCENARIOS,
                      METHOD_COLORS, METHOD_LINESTYLES)


__all__ = [
    "comparison_table",
    "comparison_chart",
    "scenario_table_and_plot",
]


def comparison_table(results_by_value, labels, sweep_param, ballot_type="honBallot"):
    """Markdown table: rows=label, columns=sweep_param values, cell=VSE% (+/- CI)."""
    values = sorted(results_by_value)
    header = ["Method"] + [f"{sweep_param}={v:.2f}" for v in values]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for label in labels:
        row = [label]
        for v in values:
            mean_, ci = results_by_value[v][(label, ballot_type)]
            row.append(f"{mean_ * 100:.1f}% (+/-{ci * 100:.1f})")
        lines.append("| " + " | ".join(row) + " |")
    display(Markdown("\n".join(lines)))


def comparison_chart(results_by_value, labels, sweep_param, ballot_type="honBallot",
                      baseline_label=None, title=None):
    """VSE-vs-sweep_param line chart; if baseline_label is given, a second panel shows
    label - baseline for every other label (the 'flip it ... minus STAR' framing)."""
    values = sorted(results_by_value)
    ncols = 2 if baseline_label else 1
    fig, axes = plt.subplots(1, ncols, figsize=(7 * ncols, 5))
    ax_vse = axes[0] if baseline_label else axes
    for label in labels:
        vses = [results_by_value[v][(label, ballot_type)][0] * 100 for v in values]
        ax_vse.plot(values, vses, marker="o", markersize=7, linewidth=2,
                    color=METHOD_COLORS.get(label), linestyle=METHOD_LINESTYLES.get(label, "-"),
                    label=label)
    ax_vse.set_xlabel(sweep_param)
    ax_vse.set_ylabel("VSE (%)")
    ax_vse.set_title(title or f"VSE vs. {sweep_param}")
    ax_vse.legend(fontsize=8)
    ax_vse.grid(True, alpha=0.3)

    if baseline_label:
        ax_gap = axes[1]
        baseline_vses = [results_by_value[v][(baseline_label, ballot_type)][0] * 100 for v in values]
        for label in labels:
            if label == baseline_label:
                continue
            vses = [results_by_value[v][(label, ballot_type)][0] * 100 for v in values]
            gap = [a - b for a, b in zip(vses, baseline_vses)]
            ax_gap.plot(values, gap, marker="o", markersize=7, linewidth=2,
                        color=METHOD_COLORS.get(label), linestyle=METHOD_LINESTYLES.get(label, "-"),
                        label=f"{label} − {baseline_label}")
        ax_gap.axhline(0, color="gray", linewidth=1, linestyle=":")
        ax_gap.set_xlabel(sweep_param)
        ax_gap.set_ylabel("VSE gap (percentage points)")
        ax_gap.set_title(f"Gap vs. {baseline_label}")
        ax_gap.legend(fontsize=8)
        ax_gap.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def scenario_table_and_plot(method_labels):
    # Table: rows = method, columns = scenario, cell = VSE% (+/-CI)
    R = context.current()
    joint_results = R.joint_results
    _scenario_names = R.scenario_names
    _joint_table_lines = ["| Method | " + " | ".join(_scenario_names) + " |",
                        "|---|" + "---|" * len(_scenario_names)]
    for label in method_labels:
        row = [label]
        for name in _scenario_names:
            mean_, ci = joint_results[name][(label, "honBallot")]
            row.append(f"{mean_ * 100:.1f}% (+/-{ci * 100:.1f})")
        _joint_table_lines.append("| " + " | ".join(row) + " |")
    display(Markdown("\n".join(_joint_table_lines)))

    # Grouped bar chart: one group per scenario, one bar per method.
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    _n_labels = len(method_labels)
    _bar_width = 0.8 / _n_labels
    _x = np.arange(len(_scenario_names))
    for i, label in enumerate(method_labels):
        vses = [joint_results[name][(label, "honBallot")][0] * 100 for name in _scenario_names]
        cis = [joint_results[name][(label, "honBallot")][1] * 100 for name in _scenario_names]
        hatch = "//" if "Clear-Eyed" in label else ("xx" if "Coma" in label else None)
        ax.bar(_x + i * _bar_width, vses, _bar_width, yerr=cis, capsize=3,
            color=METHOD_COLORS[label], hatch=hatch, label=label, edgecolor=FG_COLOR, linewidth=0.5,
            error_kw=dict(ecolor=FG_COLOR))
    ax.set_xticks(_x + _bar_width * (_n_labels - 1) / 2)
    ax.set_xticklabels(_scenario_names)
    ax.set_ylabel("VSE (%)")
    ax.set_title(f"VSE under joint realistic-conditions scenarios ({JOINT_NITER} elections/scenario)")
    ax.legend(fontsize=8, loc="center left", bbox_to_anchor=(1.02, 0.5))
    ax.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()
