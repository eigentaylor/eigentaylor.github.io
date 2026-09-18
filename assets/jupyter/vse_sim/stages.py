"""The eight expensive stages, and how each one is stored and read back.

Everything slow in this project happens in one of the stages below. Each is a pure
function of `config.py` and `config.SEED`: it draws its own electorate pool by a declared
`pool_id`, runs, and writes its accumulators to `results/<stage>.json`. None of them
depends on any other having run first, which is what lets `run.py --verify` reproduce any
one of them on its own and what makes the published numbers checkable rather than merely
published.

    ideal            section 9   the baseline run, the only one using the full chooser battery
    sweeps           section 13  each degradation parameter swept on its own
    joint            section 16  all three parameters moved together
    runoff_rho       section 21  how much a better-informed runoff helps
    runoff_learn     section 21  the same question in terms of a chance to learn
    plurality_ideal  section 24  an Ideal-only Plurality-family run, paired with `joint`
    ncand            section 25  Approval Top-2 vs Plurality Top-2 by candidate count
    secondary        section 21  disabled in the notebook (SKIP_CELL = True); kept for parity

Some stages share a pool on purpose. Section 24's paired table compares `plurality_ideal`
against `joint` election by election and asserts the two are index-aligned, which is only
meaningful over identical draws -- so both declare `pool_id="joint"`. The two runoff
sweeps likewise share one pool per baseline scenario.

`load_all()` reassembles what the notebook's cells 46-47 and 76 did by hand: reducing the
accumulators, copying the Ideal run into the joint scenarios and the sweeps at 1.0, and
applying the alias fix-up for methods that are mathematically identical under no
friction.
"""
import pathlib
import time
from collections import defaultdict

import numpy as np

from . import artifacts, config as cfg, electorates, sweeps
from .engine import reduce_to_ce, reduce_to_mean_ci, run_vse_simulation
from .vendored.simulation import baseRuns, seedRandomGenerators

Z_95 = 1.96


def seed_simulation(*parts):
    """Seed the RNG for the work that follows, independently of how the pool was obtained.

    A stage draws its electorates and then runs; both consume randomness. If the run
    simply continued from wherever pool-drawing left the RNG, then loading a pool from
    cache -- which draws nothing -- would leave a different state and produce different
    numbers than a cold run. Reseeding here makes a stage's results depend only on
    `config.SEED` and the stage's own name, never on what the cache happened to hold.

    Every sub-run inside a stage (one swept parameter, one baseline scenario) gets its own
    seed too, so it can be reproduced without running the ones before it.
    """
    batch = [] if not electorates.BATCH else [f"batch{electorates.BATCH}"]
    seedRandomGenerators("/".join([cfg.SEED, *map(str, parts), *batch, "sim"]))

# Section names -> how `artifacts.to_records` should flatten that section. Declared once
# here so writing and reading a stage can never disagree about the shape.
LEVELS = {
    "vse": [("label", "chooser")],
    "paired_diff": [("label", "baseline")],
    "paired_ce": [("label", "baseline")],
    "ce_wins": [("label", "chooser")],
    "ce_denominator": ["kind"],
    "betrayal": [("label",)],
    "coma": [("label",)],
    "primary_cost": [("label",)],
    "primary_corruption": ["kind"],
}


def _by(prefix, levels):
    """The same section, nested one level deeper under `prefix` (a scenario, a swept value)."""
    return [prefix] + levels


def _base_spec(**extra):
    """The parameters a stage's results depend on, described stably.

    "Stably" is the whole point: `str()` of the media function or of a chooser object
    includes its memory address, which changes every process, so a spec built from those
    would never match itself twice -- the notebook would report every artifact stale, and
    `--verify` would fail on a run that actually reproduced perfectly. Only values with a
    process-independent representation belong here.

    Which choosers ran is deliberately absent: it is visible directly in the stored
    records, every one of which carries its own `chooser` field.
    """
    return {"seed": cfg.SEED, "nvot": cfg.NVOT, "ncand": cfg.NCAND, "model": str(cfg.MODEL),
            "media": cfg.MEDIA.__qualname__, **extra}


