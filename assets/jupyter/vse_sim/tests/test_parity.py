"""The package must reproduce the original notebook bit-for-bit.

`vse_simulation.ipynb` is left untouched by the modularization, so it stays available as
a reference implementation. This module runs it and `vse_sim` side by side over the SAME
electorates with the SAME RNG seed, and requires every returned number to be exactly
equal -- not close, equal. That is what makes moving ~350KB of code out of the notebook a
provable refactor rather than a rewrite.

If this fails, the package has drifted from the notebook and the difference is a bug.
"""
from collections import defaultdict

import numpy as np
import pytest

from vse_sim import config as cfg
from vse_sim.engine import (reduce_betrayal_summary, reduce_coma_summary,
                            reduce_primary_corruption_summary,
                            reduce_primary_cost_summary, run_vse_simulation)
from vse_sim.tests._notebook_ref import load
from vse_sim.vendored.simulation import seedRandomGenerators
from vse_sim.vendored.voter_models import Electorate, Voter

PARITY_SEED = "parity-check"
PARITY_NITER = 40

# Ideal plus one run per degradation mechanism in isolation plus one with all three at
# once: between them these exercise every branch the loop has (the rho>=1.0 and
# alpha=beta=1.0 no-op fast paths, and the fully-general path).
PARAMS = [
    pytest.param({}, id="ideal"),
    pytest.param({"epistemic_rho": 0.7}, id="epistemic_rho=0.7"),
    pytest.param({"awareness_alpha": 0.7}, id="awareness_alpha=0.7"),
    pytest.param({"fatigue_beta": 0.7}, id="fatigue_beta=0.7"),
    pytest.param({"epistemic_rho": 0.8, "awareness_alpha": 0.8, "fatigue_beta": 0.8},
                 id="joint=0.8"),
]


def _same(a, b):
    """Exact equality, except that NaN counts as equal to NaN.

    Several reducers return NaN by design when a denominator is empty (no decisive
    election, no flip, an all-tied population). Plain `==` calls those unequal, which
    would make an exact match look like a drift, so compare them structurally instead.
    """
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_same(a[k], b[k]) for k in a)
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(_same(x, y) for x, y in zip(a, b))
    if isinstance(a, float) and isinstance(b, float) and a != a and b != b:
        return True  # NaN on both sides
    return a == b


@pytest.fixture(scope="module")
def nb():
    return load()


@pytest.fixture(scope="module")
def pools(nb):
    """One pool of true electorates, materialized in BOTH implementations' classes.

    Drawn once from the notebook's own model, then copied value-for-value into the
    package's `Electorate`/`Voter`. Handing each implementation a pool built from its own
    classes keeps the comparison about the simulation loop rather than about which
    tuple subclass the utilities happen to live in -- and doubles as a check that the
    pool really does round-trip through a plain array of floats, which is what
    `electorates.py` relies on for its on-disk cache.
    """
    nb["seedRandomGenerators"](PARITY_SEED)
    nb_pool = [nb["MODEL"](nb["NVOT"], nb["NCAND"]) for _ in range(PARITY_NITER)]
    as_array = np.array([[list(v) for v in e] for e in nb_pool], dtype=np.float64)
    pkg_pool = [Electorate(Voter(row) for row in election) for election in as_array]
    return nb_pool, pkg_pool


def _run_notebook(nb, pool, params):
    nb["seedRandomGenerators"](PARITY_SEED)
    sinks = dict(betrayal={}, coma={}, primary_cost={}, primary_corruption={},
                 raw=defaultdict(list))
    out = nb["run_vse_simulation"](
        nb["MODEL"], nb["METHODS"], nb["NVOT"], nb["NCAND"], PARITY_NITER,
        nb["CHOOSER_FUNS"], nb["MEDIA"], electorates=pool,
        paired_diff_pairs=nb["_paired_diff_pairs"], paired_ce_pairs=nb["_paired_ce_pairs"],
        raw_vse_sink=sinks["raw"], honest_only=True,
        betrayal_targets=nb["_betrayal_targets"], betrayal_sink=sinks["betrayal"],
        coma_targets=nb["_coma_targets"], coma_sink=sinks["coma"],
        primary_cost_targets=nb["_primary_cost_targets"], primary_cost_sink=sinks["primary_cost"],
        primary_corruption_sink=sinks["primary_corruption"], **params)
    return out, sinks


# Methods the package added on top of the original notebook. The original stays untouched as the
# reference, so parity is checked over the ORIGINAL methods only: the extras are filtered out of
# every package-side input below. (Adding a method still perturbs the shared RNG stream, which is
# why the extras must be excluded from the run itself, not just from the comparison.)
EXTRA_LABELS = {"Schulze (equal ranks)"}


def _orig(pairs):
    return [p for p in pairs if not EXTRA_LABELS & set(p)]


def _run_package(pool, params):
    seedRandomGenerators(PARITY_SEED)
    sinks = dict(betrayal={}, coma={}, primary_cost={}, primary_corruption={},
                 raw=defaultdict(list))
    out = run_vse_simulation(
        cfg.MODEL, [m for m in cfg.METHODS if m[0] not in EXTRA_LABELS], cfg.NVOT, cfg.NCAND,
        PARITY_NITER, cfg.CHOOSER_FUNS, cfg.MEDIA, electorates=pool,
        paired_diff_pairs=_orig(cfg.PAIRED_DIFF_PAIRS), paired_ce_pairs=_orig(cfg.PAIRED_CE_PAIRS),
        raw_vse_sink=sinks["raw"], honest_only=True,
        betrayal_targets=cfg.BETRAYAL_TARGETS, betrayal_sink=sinks["betrayal"],
        coma_targets=cfg.COMA_TARGETS, coma_sink=sinks["coma"],
        primary_cost_targets=cfg.PRIMARY_COST_TARGETS, primary_cost_sink=sinks["primary_cost"],
        primary_corruption_sink=sinks["primary_corruption"], **params)
    return out, sinks


