"""The loaded results, under the names the notebook uses.

Every render function needs some slice of the simulation output, and threading a dozen
structures through each call site would bury the one line that actually draws something.
So the notebook loads once into a `Results`, calls `use()`, and the helpers read it back
with `current()`.

This is a module-level global, which is the thing `SignificanceLog` exists to avoid -- but
the two are different in the way that matters. This one is written once, at the top of the
notebook, and is read-only afterwards; the significance log is appended to by cells
scattered through the document and then read by a section that depends on all of them
having run. An order-dependent accumulator needs a completeness check. A constant does not."""

from dataclasses import dataclass, field

from .. import config as cfg, stages
from ..engine import relative_ce
from .significance import SignificanceLog


@dataclass
class Results:
    """Everything the stages produced, reassembled the way the notebook expects it.

    The field names are the notebook's own (`results`, `joint_results`,
    `paired_diff_by_scenario`, ...) so a cell that was reading a global still reads the
    same thing, just off this object.
    """
    ideal: dict
    sweeps: dict
    joint: dict
    runoff_rho: dict
    runoff_learn: dict
    plurality_ideal: dict
    ncand: dict
    z: float = 1.96
    significance: SignificanceLog = field(default_factory=SignificanceLog)

    # -- section 9 ---------------------------------------------------------------
    @property
    def results(self):
        return self.ideal["results"]

    @property
    def ce_results(self):
        return self.ideal["ce_results"]

    @property
    def rel_ce_results(self):
        return relative_ce(self.ce_results)

    @property
    def ideal_paired_diff(self):
        return self.ideal["paired_diff"]

    @property
    def ideal_paired_ce(self):
        return self.ideal["paired_ce"]

    # -- section 16 --------------------------------------------------------------
    @property
    def joint_results(self):
        return self.joint["results"]

    @property
    def joint_ce_results(self):
        return self.joint["ce"]

    @property
    def paired_diff_by_scenario(self):
        return self.joint["paired_diff"]

    @property
    def paired_ce_by_scenario(self):
        return self.joint["paired_ce"]

    @property
    def joint_raw_vse_by_scenario(self):
        return self.joint["raw_vse"]

    @property
    def scenario_names(self):
        return list(cfg.JOINT_SCENARIOS)

    # -- section 13 --------------------------------------------------------------
    @property
    def sweep_results_by_param(self):
        return self.sweeps["results"]

    @property
    def sweep_ce_by_param(self):
        return self.sweeps["ce"]

    @property
    def sweep_paired_diff_by_param(self):
        return self.sweeps["paired_diff"]

    @property
    def primary_corruption_by_value_by_param(self):
        return self.sweeps["primary_corruption"]

    # -- sections 21 and 25 ------------------------------------------------------
    @property
    def runoff_sweep_results(self):
        return self.runoff_rho["results"]

    @property
    def learn_sweep_results(self):
        return self.runoff_learn["results"]

    @property
    def learn_sweep_paired_diff(self):
        return self.runoff_learn["paired_diff"]

    @property
    def learn_sweep_baseline(self):
        return self.runoff_learn["baseline"]

    @property
    def results_by_scenario_ncand(self):
        return self.ncand["results"]

    @property
    def paired_diff_by_scenario_ncand(self):
        return self.ncand["paired_diff"]

    @property
    def total_seconds(self):
        return sum(s["meta"].get("seconds", 0) for s in
                   (self.ideal, self.sweeps, self.joint, self.runoff_rho,
                    self.runoff_learn, self.plurality_ideal, self.ncand))

    @property
    def total_elections(self):
        return sum(s["meta"].get("elections", 0) for s in
                   (self.ideal, self.sweeps, self.joint, self.runoff_rho,
                    self.runoff_learn, self.plurality_ideal, self.ncand))


CURRENT = None


def load(results_dir=None, z=1.96):
    """Read every stage's results and stitch in what the notebook used to graft by hand.

    Cells 46-47 and 76 of the original notebook did three things after the runs finished,
    all reproduced here:

    1. At rho = alpha = beta = 1.0 a Clear-Eyed or Coma runoff variant is mathematically
       identical to its base method -- both mechanisms are exact no-ops there. Simulating
       them as separate entries anyway means each draws from a different position in the
       shared RNG stream for the same election, so a rare exact-tie tie-break can resolve
       differently: a small spurious gap with no cause. The canonical member's numbers are
       copied onto its aliases rather than trusting the separately-simulated ones.
    2. "Ideal" as a joint scenario IS the section 9 run, not a fourth simulation.
    3. Primary-vote corruption at Ideal is zero by construction (every voter is aware of
       every candidate and perceives it correctly), so it is synthesized rather than
       grafted -- section 9 never collected that metric.
    """
    kwargs = {} if results_dir is None else {"results_dir": results_dir}
    R = Results(
        ideal=stages.load_ideal(z=z, **kwargs),
        sweeps=stages.load_sweeps(z=z, **kwargs),
        joint=stages.load_joint(z=z, **kwargs),
        runoff_rho=stages.load_runoff_rho(z=z, **kwargs),
        runoff_learn=stages.load_runoff_learn(z=z, **kwargs),
        plurality_ideal=stages.load_plurality_ideal(z=z, **kwargs),
        ncand=stages.load_ncand(z=z, **kwargs),
        z=z,
    )
    _apply_ideal_aliases(R)
    _graft_ideal_into_joint(R)
    _copy_ideal_into_sweeps(R)
    use(R)
    return R