def _ce_sections(ce_raw):
    """`(cw_exists_count, {key: wins})` split into per-method rows and one denominator.

    Whether a true Condorcet winner exists is a property of the elections alone -- it
    doesn't depend on any method or chooser -- so it is one number per run rather than a
    column repeated on every row. It is written as an explicit `cw_exists` field, not
    through the generic scalar-leaf encoding, because that encoding names its field
    `value`, which would collide with the `value` a swept parameter is keyed by.
    """
    cw_exists, wins = ce_raw
    return artifacts.to_records(wins, LEVELS["vse"], scalar_name="cw_wins"), int(cw_exists)


# ---------------------------------------------------------------------------------
# Stage 1 -- section 9: the baseline "Ideal" run
# ---------------------------------------------------------------------------------

def spec_ideal(niter=None):
    return _base_spec(niter=cfg.NITER if niter is None else niter,
                      methods=[l for l, _ in cfg.METHODS],
                      paired_diff_pairs=[list(p) for p in cfg.PAIRED_DIFF_PAIRS],
                      paired_ce_pairs=[list(p) for p in cfg.PAIRED_CE_PAIRS],
                      pool_id="ideal")


def run_ideal(niter=None, use_cache=True):
    """Every method at rho = alpha = beta = 1.0, with the full honest/strategic battery.

    This is the only stage that computes strategic ballots: nothing downstream of it ever
    reads a non-honest chooser, so every other stage runs `honest_only=True`.
    """
    niter = cfg.NITER if niter is None else niter
    pool = electorates.pool("ideal", niter, use_cache=use_cache)
    seed_simulation("ideal")
    raw_vse, betrayal, coma, primary_cost = defaultdict(list), {}, {}, {}
    summary, ce_raw, paired_diff, paired_ce = run_vse_simulation(
        cfg.MODEL, cfg.METHODS, cfg.NVOT, cfg.NCAND, niter, baseRuns, cfg.MEDIA,
        electorates=pool,
        epistemic_rho=cfg.EPISTEMIC_RHO, awareness_alpha=cfg.AWARENESS_ALPHA,
        fatigue_beta=cfg.FATIGUE_BETA,
        paired_diff_pairs=cfg.PAIRED_DIFF_PAIRS, paired_ce_pairs=cfg.PAIRED_CE_PAIRS,
        raw_vse_sink=raw_vse,
        betrayal_targets=cfg.BETRAYAL_TARGETS, betrayal_sink=betrayal,
        coma_targets=cfg.COMA_TARGETS, coma_sink=coma,
        primary_cost_targets=cfg.PRIMARY_COST_TARGETS, primary_cost_sink=primary_cost)
    ce_wins, cw_exists = _ce_sections(ce_raw)
    data = {
        "vse": artifacts.to_records(summary, LEVELS["vse"]),
        "paired_diff": artifacts.to_records(paired_diff, LEVELS["paired_diff"]),
        "paired_ce": artifacts.to_records(paired_ce, LEVELS["paired_ce"]),
        "ce_wins": ce_wins,
        "ce_denominator": [{"cw_exists": cw_exists}],
        "betrayal": artifacts.to_records(betrayal, [("label",)]),
        "coma": artifacts.to_records(coma, [("label",)]),
        "primary_cost": artifacts.to_records(primary_cost, [("label",)]),
    }
    arrays = {f"{label}||{chooser}": np.asarray(vals, dtype=np.float64)
              for (label, chooser), vals in raw_vse.items()}
    return spec_ideal(niter), data, arrays


