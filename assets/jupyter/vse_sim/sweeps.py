"""Drivers that run `engine.run_vse_simulation` across a parameter grid (sections
13, 16, 21 and 25 of `vse_simulation.ipynb`, cells 60, 73, 105, 111 and 166).

Every function here takes an optional `electorates` pool and passes it straight through,
so each point on a sweep sees the SAME underlying worlds under different assumptions
(common random numbers) rather than independently-drawn ones. `stages.py` supplies those
pools from `electorates.py`'s cache.

Rendering lives in `render/`; nothing in this module draws or displays."""

import time
from collections import defaultdict

import numpy as np

from .config import (CHOOSER_FUNS, JOINT_SCENARIOS, MEDIA, METHODS_LOOKUP, MODEL,
                     NCAND, NVOT)
from .engine import reduce_to_ce, reduce_to_mean_ci, run_vse_simulation
from .friction import apply_participation_friction
from .noise import draw_noise, make_perceived_electorate
from .top2 import ApprovalTop2


# ---- section 13: univariate parameter sweeps (cell 60) ----
def sweep_methods(labels, sweep_param, sweep_values, niter, electorates=None,
                   betrayal_targets=None, betrayal_sink_by_value=None,
                   paired_diff_pairs=None, paired_diff_chooser="honBallot",
                   primary_corruption_sink_by_value=None, **fixed_overrides):
    """Run niter elections per value of sweep_param (one of 'epistemic_rho', 'awareness_alpha',
    'fatigue_beta'), holding the other two parameters at 1.0 (override via fixed_overrides),
    for just the given method labels (resolved against METHODS_LOOKUP). electorates: optional
    shared pool passed straight through to run_vse_simulation -- see its docstring; pass the
    SAME pool across every sweep_param call so all values, across all three parameters, are
    compared against the same underlying worlds (common random numbers).

    betrayal_targets/betrayal_sink_by_value: same convention as run_vse_simulation's own
    betrayal_targets/betrayal_sink (see its docstring), threaded straight through at every swept
    value -- populated as {value: betrayal_sink}, each value's sink built fresh. None (default)
    for either: no extra bookkeeping, no behavior change.

    primary_corruption_sink_by_value: same convention as run_vse_simulation's own
    primary_corruption_sink (see its docstring), threaded straight through at every swept value --
    populated as {value: primary_corruption_sink}, each value's sink built fresh. None (default):
    no extra bookkeeping, no behavior change.

    paired_diff_pairs/paired_diff_chooser: same convention as run_vse_simulation's own
    paired_diff_pairs (see its docstring), threaded straight through at every swept value -- every
    method within one run_vse_simulation call here sees the identical election, so this is a
    genuine paired comparison, not two separate point estimates. Returns a third dict,
    paired_diff_by_value: {value: {(label, baseline_label): (mean, ci)}}. Always returned (empty
    dict per value when paired_diff_pairs is None/empty), so callers can unpack a 3-tuple
    unconditionally -- same convention run_vse_simulation itself uses for paired_diff_summary.

    Returns (results_by_value, ce_by_value, paired_diff_by_value): each {value: {key: ...}}.
    results_by_value holds (mean, ci) VSE pairs; ce_by_value holds raw Condorcet efficiency.
    """
    methods_subset = [(label, METHODS_LOOKUP[label]) for label in labels]
    base_kwargs = dict(epistemic_rho=1.0, awareness_alpha=1.0, fatigue_beta=1.0)
    base_kwargs.update(fixed_overrides)
    results_by_value = {}
    ce_by_value = {}
    paired_diff_by_value = {}
    for value in sweep_values:
        kwargs = dict(base_kwargs)
        kwargs[sweep_param] = value
        value_betrayal_sink = {} if betrayal_sink_by_value is not None else None
        value_primary_corruption_sink = {} if primary_corruption_sink_by_value is not None else None
        summary, ce_raw, paired_diff_raw, _ = run_vse_simulation(MODEL, methods_subset, NVOT, NCAND, niter,
                                      CHOOSER_FUNS, MEDIA, electorates=electorates,
                                      betrayal_targets=betrayal_targets, betrayal_sink=value_betrayal_sink,
                                      paired_diff_pairs=paired_diff_pairs, paired_diff_chooser=paired_diff_chooser,
                                      primary_corruption_sink=value_primary_corruption_sink,
                                      **kwargs)
        results_by_value[value] = reduce_to_mean_ci(summary)
        ce_by_value[value] = reduce_to_ce(ce_raw, results_by_value[value].keys())
        paired_diff_by_value[value] = reduce_to_mean_ci(paired_diff_raw)
        if betrayal_sink_by_value is not None:
            betrayal_sink_by_value[value] = value_betrayal_sink
        if primary_corruption_sink_by_value is not None:
            primary_corruption_sink_by_value[value] = value_primary_corruption_sink
        print(f"{sweep_param}={value:.2f} done")
    return results_by_value, ce_by_value, paired_diff_by_value


