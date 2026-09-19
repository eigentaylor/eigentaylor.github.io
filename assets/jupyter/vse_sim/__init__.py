"""Modular VSE simulation: the code behind `vse_simulation_modular.ipynb`.

Layout
------
`vendored/`   an unmodified copy of the electionscience/vse-sim methodology.
`noise.py`, `friction.py`, `top2.py`, `condorcet.py`
              the mechanisms original to this project.
`config.py`   every parameter, in one place.
`engine.py`   the per-election simulation loop and its reducers.
`sweeps.py`   the drivers that run the loop across a parameter grid.
`stages.py`   the eight expensive stages, each independently reproducible.
`artifacts.py`, `electorates.py`
              on-disk caching of results and electorate pools.
`render/`     tables and charts; reads artifacts, never simulates.

Run `python -m vse_sim.run --help` from `assets/jupyter/`.
"""