def load_ideal(results_dir=artifacts.RESULTS_DIR, z=Z_95, niter=None):
    payload = artifacts.load("ideal", spec_ideal(niter), results_dir)
    d = payload["data"]
    summary = artifacts.from_records(d["vse"], LEVELS["vse"])
    wins = {k: v for k, v in artifacts.from_records(d["ce_wins"], LEVELS["vse"], scalar_name="cw_wins").items()}
    cw_exists = d["ce_denominator"][0]["cw_exists"]
    results = reduce_to_mean_ci(summary, z)
    return {
        "raw_summary": summary,
        "results": results,
        "ce_results": reduce_to_ce((cw_exists, wins), results.keys()),
        "raw_ce": (cw_exists, wins),
        "paired_diff_raw": artifacts.from_records(d["paired_diff"], LEVELS["paired_diff"]),
        "paired_ce_raw": artifacts.from_records(d["paired_ce"], LEVELS["paired_ce"]),
        "paired_diff": reduce_to_mean_ci(
            artifacts.from_records(d["paired_diff"], LEVELS["paired_diff"]), z),
        "paired_ce": reduce_to_mean_ci(
            artifacts.from_records(d["paired_ce"], LEVELS["paired_ce"]), z),
        "betrayal": artifacts.from_records(d["betrayal"], [("label",)]),
        "coma": artifacts.from_records(d["coma"], [("label",)]),
        "primary_cost": artifacts.from_records(d["primary_cost"], [("label",)]),
        "raw_vse": _load_arrays("ideal", results_dir),
        "niter": payload["spec"]["niter"],
    }


# ---------------------------------------------------------------------------------
# Stage 2 -- section 13: each degradation parameter swept on its own
# ---------------------------------------------------------------------------------

def spec_sweeps(niter=None):
    return _base_spec(niter=cfg.SWEEP_NITER if niter is None else niter, values=list(cfg.SWEEP_VALUES_TO_RUN),
                      params={p: [l for l, _ in ms] for p, ms in cfg.SWEEP_PARAMS},
                      paired_diff_pairs=[list(p) for p in cfg.SCORE_STAR_PAIRED_DIFF_PAIRS],
                      betrayal_targets=[list(t) for t in cfg.STAR_BETRAYAL_TARGETS])


def run_sweeps(niter=None, use_cache=True):
    """One pool per swept parameter (as the notebook does), shared across its values."""
    niter = cfg.SWEEP_NITER if niter is None else niter
    data = {k: [] for k in ("vse", "paired_diff", "ce_wins", "ce_denominator",
                            "betrayal", "primary_corruption")}
    for param, methods in cfg.SWEEP_PARAMS:
        pool = electorates.pool(f"sweep/{param}", niter, use_cache=use_cache)
        seed_simulation("sweeps", param)
        raw, betrayal_by_value, corruption_by_value = {}, {}, {}
        sweeps.sweep_methods(
            [l for l, _ in methods], param, cfg.SWEEP_VALUES_TO_RUN, niter,
            electorates=pool, honest_only=True, raw_summary_sink=raw,
            betrayal_targets=cfg.STAR_BETRAYAL_TARGETS,
            betrayal_sink_by_value=betrayal_by_value,
            paired_diff_pairs=cfg.SCORE_STAR_PAIRED_DIFF_PAIRS,
            primary_corruption_sink_by_value=corruption_by_value)
        for value, parts in raw.items():
            key = {"param": param, "value": value}
            data["vse"] += [{**key, **r} for r in artifacts.to_records(parts["vse"], LEVELS["vse"])]
            data["paired_diff"] += [{**key, **r} for r in
                                    artifacts.to_records(parts["paired_diff"], LEVELS["paired_diff"])]
            wins, cw_exists = _ce_sections(parts["ce"])
            data["ce_wins"] += [{**key, **r} for r in wins]
            data["ce_denominator"].append({**key, "cw_exists": cw_exists})
        for value, sink in betrayal_by_value.items():
            data["betrayal"] += [{"param": param, "value": value, **r}
                                 for r in artifacts.to_records(sink, [("label",)])]
        for value, sink in corruption_by_value.items():
            data["primary_corruption"].append({"param": param, "value": value, **sink})
    return spec_sweeps(niter), data, {}