# ---- section 16: joint 'realistic conditions' scenarios (cell 73) ----


def run_joint_scenarios(labels, scenarios, niter, electorates=None, paired_diff_pairs=None,
                         paired_ce_pairs=None, raw_vse_by_scenario=None,
                         betrayal_targets=None, betrayal_sink_by_scenario=None,
                         coma_targets=None, coma_sink_by_scenario=None,
                         primary_corruption_sink_by_scenario=None,
                         primary_cost_targets=None, primary_cost_sink_by_scenario=None):
    """scenarios: {scenario_name: {epistemic_rho, awareness_alpha, fatigue_beta}} (missing keys default
    to 1.0). electorates: optional shared pool passed straight through to run_vse_simulation --
    see its docstring; pass the SAME pool to every scenario so they're all compared against the
    same underlying worlds (common random numbers). Returns (results_by_scenario,
    ce_by_scenario, paired_diff_by_scenario, paired_ce_by_scenario), each
    {scenario_name: {(label, chooser): ...}} (or {scenario_name: {(label, baseline_label): ...}}
    for paired_diff_by_scenario/paired_ce_by_scenario) -- same shape sweep_methods returns, just
    keyed by scenario name instead of a swept parameter value. results_by_scenario holds
    (mean, ci) VSE pairs; ce_by_scenario holds raw Condorcet efficiency (checkpoint-4 addition);
    paired_diff_by_scenario holds (mean, ci) for the paired per-election (VSE[label] -
    VSE[baseline_label]) difference (honBallot only) for every pair in paired_diff_pairs;
    paired_ce_by_scenario holds (mean, ci) for the paired per-election (CW-hit[label] -
    CW-hit[baseline_label]) difference for every pair in paired_ce_pairs -- both empty per
    scenario when the corresponding pairs arg is None/empty -- see run_vse_simulation's own
    docstring for what "paired" means here.

    raw_vse_by_scenario: optional dict the caller pre-creates (e.g. {}); when given, populated
    as {scenario_name: {(label, chooser): [per-election vse, ...]}} -- same raw per-election
    values run_vse_simulation's own raw_vse_sink collects, just threaded through per scenario.
    Feeds Section 26's per-election VSE histograms. None (default): no extra bookkeeping.

    betrayal_targets/betrayal_sink_by_scenario, coma_targets/coma_sink_by_scenario: same
    convention as raw_vse_by_scenario above, threaded straight through to each scenario's
    run_vse_simulation call -- see its betrayal_targets/coma_targets docstring. Populated as
    {scenario_name: betrayal_sink} / {scenario_name: coma_sink}, each scenario's sink built fresh
    (a plain {} passed as run_vse_simulation's own betrayal_sink/coma_sink for that scenario).
    None (default) for either: no extra bookkeeping, no behavior change.

    primary_corruption_sink_by_scenario: same convention as raw_vse_by_scenario/
    betrayal_sink_by_scenario above, threaded straight through to each scenario's
    run_vse_simulation call -- see its primary_corruption_sink docstring. Populated as
    {scenario_name: primary_corruption_sink}. None (default): no extra bookkeeping.

    primary_cost_targets/primary_cost_sink_by_scenario: same convention as
    betrayal_targets/betrayal_sink_by_scenario above, threaded straight through to each
    scenario's run_vse_simulation call -- see its primary_cost_targets docstring. Populated
    as {scenario_name: primary_cost_sink}. None (default) for either: no extra bookkeeping.

    Always runs with honest_only=True -- nothing downstream of this function (every joint-
    scenario table/chart) ever reads a non-honBallot chooser, so the strategic/one-sided/
    smart-one-sided ballots aren't computed at all here."""
    function_start_time = time.time()
    methods_subset = [(label, METHODS_LOOKUP[label]) for label in labels]
    results_by_scenario = {}
    ce_by_scenario = {}
    paired_diff_by_scenario = {}
    paired_ce_by_scenario = {}
    for name, params in scenarios.items():
        scenario_start_time = time.time()
        print(f"Running scenario '{name}' ({params}) ...")
        kwargs = dict(epistemic_rho=1.0, awareness_alpha=1.0, fatigue_beta=1.0)
        kwargs.update(params)
        raw_sink = defaultdict(list) if raw_vse_by_scenario is not None else None
        scenario_betrayal_sink = {} if betrayal_sink_by_scenario is not None else None
        scenario_coma_sink = {} if coma_sink_by_scenario is not None else None
        scenario_primary_corruption_sink = {} if primary_corruption_sink_by_scenario is not None else None
        scenario_primary_cost_sink = {} if primary_cost_sink_by_scenario is not None else None
        summary, ce_raw, paired_diff_raw, paired_ce_raw = run_vse_simulation(
            MODEL, methods_subset, NVOT, NCAND, niter, CHOOSER_FUNS, MEDIA,
            electorates=electorates, paired_diff_pairs=paired_diff_pairs,
            paired_ce_pairs=paired_ce_pairs, raw_vse_sink=raw_sink, honest_only=True,
            betrayal_targets=betrayal_targets, betrayal_sink=scenario_betrayal_sink,
            coma_targets=coma_targets, coma_sink=scenario_coma_sink,
            primary_corruption_sink=scenario_primary_corruption_sink,
            primary_cost_targets=primary_cost_targets, primary_cost_sink=scenario_primary_cost_sink, **kwargs
        )
        results_by_scenario[name] = reduce_to_mean_ci(summary)
        ce_by_scenario[name] = reduce_to_ce(ce_raw, results_by_scenario[name].keys())
        paired_diff_by_scenario[name] = reduce_to_mean_ci(paired_diff_raw)
        paired_ce_by_scenario[name] = reduce_to_mean_ci(paired_ce_raw)
        if raw_vse_by_scenario is not None:
            raw_vse_by_scenario[name] = dict(raw_sink)
        if betrayal_sink_by_scenario is not None:
            betrayal_sink_by_scenario[name] = scenario_betrayal_sink
        if coma_sink_by_scenario is not None:
            coma_sink_by_scenario[name] = scenario_coma_sink
        if primary_corruption_sink_by_scenario is not None:
            primary_corruption_sink_by_scenario[name] = scenario_primary_corruption_sink
        if primary_cost_sink_by_scenario is not None:
            primary_cost_sink_by_scenario[name] = scenario_primary_cost_sink
        print(f"{name} done in {time.time() - scenario_start_time:.1f}s")
    print(f"Total time: {time.time() - function_start_time:.1f}s")
    return results_by_scenario, ce_by_scenario, paired_diff_by_scenario, paired_ce_by_scenario


