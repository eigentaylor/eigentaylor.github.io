"""Tables and charts. Reads the stored results; never runs a simulation.

    from vse_sim.render import context, tables, charts
    R = context.load()          # every stage, checked against config.py
    tables.display_paired_gap_table("Approval", "Plurality")

Each module corresponds to a group of the original notebook's display cells, and the
function bodies are copied from it verbatim -- only the bindings changed, from globals in
one big namespace to attributes on the loaded results.
"""
from . import charts, context, diagnostics, labels, projection, robustness, significance, tables, theme  # noqa: F401