def load_sweeps(results_dir=artifacts.RESULTS_DIR, z=Z_95, niter=None):
    payload = artifacts.load("sweeps", spec_sweeps(niter), results_dir)
    d = payload["data"]
    out = {"results": {}, "ce": {}, "paired_diff": {}, "raw_summary": {},
           "betrayal": {}, "primary_corruption": {}, "niter": payload["spec"]["niter"]}
    vse = artifacts.from_records(d["vse"], ["param", "value", ("label", "chooser")])
    pdf = artifacts.from_records(d["paired_diff"], ["param", "value", ("label", "baseline")])
    wins = artifacts.from_records(d["ce_wins"], ["param", "value", ("label", "chooser")], scalar_name="cw_wins")
    denom = {(r["param"], r["value"]): r["cw_exists"] for r in d["ce_denominator"]}
    for param in vse:
        out["raw_summary"][param] = vse[param]
        out["results"][param] = {v: reduce_to_mean_ci(s, z) for v, s in vse[param].items()}
        out["paired_diff"][param] = {v: reduce_to_mean_ci(s, z) for v, s in pdf[param].items()}
        out["ce"][param] = {v: reduce_to_ce((denom[(param, v)], wins[param][v]),
                                            out["results"][param][v].keys())
                            for v in wins[param]}
    out["betrayal"] = artifacts.from_records(d["betrayal"], ["param", "value", ("label",)])
    for row in d["primary_corruption"]:
        row = dict(row)
        param, value = row.pop("param"), row.pop("value")
        out["primary_corruption"].setdefault(param, {})[value] = row
    return out


# ---------------------------------------------------------------------------------
# Stage 3 -- section 16: all three parameters moved together
# ---------------------------------------------------------------------------------

JOINT_SCENARIOS_TO_RUN = {n: p for n, p in cfg.JOINT_SCENARIOS.items() if n != "Ideal"}


def spec_joint(niter=None):
    return _base_spec(niter=cfg.JOINT_NITER if niter is None else niter, scenarios=JOINT_SCENARIOS_TO_RUN,
                      labels=list(cfg.COMPARE_LABELS),
                      paired_diff_pairs=[list(p) for p in cfg.PAIRED_DIFF_PAIRS],
                      paired_ce_pairs=[list(p) for p in cfg.PAIRED_CE_PAIRS],
                      pool_id="joint")


def run_joint(niter=None, use_cache=True):
    """The three friction scenarios. "Ideal" is not re-simulated -- it IS the `ideal` stage."""
    niter = cfg.JOINT_NITER if niter is None else niter
    pool = electorates.pool("joint", niter, use_cache=use_cache)
    seed_simulation("joint")
    raw, raw_vse = {}, {}
    betrayal, coma, corruption, primary_cost = {}, {}, {}, {}
    sweeps.run_joint_scenarios(
        cfg.COMPARE_LABELS, JOINT_SCENARIOS_TO_RUN, niter, electorates=pool,
        raw_summary_sink=raw, paired_diff_pairs=cfg.PAIRED_DIFF_PAIRS,
        paired_ce_pairs=cfg.PAIRED_CE_PAIRS, raw_vse_by_scenario=raw_vse,
        betrayal_targets=cfg.BETRAYAL_TARGETS, betrayal_sink_by_scenario=betrayal,
        coma_targets=cfg.COMA_TARGETS, coma_sink_by_scenario=coma,
        primary_corruption_sink_by_scenario=corruption,
        primary_cost_targets=cfg.PRIMARY_COST_TARGETS, primary_cost_sink_by_scenario=primary_cost)
    data = {k: [] for k in ("vse", "paired_diff", "paired_ce", "ce_wins", "ce_denominator",
                            "betrayal", "coma", "primary_cost", "primary_corruption")}
    for scenario, parts in raw.items():
        key = {"scenario": scenario}
        data["vse"] += [{**key, **r} for r in artifacts.to_records(parts["vse"], LEVELS["vse"])]
        data["paired_diff"] += [{**key, **r} for r in
                                artifacts.to_records(parts["paired_diff"], LEVELS["paired_diff"])]
        data["paired_ce"] += [{**key, **r} for r in
                              artifacts.to_records(parts["paired_ce"], LEVELS["paired_ce"])]
        wins, cw_exists = _ce_sections(parts["ce"])
        data["ce_wins"] += [{**key, **r} for r in wins]
        data["ce_denominator"].append({**key, "cw_exists": cw_exists})
    for name, sink in [("betrayal", betrayal), ("coma", coma), ("primary_cost", primary_cost)]:
        for scenario, by_label in sink.items():
            data[name] += [{"scenario": scenario, **r}
                           for r in artifacts.to_records(by_label, [("label",)])]
    for scenario, sink in corruption.items():
        data["primary_corruption"].append({"scenario": scenario, **sink})
    arrays = {f"{scenario}||{label}||{chooser}": np.asarray(vals, dtype=np.float64)
              for scenario, by_key in raw_vse.items()
              for (label, chooser), vals in by_key.items()}
    return spec_joint(niter), data, arrays