# ---- section 21: runoff information sweeps (cells 105 and 111) ----
def sweep_runoff_rho(method_factories, runoff_rho_values, primary_params, niter, awareness_modes,
                    electorates=None):
    """method_factories: {label: factory(runoff_rho, runoff_awareness_alpha) -> fresh method instance}.
    primary_params: epistemic_rho/awareness_alpha/fatigue_beta held FIXED for the primary. awareness_modes:
    {mode_name: (rt -> runoff_awareness_alpha)} -- ALL modes evaluated together, sharing the SAME
    primary electorate per election, rather than each mode drawing its own independent batch.
    This extends the paired-comparison (common-random-numbers) design already used for
    methods/runoff_rho to the awareness-mode axis too: the 2 awareness modes for a given baseline
    share identical primary_params (only the runoff differs between them), so there's no reason
    to redraw niter primary electorates per mode when niter total already covers both -- cuts
    primary-electorate draws from niter * len(awareness_modes) down to niter.

    Each election also draws ONE noise sample (draw_noise) that's reused across EVERY swept
    runoff_rho value for that election (via each method instance's _runoff_noise) -- so runoff_rho
    varies only the rho-weighting applied to the SAME underlying misperception, not an unrelated
    fresh draw at every point. This is what makes the runoff_rho axis itself a genuine paired sweep,
    not just the primary electorate.

    electorates: optional shared pool (same convention as sweep_methods/run_joint_scenarios) --
    pass the SAME pool used elsewhere at this baseline (e.g. the kappa sweep below) so
    every sweep at a given baseline compares against identical underlying elections instead of
    each drawing its own independent batch.

    Returns {mode_name: {runoff_rho: {(label, chooser): (mean, ci)}}}.
    """
    sweep_start_time = time.time()
    epistemic_rho = primary_params.get("epistemic_rho", 1.0)
    awareness_alpha = primary_params.get("awareness_alpha", 1.0)
    fatigue_beta = primary_params.get("fatigue_beta", 1.0)
    summary = {mode_name: {rt: defaultdict(lambda: [0, 0.0, 0.0]) for rt in runoff_rho_values}
               for mode_name in awareness_modes}
    for i in range(niter):
        true_electorate = electorates[i] if electorates is not None else MODEL(NVOT, NCAND)
        election_noise = draw_noise(true_electorate)  # shared across every runoff_rho below
        perceived_electorate = make_perceived_electorate(true_electorate, epistemic_rho, noise=election_noise)
        ballot_electorate, _, _ = apply_participation_friction(
            perceived_electorate, true_electorate, awareness_alpha, fatigue_beta
        )  # this sweep's methods (Top2 variants) never feed Irv, so discard genuine_sets/aware_sets
        for mode_name, awareness_for_rt in awareness_modes.items():
            for label, factory in method_factories.items():
                for rt in runoff_rho_values:
                    _method = factory(rt, awareness_for_rt(rt))
                    if rt is not None:
                        # Same z as the primary's own perceived_electorate -- isolates "how does
                        # runoff_rho alone change things" from "what if we'd drawn different noise".
                        _method._runoff_noise = election_noise
                    for row in _method.resultsTable(
                        i, str(MODEL), NCAND, ballot_electorate, CHOOSER_FUNS,
                        media=MEDIA, scoring_voters=true_electorate, perceived_voters=perceived_electorate,
                        honest_only=True,
                    ):
                        acc = summary[mode_name][rt][(label, row["chooser"])]
                        acc[0] += 1
                        acc[1] += row["vse"]
                        acc[2] += row["vse"] ** 2
        if (i + 1) % 100 == 0:
            print(f"{i + 1}/{niter} elections done in {time.time() - sweep_start_time:.1f}s")
    return {mode_name: {rt: reduce_to_mean_ci(dict(summary[mode_name][rt])) for rt in runoff_rho_values}
            for mode_name in awareness_modes}


