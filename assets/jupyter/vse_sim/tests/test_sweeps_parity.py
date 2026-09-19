"""The sweep drivers must reproduce the original notebook bit-for-bit too.

`test_parity.py` covers the per-election loop. This covers the five functions that drive
it across a parameter grid -- the code that was reassembled into `sweeps.py` from five
different notebook cells, and so has the most opportunity to have been rearranged wrong.

Each test hands both implementations the SAME electorate pool and reseeds identically
before each call, so any difference is the driver's, not the draw's.
"""
import numpy as np
import pytest

from vse_sim import config as cfg
from vse_sim import sweeps
from vse_sim.tests._notebook_ref import load
from vse_sim.tests.test_parity import _same
from vse_sim.vendored.simulation import seedRandomGenerators
from vse_sim.vendored.voter_models import Electorate, Voter

SEED = "sweep-parity"
NITER = 12


@pytest.fixture(scope="module")
def nb():
    return load(with_sweeps=True)


@pytest.fixture(scope="module")
def pools(nb):
    seedRandomGenerators(SEED)
    nb_pool = [nb["MODEL"](nb["NVOT"], nb["NCAND"]) for _ in range(NITER)]
    arr = np.array([[list(v) for v in e] for e in nb_pool], dtype=np.float64)
    return nb_pool, [Electorate(Voter(r) for r in e) for e in arr]


def _both(nb, nb_call, pkg_call):
    seedRandomGenerators(SEED)
    left = nb_call()
    seedRandomGenerators(SEED)
    right = pkg_call()
    return left, right


def test_sweep_methods(nb, pools):
    nb_pool, pkg_pool = pools
    labels = ["Plurality", "Approval", "STAR", "Condorcet (Schulze)"]
    values = [0.7, 0.9]
    kwargs = dict(betrayal_targets=cfg.STAR_BETRAYAL_TARGETS, honest_only=True,
                  paired_diff_pairs=[("Approval", "STAR")])
    nb_bs, pkg_bs = {}, {}
    nb_cs, pkg_cs = {}, {}
    left, right = _both(
        nb,
        lambda: nb["sweep_methods"](labels, "epistemic_rho", values, NITER,
                                    electorates=nb_pool, betrayal_sink_by_value=nb_bs,
                                    primary_corruption_sink_by_value=nb_cs, **kwargs),
        lambda: sweeps.sweep_methods(labels, "epistemic_rho", values, NITER,
                                     electorates=pkg_pool, betrayal_sink_by_value=pkg_bs,
                                     primary_corruption_sink_by_value=pkg_cs, **kwargs))
    assert _same(left, right), "sweep_methods results differ"
    assert _same(nb_bs, pkg_bs), "sweep_methods betrayal sinks differ"
    assert _same(nb_cs, pkg_cs), "sweep_methods primary-corruption sinks differ"


def test_run_joint_scenarios(nb, pools):
    nb_pool, pkg_pool = pools
    labels = ["Plurality", "Approval", "Approval Top-2", "Approval Top-2 (Coma)", "STAR"]
    scenarios = {"Mild friction": cfg.JOINT_SCENARIOS["Mild friction"],
                 "Heavy friction": cfg.JOINT_SCENARIOS["Heavy friction"]}
    sinks = [({}, {}) for _ in range(5)]
    nb_raw, pkg_raw = {}, {}
    args = dict(paired_diff_pairs=[("Approval", "STAR")],
                paired_ce_pairs=[("Approval", "STAR")],
                betrayal_targets=cfg.BETRAYAL_TARGETS,
                coma_targets=[("Approval Top-2 (Coma)", 1)],
                primary_cost_targets=cfg.PRIMARY_COST_TARGETS)
    left, right = _both(
        nb,
        lambda: nb["run_joint_scenarios"](labels, scenarios, NITER, electorates=nb_pool,
                                          raw_vse_by_scenario=nb_raw,
                                          betrayal_sink_by_scenario=sinks[0][0],
                                          coma_sink_by_scenario=sinks[1][0],
                                          primary_corruption_sink_by_scenario=sinks[2][0],
                                          primary_cost_sink_by_scenario=sinks[3][0], **args),
        lambda: sweeps.run_joint_scenarios(labels, scenarios, NITER, electorates=pkg_pool,
                                           raw_vse_by_scenario=pkg_raw,
                                           betrayal_sink_by_scenario=sinks[0][1],
                                           coma_sink_by_scenario=sinks[1][1],
                                           primary_corruption_sink_by_scenario=sinks[2][1],
                                           primary_cost_sink_by_scenario=sinks[3][1], **args))
    assert _same(left, right), "run_joint_scenarios results differ"
    assert _same(nb_raw, pkg_raw), "per-election VSE rows differ"
    for i, name in enumerate(["betrayal", "coma", "primary_corruption", "primary_cost"]):
        assert _same(sinks[i][0], sinks[i][1]), f"{name} sink differs"


def test_sweep_runoff_rho(nb, pools):
    nb_pool, pkg_pool = pools
    primary = cfg.JOINT_SCENARIOS["Mild friction"]
    modes = cfg.RUNOFF_AWARENESS_MODES_MAIN
    aw = {k: (lambda rt, _f=f: _f(rt, primary["awareness_alpha"])) for k, f in modes.items()}
    left, right = _both(
        nb,
        lambda: nb["sweep_runoff_rho"](cfg.RUNOFF_METHOD_FACTORIES, [0.5, 1.0], primary,
                                       NITER, aw, electorates=nb_pool),
        lambda: sweeps.sweep_runoff_rho(cfg.RUNOFF_METHOD_FACTORIES, [0.5, 1.0], primary,
                                        NITER, aw, electorates=pkg_pool))
    assert _same(left, right), "sweep_runoff_rho results differ"


def test_sweep_runoff_learn(nb, pools):
    nb_pool, pkg_pool = pools
    primary = cfg.JOINT_SCENARIOS["Mild friction"]
    baseline = ("STAR", cfg.METHODS_LOOKUP["STAR"])
    left, right = _both(
        nb,
        lambda: nb["sweep_runoff_learn"](cfg.RUNOFF_LEARN_METHOD_FACTORIES, [0.0, 1.0],
                                         primary, NITER, None, electorates=nb_pool,
                                         paired_baseline=baseline),
        lambda: sweeps.sweep_runoff_learn(cfg.RUNOFF_LEARN_METHOD_FACTORIES, [0.0, 1.0],
                                          primary, NITER, None, electorates=pkg_pool,
                                          paired_baseline=baseline))
    assert _same(left, right), "sweep_runoff_learn results differ"


def test_sweep_ncand(nb, pools):
    labels = cfg.NCAND_SWEEP_LABELS
    ncands = [3, 5]
    seedRandomGenerators(SEED)
    by_ncand_nb = {n: [nb["MODEL"](nb["NVOT"], n) for _ in range(NITER)] for n in ncands}
    by_ncand_pkg = {n: [Electorate(Voter(list(v)) for v in e) for e in pool]
                    for n, pool in by_ncand_nb.items()}
    pairs = [("Approval Top-2", "Plurality Top-2")]
    left, right = _both(
        nb,
        lambda: nb["sweep_ncand"](labels, ncands, NITER, friction_params={"epistemic_rho": 0.8},
                                  electorates_by_ncand=by_ncand_nb, paired_diff_pairs=pairs),
        lambda: sweeps.sweep_ncand(labels, ncands, NITER, friction_params={"epistemic_rho": 0.8},
                                   electorates_by_ncand=by_ncand_pkg, paired_diff_pairs=pairs))
    assert _same(left, right), "sweep_ncand results differ"
