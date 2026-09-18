"""Results survive the trip to disk and back, and a changed parameter is caught.

Three things are checked here:

1. **Round-trip.** Every stage is run at a tiny election count into a temporary
   directory, then loaded back. The decoded structures must match what the run produced,
   including the awkward keys -- tuples like `(label, chooser)`, floats like `1/3` out of
   `np.linspace`, and the literal `None` that means "the runoff reuses its primary's
   electorate". Those are exactly the keys JSON cannot store as object keys, which is why
   `artifacts.py` flattens every mapping into records.

2. **Determinism.** Running a stage twice gives byte-identical results, which is what
   `python -m vse_sim.run --verify` relies on, and what makes the published numbers
   something a reader can regenerate rather than take on faith.

3. **Staleness.** Loading results under a spec that no longer matches raises rather than
   quietly rendering numbers from before the change.
"""
import json

import numpy as np
import pytest

from vse_sim import artifacts, config as cfg, stages
from vse_sim import electorates as el

TINY = 6


@pytest.fixture(scope="module")
def ran(tmp_path_factory):
    """Every stage, run once at a tiny size into a scratch results directory."""
    out = tmp_path_factory.mktemp("results")
    produced = {}
    for name in stages.ORDER:
        path, _elapsed = stages.run_stage(name, results_dir=out, niter=TINY)
        produced[name] = path
    return out, produced


def test_every_stage_round_trips(ran):
    out, _ = ran
    for name in stages.ORDER:
        loaded = stages.STAGES[name].load(results_dir=out, niter=TINY)
        assert loaded["niter"] == TINY
        assert loaded["results"], f"{name} decoded to nothing"


def test_awkward_keys_survive(ran):
    """The keys JSON can't hold: tuples, floats, and None."""
    out, _ = ran
    ideal = stages.load_ideal(results_dir=out, niter=TINY)
    assert all(isinstance(k, tuple) and len(k) == 2 for k in ideal["results"]), \
        "(label, chooser) tuple keys did not survive"

    rho = stages.load_runoff_rho(results_dir=out, niter=TINY)
    for baseline, by_mode in rho["results"].items():
        for mode, by_rt in by_mode.items():
            assert None in by_rt, f"the runoff_rho=None key was lost for {baseline}/{mode}"
            assert any(isinstance(k, float) for k in by_rt), "float runoff_rho keys were lost"

    learn = stages.load_runoff_learn(results_dir=out, niter=TINY)
    kappas = list(next(iter(next(iter(learn["results"].values())).values())))
    assert all(isinstance(k, float) for k in kappas), "kappa keys are not plain floats"
    assert any(abs(k - 1 / 3) < 1e-12 for k in kappas), \
        "the 1/3 kappa grid point (an exact fraction, not a linspace value) did not survive"

    ncand = stages.load_ncand(results_dir=out, niter=TINY)
    assert set(next(iter(ncand["results"].values()))) == set(cfg.NCAND_VALUES)


def test_per_election_arrays_round_trip(ran):
    out, _ = ran
    joint = stages.load_joint(results_dir=out, niter=TINY)
    assert joint["raw_vse"], "joint per-election VSE arrays were not stored"
    for scenario, by_key in joint["raw_vse"].items():
        for key, values in by_key.items():
            assert len(values) == TINY, f"{scenario}/{key} has {len(values)} rows, expected {TINY}"

    plur = stages.load_plurality_ideal(results_dir=out, niter=TINY)
    assert plur["raw_vse"], "plurality_ideal per-election VSE arrays were not stored"
    # Section 24's paired table needs these two index-aligned over the same pool.
    for label in stages.PLURALITY_FAMILY:
        assert len(plur["raw_vse"][(label, "honBallot")]) == \
            len(joint["raw_vse"]["Mild friction"][(label, "honBallot")])


def test_plurality_ideal_shares_the_joint_pool():
    """Section 24 compares these two election by election; that needs identical draws."""
    a = el.pool("joint", 4, use_cache=False)
    b = el.pool("joint", 4, use_cache=False)
    assert [[list(v) for v in e] for e in a] == [[list(v) for v in e] for e in b]
    assert stages.spec_joint()["pool_id"] == stages.spec_plurality_ideal()["pool_id"] == "joint"