def sweep_runoff_learn(method_factories, learn_kappa_values, primary_params, niter,
                        runoff_rho_fixed, electorates=None, paired_baseline=None):
    """Like sweep_runoff_rho, but holds runoff_rho FIXED at runoff_rho_fixed for every point and
    sweeps runoff_kappa instead -- isolates the "chance to learn" axis alone, holding the
    runoff's own epistemic-noise level constant throughout. At each swept point, a voter unaware
    of a given finalist in the primary gets one independent Bernoulli(runoff_kappa) roll to
    become aware of THAT finalist by runoff day (see Top2Base._runoff_electorate's
    runoff_kappa branch above). runoff_kappa=0.0 is an exact match for Coma; runoff_kappa=
    1.0 is an exact match for Groggy -- not approximations. runoff_rho_fixed=None reuses the
    primary's own (possibly noisy) epistemic level for the runoff; runoff_rho_fixed=1.0 gives the
    runoff perfect epistemic information regardless of learning. electorates: optional shared
    pool, same convention as sweep_runoff_rho/sweep_methods.

    paired_baseline: optional (label, method) pair, e.g. ("STAR", METHODS_LOOKUP["STAR"]) --
    evaluated ONCE per election (not once per swept kappa, since STAR's own automatic runoff doesn't
    depend on AT2's runoff_kappa axis at all), on the SAME ballot_electorate/perceived_electorate
    every swept (label, kappa) combination sees that election -- a genuine paired comparison, not an
    independent-samples one (unlike combining this sweep's own CI with a DIFFERENT electorate
    pool's CI, e.g. joint_results). Tracks the baseline's own (mean, ci) too, not just the diff,
    so a caller can display a self-consistent AT2/baseline/gap table computed from one shared set
    of elections. Returns (results_by_kappa, paired_diff_by_kappa, baseline_mean_ci) -- paired_diff_by_kappa
    empty and baseline_mean_ci None when paired_baseline isn't given.

    Returns (results_by_kappa, paired_diff_by_kappa, baseline_mean_ci); results_by_kappa is
    {runoff_kappa: {(label, chooser): (mean, ci)}}.
    """
    sweep_start_time = time.time()
    epistemic_rho = primary_params.get("epistemic_rho", 1.0)
    awareness_alpha = primary_params.get("awareness_alpha", 1.0)
    fatigue_beta = primary_params.get("fatigue_beta", 1.0)
    summary = {kappa: defaultdict(lambda: [0, 0.0, 0.0]) for kappa in learn_kappa_values}
    paired_diff_summary = {kappa: [0, 0.0, 0.0] for kappa in learn_kappa_values}
    baseline_summary = [0, 0.0, 0.0]
    baseline_label, baseline_method = paired_baseline if paired_baseline else (None, None)
    for i in range(niter):
        true_electorate = electorates[i] if electorates is not None else MODEL(NVOT, NCAND)
        perceived_electorate = make_perceived_electorate(true_electorate, epistemic_rho)
        ballot_electorate, _, aware_sets = apply_participation_friction(
            perceived_electorate, true_electorate, awareness_alpha, fatigue_beta
        )  # aware_sets IS needed here (unlike sweep_runoff_rho/the old sweep_runoff_awareness) --
           # runoff_kappa reads self._aware_sets, so it must be threaded through below.
        baseline_vse = None
        if baseline_method is not None:
            baseline_row = next(
                r for r in baseline_method.resultsTable(
                    i, str(MODEL), NCAND, ballot_electorate, [],
                    media=MEDIA, scoring_voters=true_electorate, perceived_voters=perceived_electorate,
                    honest_only=True,
                ) if r["chooser"] == "honBallot"
            )
            baseline_vse = baseline_row["vse"]
            baseline_summary[0] += 1
            baseline_summary[1] += baseline_vse
            baseline_summary[2] += baseline_vse ** 2
        for label, factory in method_factories.items():
            for kappa in learn_kappa_values:
                for row in factory(runoff_rho_fixed, kappa).resultsTable(
                    i, str(MODEL), NCAND, ballot_electorate, CHOOSER_FUNS,
                    media=MEDIA, scoring_voters=true_electorate, perceived_voters=perceived_electorate,
                    aware_sets=aware_sets, honest_only=True,
                ):
                    acc = summary[kappa][(label, row["chooser"])]
                    acc[0] += 1
                    acc[1] += row["vse"]
                    acc[2] += row["vse"] ** 2
                    if baseline_vse is not None and row["chooser"] == "honBallot":
                        dacc = paired_diff_summary[kappa]
                        d = row["vse"] - baseline_vse
                        dacc[0] += 1
                        dacc[1] += d
                        dacc[2] += d ** 2
        if (i + 1) % 100 == 0:
            print(f"{i + 1}/{niter} elections done in {time.time() - sweep_start_time:.1f}s")
    results_by_kappa = {kappa: reduce_to_mean_ci(dict(summary[kappa])) for kappa in learn_kappa_values}
    paired_diff_by_kappa = (
        {kappa: reduce_to_mean_ci({"_": paired_diff_summary[kappa]})["_"] for kappa in learn_kappa_values}
        if paired_baseline else {}
    )
    baseline_mean_ci = reduce_to_mean_ci({"_": baseline_summary})["_"] if paired_baseline else None
    return results_by_kappa, paired_diff_by_kappa, baseline_mean_ci