def load_joint(results_dir=artifacts.RESULTS_DIR, z=Z_95, niter=None):
    payload = artifacts.load("joint", spec_joint(niter), results_dir)
    d = payload["data"]
    vse = artifacts.from_records(d["vse"], ["scenario", ("label", "chooser")])
    wins = artifacts.from_records(d["ce_wins"], ["scenario", ("label", "chooser")], scalar_name="cw_wins")
    denom = {r["scenario"]: r["cw_exists"] for r in d["ce_denominator"]}
    results = {s: reduce_to_mean_ci(v, z) for s, v in vse.items()}
    corruption = {}
    for row in d["primary_corruption"]:
        row = dict(row)
        corruption[row.pop("scenario")] = row
    return {
        "raw_summary": vse,
        "results": results,
        "ce": {s: reduce_to_ce((denom[s], wins[s]), results[s].keys()) for s in wins},
        "paired_diff": {s: reduce_to_mean_ci(v, z) for s, v in artifacts.from_records(
            d["paired_diff"], ["scenario", ("label", "baseline")]).items()},
        "paired_ce": {s: reduce_to_mean_ci(v, z) for s, v in artifacts.from_records(
            d["paired_ce"], ["scenario", ("label", "baseline")]).items()},
        "paired_diff_raw": artifacts.from_records(d["paired_diff"],
                                                  ["scenario", ("label", "baseline")]),
        "betrayal": artifacts.from_records(d["betrayal"], ["scenario", ("label",)]),
        "coma": artifacts.from_records(d["coma"], ["scenario", ("label",)]),
        "primary_cost": artifacts.from_records(d["primary_cost"], ["scenario", ("label",)]),
        "primary_corruption": corruption,
        "raw_vse": _load_arrays("joint", results_dir, depth=3),
        "niter": payload["spec"]["niter"],
    }


# ---------------------------------------------------------------------------------
# Stage 4 -- section 21: sweeping the runoff's own information level
# ---------------------------------------------------------------------------------

def spec_runoff_rho(niter=None):
    return _base_spec(niter=cfg.RUNOFF_RHO_SWEEP_NITER if niter is None else niter,
                      baselines=list(cfg.RUNOFF_BASELINE_NAMES),
                      rho_values={b: [None if x is None else float(x) for x in v]
                                  for b, v in cfg.RUNOFF_RHO_VALUES_BY_BASELINE.items()},
                      methods=list(cfg.RUNOFF_METHOD_FACTORIES),
                      modes=list(cfg.RUNOFF_AWARENESS_MODES_MAIN))


def run_runoff_rho(niter=None, use_cache=True):
    niter = cfg.RUNOFF_RHO_SWEEP_NITER if niter is None else niter
    rows = []
    for baseline in cfg.RUNOFF_BASELINE_NAMES:
        params = cfg.JOINT_SCENARIOS[baseline]
        # Same pool id as `runoff_learn`, which asks for more elections. Pools are
        # prefix-compatible (see electorates.py), so whichever stage runs first sizes the
        # cache and the other reuses or grows it -- both still see the same draws.
        pool = electorates.pool(f"runoff/{baseline}", niter, use_cache=use_cache)
        seed_simulation("runoff_rho", baseline)
        awareness = {name: (lambda rt, _f=fn: _f(rt, params["awareness_alpha"]))
                     for name, fn in cfg.RUNOFF_AWARENESS_MODES_MAIN.items()}
        raw = {}
        sweeps.sweep_runoff_rho(cfg.RUNOFF_METHOD_FACTORIES,
                                cfg.RUNOFF_RHO_VALUES_BY_BASELINE[baseline], params, niter,
                                awareness, electorates=pool, raw_summary_sink=raw)
        rows += [{"baseline": baseline, **r} for r in
                 artifacts.to_records(raw, ["mode", "runoff_rho", ("label", "chooser")])]
    return spec_runoff_rho(niter), {"vse": rows}, {}