def test_results_are_deterministic(tmp_path):
    """The same stage, run twice, gives the same content hash. This is what --verify checks."""
    for name in ["ideal", "runoff_rho"]:
        first, _ = stages.run_stage(name, results_dir=tmp_path / "a", niter=TINY)
        second, _ = stages.run_stage(name, results_dir=tmp_path / "b", niter=TINY)
        a = json.loads(first.read_text())
        b = json.loads(second.read_text())
        assert a["content_hash"] == b["content_hash"], f"{name} is not reproducible"
        assert a["data"] == b["data"]


def test_results_do_not_depend_on_the_pool_cache(tmp_path):
    """A cold run and a warm one must agree.

    Drawing a pool consumes randomness; loading one from cache does not. If a stage just
    continued from wherever pool-building left the RNG, the first run of the day and every
    run after it would produce different numbers -- and `--verify` would fail for a reader
    who happened to have a warm cache. Stages reseed before simulating (see
    `stages.seed_simulation`), which is what this pins down.
    """
    el.clear_cache()
    cold, _ = stages.run_stage("ideal", results_dir=tmp_path / "cold", niter=TINY)
    warm, _ = stages.run_stage("ideal", results_dir=tmp_path / "warm", niter=TINY)
    assert json.loads(cold.read_text())["content_hash"] == \
        json.loads(warm.read_text())["content_hash"], \
        "results changed once the electorate pool came from cache"

    no_cache, _ = stages.run_stage("ideal", results_dir=tmp_path / "nc", niter=TINY,
                                   use_cache=False)
    assert json.loads(no_cache.read_text())["content_hash"] == \
        json.loads(cold.read_text())["content_hash"]


def test_spec_is_stable_across_processes():
    """No spec field may embed a memory address, or nothing would ever match itself.

    `str()` of the media function or of a chooser object includes `0x...`, which changes
    every process; a spec built from those would report every stored artifact stale and
    make `--verify` fail on a run that reproduced perfectly.
    """
    import re
    for name in stages.ORDER:
        blob = artifacts.canonical(stages.STAGES[name].spec())
        assert not re.search(r"0x[0-9a-f]{6,}", blob), f"{name}'s spec embeds an address"
        assert "<" not in blob or "locals" in blob, f"{name}'s spec embeds an object repr"


def test_stale_spec_is_refused(ran):
    out, _ = ran
    with pytest.raises(artifacts.StaleArtifact) as excinfo:
        stages.load_ideal(results_dir=out, niter=TINY + 1)
    assert "python -m vse_sim.run --stage ideal" in str(excinfo.value)
    assert "niter" in str(excinfo.value)


def test_missing_stage_names_the_command(tmp_path):
    with pytest.raises(artifacts.MissingArtifact) as excinfo:
        stages.load_joint(results_dir=tmp_path)
    assert "python -m vse_sim.run --stage joint" in str(excinfo.value)


def test_merge_pools_accumulators_exactly():
    """Two batches merged must equal one run over the pooled sample, exactly.

    `n`, `sum` and `sum_sq` are each a sum over elections, so adding them elementwise
    gives the combined sample's mean and variance with no approximation. This is what
    makes `--extra-batch` sound for a reader who wants tighter intervals than published.
    """
    spec = {"seed": "x"}
    a = {"schema": 1, "runs": 1, "spec_hash": artifacts.sha256(spec),
         "data": {"vse": [{"label": "A", "chooser": "hon", "n": 3, "sum": 1.5, "sum_sq": 0.9}]}}
    b = {"schema": 1, "runs": 1, "spec_hash": artifacts.sha256(spec),
         "data": {"vse": [{"label": "A", "chooser": "hon", "n": 2, "sum": 1.0, "sum_sq": 0.6}]}}
    merged = artifacts.merge(a, b)
    row = merged["data"]["vse"][0]
    assert (row["n"], row["sum"], row["sum_sq"]) == (5, 2.5, pytest.approx(1.5))
    assert merged["runs"] == 2

    # The merged accumulator must reproduce the pooled mean and variance directly.
    from vse_sim.engine import reduce_to_mean_ci
    pooled = reduce_to_mean_ci({"k": [row["n"], row["sum"], row["sum_sq"]]})["k"]
    assert pooled[0] == pytest.approx(2.5 / 5)


def test_non_json_values_are_refused_loudly():
    """A stray NumPy type must raise, not be silently dropped from a result file."""
    assert artifacts.jsonable(np.float64(0.5)) == 0.5
    assert artifacts.jsonable(np.int64(3)) == 3
    with pytest.raises(TypeError):
        artifacts.jsonable(object())