# ---- section 25: candidate-count sweep (cell 166) ----
def sweep_ncand(labels, ncand_values, niter, friction_params=None, electorates_by_ncand=None,
                 paired_diff_pairs=None):
    """Run niter elections per value of ncand, holding friction fixed.

    friction_params defaults to Ideal if omitted.
    electorates_by_ncand: optional {ncand: [true_electorates...]} pool for CRN reuse.
    paired_diff_pairs: optional list of (label, baseline_label) pairs -- see run_vse_simulation's
      own docstring; passed straight through so callers get a genuine paired VSE-gap CI (not an
      approximated one) at every ncand value, same convention as Section 16.
    Returns (results_by_ncand, ce_by_ncand, paired_diff_by_ncand).
    """
    start_time = time.time()
    methods_subset = [(label, METHODS_LOOKUP[label]) for label in labels]
    kwargs = dict(epistemic_rho=1.0, awareness_alpha=1.0, fatigue_beta=1.0)
    kwargs.update(friction_params or {})
    required_labels = {"Approval Top-2", "Plurality Top-2"}
    missing_labels = sorted(required_labels - set(labels))
    if missing_labels:
        raise ValueError(
            "AT2 vs PT2 paired-gap CI needs both labels present. "
            f"Missing: {', '.join(missing_labels)}"
        )

    # Keep friction args strict so typos don't silently pass through.
    valid_friction_keys = {"epistemic_rho", "awareness_alpha", "fatigue_beta"}
    extra_keys = set((friction_params or {}).keys()) - valid_friction_keys
    if extra_keys:
        raise ValueError(f"Unknown friction_params keys: {sorted(extra_keys)}")
    results_by_ncand = {}
    ce_by_ncand = {}
    paired_diff_by_ncand = {}

    for ncand in ncand_values:
        start_time_ncand = time.time()
        electorates = None if electorates_by_ncand is None else electorates_by_ncand[ncand]
        summary, ce_raw, paired_diff_raw, _paired_ce_raw = run_vse_simulation(
            MODEL,
            methods_subset,
            NVOT,
            ncand,
            niter,
            CHOOSER_FUNS,
            MEDIA,
            electorates=electorates,
            paired_diff_pairs=paired_diff_pairs,
            honest_only=True,
            **kwargs,
        )
        results_by_ncand[ncand] = reduce_to_mean_ci(summary)
        ce_by_ncand[ncand] = reduce_to_ce(ce_raw, results_by_ncand[ncand].keys())
        paired_diff_by_ncand[ncand] = reduce_to_mean_ci(paired_diff_raw)
        print(f"ncand={ncand} done in {time.time() - start_time_ncand:.1f}s (total elapsed: {time.time() - start_time:.1f}s)")

    return results_by_ncand, ce_by_ncand, paired_diff_by_ncand