def load_runoff_rho(results_dir=artifacts.RESULTS_DIR, z=Z_95, niter=None):
    payload = artifacts.load("runoff_rho", spec_runoff_rho(niter), results_dir)
    nested = artifacts.from_records(
        payload["data"]["vse"],
        ["baseline", "mode", "runoff_rho", ("label", "chooser")])
    return {"results": {b: {m: {rt: reduce_to_mean_ci(s, z) for rt, s in by_rt.items()}
                            for m, by_rt in by_mode.items()} for b, by_mode in nested.items()},
            "raw_summary": nested, "niter": payload["spec"]["niter"]}


# ---------------------------------------------------------------------------------
# Stage 5 -- section 21: the same question as a chance to learn
# ---------------------------------------------------------------------------------

def spec_runoff_learn(niter=None):
    return _base_spec(niter=cfg.RUNOFF_SWEEP_NITER if niter is None else niter,
                      baselines=list(cfg.RUNOFF_BASELINE_NAMES),
                      kappa_values=[float(k) for k in cfg.RUNOFF_KAPPA_VALUES],
                      variants={k: v for k, v in cfg.RUNOFF_T_FIXED_VARIANTS_MAIN.items()},
                      methods=list(cfg.RUNOFF_LEARN_METHOD_FACTORIES),
                      paired_baseline="STAR")


def run_runoff_learn(niter=None, use_cache=True):
    niter = cfg.RUNOFF_SWEEP_NITER if niter is None else niter
    data = {"vse": [], "paired_diff": [], "baseline": []}
    for baseline in cfg.RUNOFF_BASELINE_NAMES:
        pool = electorates.pool(f"runoff/{baseline}", niter, use_cache=use_cache)
        for variant, rho_fixed in cfg.RUNOFF_T_FIXED_VARIANTS_MAIN.items():
            seed_simulation("runoff_learn", baseline, variant)
            raw = {}
            sweeps.sweep_runoff_learn(
                cfg.RUNOFF_LEARN_METHOD_FACTORIES, cfg.RUNOFF_KAPPA_VALUES,
                cfg.JOINT_SCENARIOS[baseline], niter, rho_fixed, electorates=pool,
                paired_baseline=("STAR", cfg.METHODS_LOOKUP["STAR"]), raw_summary_sink=raw)
            key = {"baseline": baseline, "variant": variant}
            data["vse"] += [{**key, **r} for r in artifacts.to_records(
                raw["vse"], ["kappa", ("label", "chooser")])]
            data["paired_diff"] += [{**key, **r} for r in artifacts.to_records(
                {k: {"_": v} for k, v in raw["paired_diff"].items()}, ["kappa", "pair"])]
            data["baseline"].append({**key, **artifacts._leaf_to_fields(raw["baseline"])})
    return spec_runoff_learn(niter), data, {}


def load_runoff_learn(results_dir=artifacts.RESULTS_DIR, z=Z_95, niter=None):
    payload = artifacts.load("runoff_learn", spec_runoff_learn(niter), results_dir)
    d = payload["data"]
    vse = artifacts.from_records(d["vse"], ["baseline", "variant", "kappa", ("label", "chooser")])
    pdf = artifacts.from_records(d["paired_diff"], ["baseline", "variant", "kappa", "pair"])
    base = artifacts.from_records(d["baseline"], ["baseline", "variant"])
    return {
        "results": {b: {v: {k: reduce_to_mean_ci(s, z) for k, s in by_k.items()}
                        for v, by_k in by_v.items()} for b, by_v in vse.items()},
        "paired_diff": {b: {v: {k: reduce_to_mean_ci({"_": s["_"]}, z)["_"] for k, s in by_k.items()}
                            for v, by_k in by_v.items()} for b, by_v in pdf.items()},
        "baseline": {b: {v: reduce_to_mean_ci({"_": s}, z)["_"] for v, s in by_v.items()}
                     for b, by_v in base.items()},
        "raw_summary": vse,
        "niter": payload["spec"]["niter"],
    }


# ---------------------------------------------------------------------------------
# Stage 6 -- section 24: an Ideal-only Plurality-family run over the joint pool
# ---------------------------------------------------------------------------------