# Methods that are the same method under no friction, and the entry whose numbers they
# should carry. See load()'s docstring for why this matters.
IDENTICAL_AT_IDEAL = [
    (["Approval Top-2 (Coma)", "Approval Top-2 (Clear-Eyed)"], "Approval Top-2"),
    (["Plurality Top-2 (Clear-Eyed)"], "Plurality Top-2"),
]


def _apply_ideal_aliases(R):
    results, ce, raw, pdiff, pce = (R.ideal["results"], R.ideal["ce_results"],
                                    R.ideal["raw_vse"], R.ideal["paired_diff"],
                                    R.ideal["paired_ce"])
    for aliases, canonical in IDENTICAL_AT_IDEAL:
        for alias in aliases:
            for chooser in {k[1] for k in results if k[0] == canonical}:
                results[(alias, chooser)] = results[(canonical, chooser)]
                if (canonical, chooser) in ce:
                    ce[(alias, chooser)] = ce[(canonical, chooser)]
                if (canonical, chooser) in raw:
                    raw[(alias, chooser)] = raw[(canonical, chooser)]
            for baseline in cfg.COMPARE_LABELS:
                if (canonical, baseline) in pdiff:
                    pdiff[(alias, baseline)] = pdiff[(canonical, baseline)]
                if (canonical, baseline) in pce:
                    pce[(alias, baseline)] = pce[(canonical, baseline)]


def _graft_ideal_into_joint(R):
    keep = set(cfg.COMPARE_LABELS)
    R.joint["results"]["Ideal"] = {k: v for k, v in R.ideal["results"].items() if k[0] in keep}
    R.joint["ce"]["Ideal"] = {k: v for k, v in R.ideal["ce_results"].items() if k[0] in keep}
    R.joint["raw_vse"]["Ideal"] = {k: v for k, v in R.ideal["raw_vse"].items() if k[0] in keep}
    R.joint["paired_diff"]["Ideal"] = R.ideal["paired_diff"]
    R.joint["paired_ce"]["Ideal"] = R.ideal["paired_ce"]
    R.joint["betrayal"]["Ideal"] = R.ideal["betrayal"]
    R.joint["coma"]["Ideal"] = R.ideal["coma"]
    R.joint["primary_cost"]["Ideal"] = R.ideal["primary_cost"]
    niter, nvot = R.joint["niter"], cfg.NVOT
    R.joint["primary_corruption"]["Ideal"] = dict(
        n_elections=niter, n_voters=niter * nvot,
        aligned=niter * nvot, awareness_caused=0, noise_caused=0)


def _copy_ideal_into_sweeps(R):
    """Value 1.0 of every sweep is the Ideal run, at its own higher precision."""
    for param, methods in cfg.SWEEP_PARAMS:
        labels = {label for label, _ in methods}
        R.sweeps["results"][param][1.0] = {k: v for k, v in R.ideal["results"].items()
                                           if k[0] in labels}
        R.sweeps["ce"][param][1.0] = {k: v for k, v in R.ideal["ce_results"].items()
                                      if k[0] in labels}
        R.sweeps["paired_diff"][param][1.0] = {k: v for k, v in R.ideal["paired_diff"].items()
                                               if k[0] in labels}
        R.sweeps["betrayal"][param][1.0] = R.ideal["betrayal"]
        R.sweeps["primary_corruption"][param][1.0] = dict(
            n_elections=R.sweeps["niter"], n_voters=R.sweeps["niter"] * cfg.NVOT,
            aligned=R.sweeps["niter"] * cfg.NVOT, awareness_caused=0, noise_caused=0)


def use(results):
    global CURRENT
    CURRENT = results
    return results


def current():
    if CURRENT is None:
        raise RuntimeError(
            "no results loaded -- call vse_sim.render.context.load() first "
            "(the notebook's setup cell does this).")
    return CURRENT