def run_ncand_under_joint_scenarios(
    labels,
    ncand_values,
    niter,
    scenarios=None,
    use_common_random_numbers=True,
    paired_diff_pairs=None,
):
    """Run sweep_ncand across all joint friction scenarios.

    Returns:
      results_by_scenario: {scenario_name: {ncand: {(label, chooser): (mean, ci)}}}
      ce_by_scenario:      {scenario_name: {ncand: {(label, chooser): raw_ce}}}
      paired_diff_by_scenario: {scenario_name: {ncand: {(label, baseline_label): (mean, ci)}}}
    """
    scenarios = JOINT_SCENARIOS if scenarios is None else scenarios

    electorates_by_ncand = None
    if use_common_random_numbers:
        electorates_by_ncand = {
            ncand: [MODEL(NVOT, ncand) for _ in range(niter)]
            for ncand in ncand_values
        }

    results_by_scenario = {}
    ce_by_scenario = {}
    paired_diff_by_scenario = {}

    for scenario_name, params in scenarios.items():
        print(f"{scenario_name}:")
        r_ncand, ce_ncand, paired_diff_ncand = sweep_ncand(
            labels,
            ncand_values,
            niter,
            friction_params=params,
            electorates_by_ncand=electorates_by_ncand,
            paired_diff_pairs=paired_diff_pairs,
        )
        results_by_scenario[scenario_name] = r_ncand
        ce_by_scenario[scenario_name] = ce_ncand
        paired_diff_by_scenario[scenario_name] = paired_diff_ncand

    return results_by_scenario, ce_by_scenario, paired_diff_by_scenario
