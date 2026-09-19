"""Load the ORIGINAL `vse_simulation.ipynb`'s code into a throwaway namespace.

The original notebook is deliberately left untouched by the modularization, which makes
it a permanent reference implementation: `test_parity.py` runs it side by side with
`vse_sim` and requires bit-identical results. If a future edit to the package changes a
number, that test fails and names the function.

Only code that defines things is exec'd. The cells that run simulations, draw charts or
display tables are not touched.
"""
import contextlib
import io
import json
import pathlib

# Cells 4-38: shared imports, decorators, core, voter models, strategies, the five
# methods, the presets, epistemic noise, the Top-2 hybrids, participation friction, the
# parameters, the method list, Condorcet ground truth, the simulation loop.
LIBRARY_CELLS = [4, 6, 8, 10, 12, 14, 15, 16, 17, 18, 19, 21, 23, 25, 27, 32, 34, 36, 38]

# The constant blocks `config.py` was assembled from, as (cell, first_line, last_line).
# These slices are exactly the ones `config.py` copied, so comparing the two catches any
# later drift in either direction. Lines are 1-based and inclusive; None means "to the
# end of the cell". Slicing is needed because several of these cells mix constants with
# function definitions or with a simulation run.
CONFIG_SLICES = [
    (39, 1, None),     # COMPARE_LABELS
    (40, 1, None),     # _paired_diff_pairs
    (41, 1, 4),        # _paired_ce_pairs
    (41, 7, 14),       # _betrayal_targets / _coma_targets / _primary_cost_targets
    (61, 1, None),     # SWEEP_PARAMS and the method subsets it sweeps
    (73, 1, 8),        # SCENARIO_VALUES / JOINT_SCENARIOS
    (105, 62, 110),    # RUNOFF_* grids and factories
    (113, 1, None),    # RUNOFF_KAPPA_VALUES and the learn-sweep variants
    (166, 101, 103),   # NCAND_SWEEP_LABELS / NCAND_VALUES
    (122, 1, 1),       # STAR_SCORE_LABELS
    (171, 1, 1),       # HIST_LABELS
    (171, 4, 11),      # CLAMP_NEGATIVE_VALUES
]

# The sweep drivers `sweeps.py` was assembled from, same (cell, first, last) convention.
# Sliced to leave out the render helpers that share those cells (cell 60's
# comparison_table/comparison_chart) and the constant blocks already in CONFIG_SLICES.
SWEEP_SLICES = [
    (60, 1, 59),      # sweep_methods
    (73, 10, None),   # run_joint_scenarios
    (105, 1, 60),     # sweep_runoff_rho
    (111, 1, None),   # sweep_runoff_learn
    (166, 1, 99),     # sweep_ncand / run_ncand_under_joint_scenarios
]

NOTEBOOK = pathlib.Path(__file__).resolve().parents[2] / "vse_simulation.ipynb"


def _cells():
    return json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]


def source(idx, start=1, end=None):
    """One cell's source, optionally sliced to a 1-based inclusive line range."""
    lines = "".join(_cells()[idx]["source"]).split("\n")
    return "\n".join(lines[start - 1:len(lines) if end is None else end])


def load(with_config=True, with_sweeps=False):
    """Exec the notebook's definitions and return the resulting namespace.

    `display`/`Markdown` are stubbed to no-ops so the sanity-check cells' output doesn't
    print; their `assert`s still run, which is itself a check on the original notebook.
    """
    cells = _cells()
    parts = ["".join(cells[i]["source"]) for i in LIBRARY_CELLS]
    if with_config:
        parts += [source(i, a, b) for i, a, b in CONFIG_SLICES]
    if with_sweeps:
        parts += [source(i, a, b) for i, a, b in SWEEP_SLICES]
    ns = {
        "__name__": "vse_notebook_reference",
        "display": lambda *a, **k: None,
        "Markdown": lambda s: s,
    }
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile("\n".join(parts), str(NOTEBOOK), "exec"), ns)
    return ns