PLURALITY_FAMILY = ["Plurality", "Plurality Top-2", "Plurality Top-2 (Clear-Eyed)"]


def spec_plurality_ideal(niter=None):
    return _base_spec(niter=cfg.JOINT_NITER if niter is None else niter, labels=list(PLURALITY_FAMILY), pool_id="joint")


def run_plurality_ideal(niter=None, use_cache=True):
    """Ideal, over the SAME pool as `joint`, so section 24's paired table is index-aligned."""
    niter = cfg.JOINT_NITER if niter is None else niter
    pool = electorates.pool("joint", niter, use_cache=use_cache)
    seed_simulation("plurality_ideal")
    raw_vse = defaultdict(list)
    summary, ce_raw, _, _ = run_vse_simulation(
        cfg.MODEL, [(l, cfg.METHODS_LOOKUP[l]) for l in PLURALITY_FAMILY],
        cfg.NVOT, cfg.NCAND, niter, cfg.CHOOSER_FUNS, cfg.MEDIA,
        electorates=pool, honest_only=True, raw_vse_sink=raw_vse)
    wins, cw_exists = _ce_sections(ce_raw)
    data = {"vse": artifacts.to_records(summary, LEVELS["vse"]),
            "ce_wins": wins, "ce_denominator": [{"cw_exists": cw_exists}]}
    arrays = {f"{label}||{chooser}": np.asarray(vals, dtype=np.float64)
              for (label, chooser), vals in raw_vse.items()}
    return spec_plurality_ideal(niter), data, arrays


def load_plurality_ideal(results_dir=artifacts.RESULTS_DIR, z=Z_95, niter=None):
    payload = artifacts.load("plurality_ideal", spec_plurality_ideal(niter), results_dir)
    summary = artifacts.from_records(payload["data"]["vse"], LEVELS["vse"])
    return {"raw_summary": summary, "results": reduce_to_mean_ci(summary, z),
            "raw_vse": _load_arrays("plurality_ideal", results_dir),
            "niter": payload["spec"]["niter"]}


# ---------------------------------------------------------------------------------
# Stage 7 -- section 25: Approval Top-2 vs Plurality Top-2 by candidate count
# ---------------------------------------------------------------------------------

def spec_ncand(niter=None):
    return _base_spec(niter=cfg.NCAND_SWEEP_NITER if niter is None else niter, ncand_values=list(cfg.NCAND_VALUES),
                      labels=list(cfg.NCAND_SWEEP_LABELS),
                      scenarios=cfg.JOINT_SCENARIOS)


def run_ncand(niter=None, use_cache=True):
    """One pool per candidate count, shared across all four scenarios (common random numbers)."""
    niter = cfg.NCAND_SWEEP_NITER if niter is None else niter
    by_ncand = {n: electorates.pool(f"ncand/{n}", niter, ncand=n, use_cache=use_cache)
                for n in cfg.NCAND_VALUES}
    seed_simulation("ncand")
    raw = {}
    sweeps.run_ncand_under_joint_scenarios(
        cfg.NCAND_SWEEP_LABELS, cfg.NCAND_VALUES, niter,
        paired_diff_pairs=[("Approval Top-2", "Plurality Top-2")],
        electorates_by_ncand=by_ncand, raw_summary_sink=raw)
    data = {k: [] for k in ("vse", "paired_diff", "ce_wins", "ce_denominator")}
    for scenario, by_ncand_raw in raw.items():
        for ncand, parts in by_ncand_raw.items():
            key = {"scenario": scenario, "ncand": ncand}
            data["vse"] += [{**key, **r} for r in artifacts.to_records(parts["vse"], LEVELS["vse"])]
            data["paired_diff"] += [{**key, **r} for r in artifacts.to_records(
                parts["paired_diff"], LEVELS["paired_diff"])]
            wins, cw_exists = _ce_sections(parts["ce"])
            data["ce_wins"] += [{**key, **r} for r in wins]
            data["ce_denominator"].append({**key, "cw_exists": cw_exists})
    return spec_ncand(niter), data, {}