def test_config_matches_notebook_parameters(nb):
    """Every knob the package exposes must carry the notebook's own value."""
    for name in ["NVOT", "NCAND", "NITER", "SEED", "SWEEP_NITER", "SWEEP_VALUES",
                 "JOINT_NITER", "RUNOFF_RHO_SWEEP_NITER", "RUNOFF_SWEEP_NITER",
                 "SECONDARY_SWEEP_NITER", "NCAND_SWEEP_NITER", "EPISTEMIC_RHO",
                 "AWARENESS_ALPHA", "FATIGUE_BETA", "GAP_THRESHOLD_PP", "STAR_TOP_RANK",
                 "COMPARE_LABELS", "NCAND_VALUES", "HIST_LABELS", "SCENARIO_VALUES",
                 "JOINT_SCENARIOS", "RUNOFF_BASELINE_NAMES"]:
        val = getattr(cfg, name)
        if isinstance(val, list):
            val = [v for v in val if v not in EXTRA_LABELS]
        assert val == nb[name], f"config.{name} drifted from the notebook"
    assert str(cfg.MODEL) == str(nb["MODEL"])
    assert [label for label, _ in cfg.METHODS if label not in EXTRA_LABELS] == [label for label, _ in nb["METHODS"]]
    assert {k: v for k, v in cfg.METHOD_COLORS.items() if k not in EXTRA_LABELS} == nb["METHOD_COLORS"]
    assert {k: v for k, v in cfg.METHOD_LINESTYLES.items() if k not in EXTRA_LABELS} == nb["METHOD_LINESTYLES"]
    assert _orig(cfg.PAIRED_DIFF_PAIRS) == nb["_paired_diff_pairs"]
    assert _orig(cfg.PAIRED_CE_PAIRS) == nb["_paired_ce_pairs"]
    assert cfg.BETRAYAL_TARGETS == nb["_betrayal_targets"]
    assert cfg.COMA_TARGETS == nb["_coma_targets"]
    assert cfg.PRIMARY_COST_TARGETS == nb["_primary_cost_targets"]
    assert np.array_equal(cfg.RUNOFF_KAPPA_VALUES, nb["RUNOFF_KAPPA_VALUES"])
    for name in ["MILD_RHO_VALUES", "MODERATE_RHO_VALUES", "HEAVY_RHO_VALUES"]:
        assert np.array_equal(getattr(cfg, name), nb[name]), f"config.{name} drifted"
    assert [p for p, _ in cfg.SWEEP_PARAMS] == [p for p, _ in nb["SWEEP_PARAMS"]]
    for (_, pkg_methods), (_, nb_methods) in zip(cfg.SWEEP_PARAMS, nb["SWEEP_PARAMS"]):
        assert [l for l, _ in pkg_methods if l not in EXTRA_LABELS] == [l for l, _ in nb_methods]


@pytest.mark.parametrize("params", PARAMS)
def test_simulation_loop_is_bit_identical(nb, pools, params):
    nb_pool, pkg_pool = pools
    (nb_summary, nb_ce, nb_pd, nb_pce), nb_sinks = _run_notebook(nb, nb_pool, params)
    (pk_summary, pk_ce, pk_pd, pk_pce), pk_sinks = _run_package(pkg_pool, params)

    assert nb_summary == pk_summary, "vse_summary differs"
    assert nb_ce == pk_ce, "Condorcet-efficiency bookkeeping differs"
    assert nb_pd == pk_pd, "paired VSE diffs differ"
    assert nb_pce == pk_pce, "paired CE diffs differ"
    for name in ["betrayal", "coma", "primary_cost", "primary_corruption"]:
        assert nb_sinks[name] == pk_sinks[name], f"{name} accumulator differs"
    assert dict(nb_sinks["raw"]) == dict(pk_sinks["raw"]), "per-election VSE rows differ"


@pytest.mark.parametrize("params", PARAMS)
def test_reducers_are_bit_identical(nb, pools, params):
    """The accumulators match; so must every rate/cost derived from them."""
    nb_pool, pkg_pool = pools
    _, nb_sinks = _run_notebook(nb, nb_pool, params)
    _, pk_sinks = _run_package(pkg_pool, params)
    for label, acc in nb_sinks["betrayal"].items():
        assert _same(nb["reduce_betrayal_summary"](acc), reduce_betrayal_summary(
            pk_sinks["betrayal"][label])), f"betrayal rates differ for {label}"
    for label, acc in nb_sinks["coma"].items():
        assert _same(nb["reduce_coma_summary"](acc), reduce_coma_summary(
            pk_sinks["coma"][label])), f"coma rates differ for {label}"
    for label, acc in nb_sinks["primary_cost"].items():
        assert _same(nb["reduce_primary_cost_summary"](acc), reduce_primary_cost_summary(
            pk_sinks["primary_cost"][label])), f"primary-cost rates differ for {label}"
    assert _same(nb["reduce_primary_corruption_summary"](nb_sinks["primary_corruption"]),
                 reduce_primary_corruption_summary(pk_sinks["primary_corruption"]))