def load_ncand(results_dir=artifacts.RESULTS_DIR, z=Z_95, niter=None):
    payload = artifacts.load("ncand", spec_ncand(niter), results_dir)
    d = payload["data"]
    vse = artifacts.from_records(d["vse"], ["scenario", "ncand", ("label", "chooser")])
    wins = artifacts.from_records(d["ce_wins"], ["scenario", "ncand", ("label", "chooser")], scalar_name="cw_wins")
    denom = {(r["scenario"], r["ncand"]): r["cw_exists"] for r in d["ce_denominator"]}
    results = {s: {n: reduce_to_mean_ci(v, z) for n, v in by_n.items()} for s, by_n in vse.items()}
    return {
        "results": results,
        "ce": {s: {n: reduce_to_ce((denom[(s, n)], wins[s][n]), results[s][n].keys())
                   for n in wins[s]} for s in wins},
        "paired_diff": {s: {n: reduce_to_mean_ci(v, z) for n, v in by_n.items()}
                        for s, by_n in artifacts.from_records(
                            d["paired_diff"], ["scenario", "ncand", ("label", "baseline")]).items()},
        "raw_summary": vse,
        "niter": payload["spec"]["niter"],
    }


# ---------------------------------------------------------------------------------
# Per-election arrays
# ---------------------------------------------------------------------------------

def arrays_path(stage, results_dir=artifacts.RESULTS_DIR):
    return pathlib.Path(results_dir) / f"{stage}_raw_vse.npz"


def _save_arrays(stage, arrays, results_dir=artifacts.RESULTS_DIR):
    if not arrays:
        return None
    path = arrays_path(stage, results_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path, **arrays)
    return path


def _load_arrays(stage, results_dir=artifacts.RESULTS_DIR, depth=2):
    """Per-election VSE, keyed back into the tuple keys the notebook uses.

    Two places need the individual elections rather than their moments: section 26's
    histograms (which report an empirical mode and a negative-value fraction) and section
    24's paired Ideal-vs-friction table (which counts how many individual elections got
    better or worse). Everything else reads accumulators.
    """
    path = arrays_path(stage, results_dir)
    if not path.exists():
        return {}
    with np.load(path) as handle:
        out = {}
        for name in handle.files:
            parts = name.split("||")
            if depth == 3:
                scenario, label, chooser = parts
                out.setdefault(scenario, {})[(label, chooser)] = list(handle[name])
            else:
                out[(parts[0], parts[1])] = list(handle[name])
    return out


# ---------------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------------

class Stage:
    def __init__(self, name, section, spec, run, load, enabled=True):
        self.name, self.section = name, section
        self.spec, self.run, self.load = spec, run, load
        self.enabled = enabled

    def __repr__(self):
        return f"<Stage {self.name} (section {self.section})>"


STAGES = {s.name: s for s in [
    Stage("ideal", 9, spec_ideal, run_ideal, load_ideal),
    Stage("sweeps", 13, spec_sweeps, run_sweeps, load_sweeps),
    Stage("joint", 16, spec_joint, run_joint, load_joint),
    Stage("runoff_rho", 21, spec_runoff_rho, run_runoff_rho, load_runoff_rho),
    Stage("runoff_learn", 21, spec_runoff_learn, run_runoff_learn, load_runoff_learn),
    Stage("plurality_ideal", 24, spec_plurality_ideal, run_plurality_ideal, load_plurality_ideal),
    Stage("ncand", 25, spec_ncand, run_ncand, load_ncand),
]}

# The order stages run in. `ideal` first only so a failure shows up on the cheapest stage;
# nothing here depends on anything before it.
ORDER = ["ideal", "sweeps", "joint", "plurality_ideal", "runoff_rho", "runoff_learn", "ncand"]


def run_stage(name, results_dir=artifacts.RESULTS_DIR, niter=None, use_cache=True, write=True):
    """Run one stage and (by default) write its results. Returns (payload_path, seconds)."""
    stage = STAGES[name]
    started = time.time()
    spec, data, arrays = stage.run(niter=niter, use_cache=use_cache)
    elapsed = time.time() - started
    if not write:
        return (spec, data, arrays), elapsed
    path = artifacts.write(name, spec, data, results_dir)
    _save_arrays(name, arrays, results_dir)
    return path, elapsed
