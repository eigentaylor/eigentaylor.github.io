"""Every knob, in one place -- section 5 of `vse_simulation.ipynb` and the constant
blocks scattered through the sections after it, gathered here.

This is the single source of truth for what a run *is*. `artifacts.py` hashes the
values below into each result file's `spec`, so changing anything here invalidates
the cached results that depended on it rather than silently re-rendering stale
numbers. Nothing in this module has side effects: importing it seeds no RNG and
runs no election.

Defaults reproduce the **published reference configuration** for the electorate
(101 voters, 6 candidates, the "kitchen sink" hierarchical-cluster model, fuzzy media
noise) with `EPISTEMIC_RHO=1.0` (no epistemic noise).
"""

import numpy as np

from .top2 import ApprovalTop2, PluralityTop2, ScoreTop2
from .vendored.methods.irv import Irv
from .vendored.methods.plurality import Plurality
from .vendored.methods.schulze import Schulze
from .vendored.methods.score import Score
from .vendored.methods.srv import Srv
from .vendored.simulation import baseRuns
from .vendored.strategies import fuzzyMediaFor
from .vendored.voter_models import KSModel

# --------------------------------------------------------------------------
# Core run parameters (notebook section 5)
# --------------------------------------------------------------------------

NVOT = 101            # voters per simulated election
NCAND = 6            # candidates per simulated election
NITER = 5000          # elections to simulate
SEED = "42"            # random seed for reproducibility

# Every other section's own election count, gathered here rather than left scattered across
# the notebook -- this is the one place to look when trading precision off against runtime.
SWEEP_NITER = 2000                # Section 13: the epistemic_rho/awareness_alpha/fatigue_beta sweeps, takes very long to run
SWEEP_VALUES = [0.3, 0.5, 0.7, 0.8, 0.9, 1.0]  # Section 13's sweep grid -- 0.7/0.8/0.9/1.0 match
                                  # the joint-friction scenario values (Heavy/Moderate/Mild/Ideal)
                                  # exactly, so the univariate-sweep and joint-scenario stories read
                                  # off the same grid; 0.3/0.5 add shape context below Heavy.
                                  # Single source of truth -- Section 13, and Section 23's
                                  # by-epistemic_rho/awareness_alpha/fatigue_beta betrayal
                                  # breakdowns, all read this same list rather than each hardcoding
                                  # their own copy.
JOINT_NITER = 6000                # Section 16: joint realistic-conditions scenarios -- only 4 runs total here (vs. Section 13's 18), so we can afford tighter CIs
RUNOFF_RHO_SWEEP_NITER = 2000       # Section 21: runoff_rho sweep -- flatter curve, doesn't need the same precision
RUNOFF_SWEEP_NITER = 4000        # Section 21: runoff learn-sweep + its electorate-pool sizing
SECONDARY_SWEEP_NITER = 100      # Section 21's secondary/curiosity sweep: neither variant there brackets a named runoff model, so it doesn't need the main sections' precision -- reuses the first SECONDARY_SWEEP_NITER elections of the same per-baseline pools (paired with, not independent of, the main runs) rather than drawing a fresh batch.
NCAND_SWEEP_NITER = 1500          # Section 25: Approval Top-2 vs Plurality Top-2 across candidate counts. This takes significant time.

MODEL = KSModel(dcdecay=(1, 3), wcdecay=(1.5, 3), dccut=.2, wcalpha=1.5)  # published "kitchen sink" model
MEDIA = fuzzyMediaFor()   # gaussian noise on polls, as used for all published numbers
DO_STRATEGY_SWEEP = False  # the 25/50/75%-strategic + one-sided chooser battery (baseRuns) is only
                            # needed for the Section 8/9 baseline run below (feeds Section 10's table
                            # and Section 12's chart) -- every sweep/joint-scenario/runoff cell after
                            # that only ever reads honBallot/stratBallot. Stays False except where
                            # Section 9 explicitly brackets its own run with it set True.
CHOOSER_FUNS = baseRuns if DO_STRATEGY_SWEEP else []  # same honest/strategic/one-sided/mixed battery as the published runs, when enabled

EPISTEMIC_RHO = 1.0    # 1.0 = perfect knowledge (no noise); lower = noisier perception of candidates
AWARENESS_ALPHA = 1.0    # 1.0 = everyone knows every candidate; lower = obscure candidates go unnoticed
FATIGUE_BETA = 1.0      # 1.0 = no ballot fatigue; lower = voters give up partway down the ballot

GAP_THRESHOLD_PP = 1.0  # practical-significance bar, in percentage points -- a VSE gap smaller
                         # than this is "Indistinguishable"/"Narrow edge" territory even when
                         # statistically real; used by every "Significant?" column's taxonomy
                         # (see _classify_gap/_verdict_text below Section 16) and Section 29's
                         # niter projection. Single source of truth -- edit here to move the bar
                         # everywhere at once.


# ---------------------------------------------------------------------------
# Methods and their fixed presentation (notebook section 6)
# ---------------------------------------------------------------------------

STAR_TOP_RANK = 5

METHODS = [
    ("Plurality", Plurality()),
    ("Approval", Score(1)),
    ("RCV (IRV)", Irv()),
    ("STAR", Srv(STAR_TOP_RANK)),
    ("Score5", Score(STAR_TOP_RANK)),
    ("Condorcet (Schulze)", Schulze()),
    ("Plurality Top-2", PluralityTop2(runoff_rho=None)),
    ("Plurality Top-2 (Clear-Eyed)", PluralityTop2(runoff_rho=1.0)),
    ("Approval Top-2", ApprovalTop2(runoff_rho=None)),
    ("Approval Top-2 (Coma)", ApprovalTop2(runoff_rho=None, runoff_coma=True)),
    ("Approval Top-2 (Clear-Eyed)", ApprovalTop2(runoff_rho=1.0)),
    ("Score Top-2 (Clear-Eyed)", ScoreTop2(STAR_TOP_RANK, runoff_rho=1.0)),
    # Appended last so existing methods' RNG draws stay bit-identical to the original notebook.
    ("Schulze (equal ranks)", Schulze(quantize=True)),
]

# Fixed per-method colors (a validated colorblind-safe categorical palette -- run
# dataviz's scripts/validate_palette.js against this list before adding more), reused across
# every chart below so a given method's color never changes between figures. The Top-2 hybrid
# family gets its own hue per primary method; each family's clear-eyed-runoff variant reuses
# the SAME hue with a dashed linestyle (see METHOD_LINESTYLES) rather than a separate hue, since
# it's the same underlying method, just a different assumption about the runoff step. "Coma"
# reuses the same hue too, with its own dash-dot linestyle -- a third assumption about the
# runoff, not a separate method family. "Score5" reuses STAR's own hue with a dotted linestyle
# for the same reason -- Srv(STAR_TOP_RANK) subclasses Score(STAR_TOP_RANK), so the two share
# IDENTICAL ballots; "Score5" is that same ballot data with the runoff step switched off, not a
# separate method family (see Section 22). "Score Top-2 (Clear-Eyed)" also reuses Score5's hue
# (same STAR_TOP_RANK ballots, this time WITH a genuine primary+runoff step, Top2Base-style
# rather than STAR's same-ballot runoff -- see Section 3) with the usual Clear-Eyed dash.
METHOD_COLORS = {
    "Plurality": "#2a78d6",
    "Approval": "#eb6834",
    "RCV (IRV)": "#1baf7a",
    "STAR": "#eda100",
    "Score5": "#ecbe5b",
    "Condorcet (Schulze)": "#e87ba4",
    "Schulze (equal ranks)": "#e87ba4",
    "Plurality Top-2": "#008300",
    "Plurality Top-2 (Clear-Eyed)": "#008300",
    "Approval Top-2": "#4a3aa7",
    "Approval Top-2 (Coma)": "#4a3aa7",
    "Approval Top-2 (Clear-Eyed)": "#4a3aa7",
    "Score Top-2 (Clear-Eyed)": "#ecbe5b",
}
METHOD_LINESTYLES = {label: ("--" if "Clear-Eyed" in label else "-") for label, _ in METHODS}
METHOD_LINESTYLES["Score5"] = ":"  # same hue as STAR, dotted to mark "runoff switched off"
METHOD_LINESTYLES["Approval Top-2 (Coma)"] = "-."  # same hue as AT2, dash-dot to mark "coma"
METHOD_LINESTYLES["Schulze (equal ranks)"] = "-."  # same hue as Schulze, dash-dot to mark "equal ranks allowed"

# label -> method instance, for the reusable comparison tooling in Sections 14 onward -- lets any
# comparison pull any of these methods by name without constructing anything new.
METHODS_LOOKUP = dict(METHODS)

# Sections 10-12 run under EPISTEMIC_RHO=AWARENESS_ALPHA=FATIGUE_BETA=1.0, where clear-eyed-runoff
# variants are mathematically identical to their base method (both make_perceived_electorate
# and apply_participation_friction are exact no-ops at rho=1.0/beta=1.0) -- any visible gap in those
# sections is pure random.choice tie-break RNG-ordering artifact, not signal. "Approval Top-2
# (Coma)" is ALSO identical to plain "Approval Top-2" under these same conditions (friction is
# a no-op at awareness_alpha=1.0 regardless of which awareness_alpha value it's applied at), for the
# same reason, so the same tolerance applies to it here. Simulated once regardless (Section 9's
# run is reused as "Ideal" everywhere downstream) -- this only filters what gets plotted before
# noise is actually introduced.
PRE_NOISE_METHODS = [(label, m) for label, m in METHODS if "Clear-Eyed" not in label]


# ---------------------------------------------------------------------------
# Which methods get compared, and against what (notebook section 8)
# ---------------------------------------------------------------------------

# Hoisted here (rather than down near Section 13's compare_by_param, where this list used to
# live) so Section 9's baseline run below AND Section 16's joint-scenario run can both build
# their paired-comparison lists (PAIRED_DIFF_PAIRS/PAIRED_CE_PAIRS, just below) from this SAME
# list -- single source of truth for which methods get compared, instead of Section 9 pinning
# its own narrower STAR-only pairs. compare_by_param (Section 13.5) uses this same COMPARE_LABELS
# again once those sweeps exist.
COMPARE_LABELS = ["Plurality", "Plurality Top-2", "Plurality Top-2 (Clear-Eyed)", "RCV (IRV)", "Approval", "Approval Top-2 (Coma)", "Approval Top-2",
                   "Approval Top-2 (Clear-Eyed)", "STAR", "Score5", "Score Top-2 (Clear-Eyed)", "Condorcet (Schulze)", "Schulze (equal ranks)"]


# Every COMPARE_LABELS method gets its usual diff-vs-STAR (feeds Section 18's "Quantifying the
# swing" tables below); RCV/Schulze and the two Top-2 hybrids (baseline and Clear-Eyed) ALSO get a
# same-family paired diff, folded into this SAME simulation pass instead of each re-running its
# own separate JOINT_NITER-election simulation over the same labels/electorates a second time.
PAIRED_DIFF_PAIRS = [(label, "STAR") for label in COMPARE_LABELS if label != "STAR"] + [
    ("RCV (IRV)", "Condorcet (Schulze)"),
    ("Schulze (equal ranks)", "Condorcet (Schulze)"),
    ("Approval", "Plurality"),
    ("Approval Top-2", "Plurality Top-2"),
    ("Approval Top-2 (Clear-Eyed)", "Plurality Top-2 (Clear-Eyed)"),
    # Each Top-2 hybrid ALSO gets a paired diff vs its own family's base (non-runoff) method --
    # quantifies whether the runoff step itself helps or hurts, feeding Section 23's gap tables.
    ("Approval Top-2 (Coma)", "Approval"),
    ("Approval Top-2", "Approval"),
    ("Approval Top-2 (Clear-Eyed)", "Approval"),
    ("Plurality Top-2", "Plurality"),
    ("Plurality Top-2 (Clear-Eyed)", "Plurality"),
    # "Score Top-2 (Clear-Eyed)" vs "Approval Top-2 (Clear-Eyed)" -- a coarse (Approval) vs.
    # fine-grained (0..5 Score) noisy primary ballot, both with an idealized/delayed clear-eyed
    # runoff to correct their pick. Section 23 used to compute this as a bespoke "theoretical
    # SCORE Top-2" re-simulation; now it's just another pair riding this same run.
    ("Score Top-2 (Clear-Eyed)", "Approval Top-2 (Clear-Eyed)"),
]


# Every COMPARE_LABELS method ALSO gets a paired Condorcet-efficiency diff vs Schulze -- same
# "mean of per-election paired differences" design as PAIRED_DIFF_PAIRS above, applied to the
# binary CW-selection indicator instead of VSE (see Section 19's CE table/chart below).
PAIRED_CE_PAIRS = [(label, "Condorcet (Schulze)") for label in COMPARE_LABELS if label != "Condorcet (Schulze)"]


# Section 23's runoff-betrayal/flip (STAR) and Coma-corruption (Approval Top-2 (Coma)) diagnostics
# used to each re-simulate their own separate batch of elections per scenario; folded into the
# main joint-scenario run below instead (see run_vse_simulation's betrayal_targets/coma_targets
# docstring), so they ride the SAME JOINT_NITER-election _joint_electorate_pool draws as every
# other COMPARE_LABELS method here, at that same (higher) precision.
BETRAYAL_TARGETS = [("STAR", STAR_TOP_RANK)]
COMA_TARGETS = [("Approval Top-2 (Coma)", 1), ("STAR", STAR_TOP_RANK)] 
PRIMARY_COST_TARGETS = [("Approval Top-2", 1)]


# ---------------------------------------------------------------------------
# Univariate sweep grid (notebook section 13)
# ---------------------------------------------------------------------------

# SWEEP_VALUES is defined in Section 5 (Parameters) -- single source of truth, see there.
# epistemic_rho sweeps every method; awareness_alpha/fatigue_beta are restricted to PRE_NOISE_METHODS --
# see the section markdown above for why. "Approval Top-2 (Coma)" reacts ONLY to awareness_alpha
# (its runoff reapplies friction at the primary's own awareness_alpha, fatigue pinned to 1.0 -- see
# Top2Base.__init__) -- both epistemic_rho and fatigue_beta are held at 1.0 throughout their own
# sweeps, so Coma would be identical to plain "Approval Top-2" at EVERY point of those two
# sweeps, not just one redundant endpoint. Excluded from both entirely rather than left in to
# silently overlap; kept in the awareness_alpha sweep (via PRE_NOISE_METHODS, unchanged) where it's
# genuinely distinct.
COMA_LABEL = "Approval Top-2 (Coma)"
METHODS_NO_COMA = [(label, m) for label, m in METHODS if label != COMA_LABEL]
PRE_NOISE_METHODS_NO_COMA = [(label, m) for label, m in PRE_NOISE_METHODS if label != COMA_LABEL]

# "Score Top-2 (Clear-Eyed)" is an exception to the PRE_NOISE_METHODS exclusion above: unlike
# "Approval Top-2 (Clear-Eyed)"/"Plurality Top-2 (Clear-Eyed)", which each have a real
# non-Clear-Eyed sibling already in PRE_NOISE_METHODS that's mathematically identical to it under
# these two parameters (so excluding the Clear-Eyed copy there just drops a redundant duplicate
# row), there is no plain "Score Top-2" method registered in METHODS at all -- the same exclusion
# therefore drops Score Top-2 (Clear-Eyed)'s only data point from both sweeps entirely, not a
# duplicate. Added back explicitly so it's actually simulated there -- needed to isolate the STAR
# vs Score-Top-2(Clear-Eyed) gap by awareness_alpha/fatigue_beta alone (see Section 22/23).
SCORE_T2_CE_LABEL = "Score Top-2 (Clear-Eyed)"
SCORE_T2_CE_ENTRY = [(label, m) for label, m in METHODS if label == SCORE_T2_CE_LABEL]
PRE_NOISE_METHODS_PLUS_SCORE_CE = PRE_NOISE_METHODS + SCORE_T2_CE_ENTRY
PRE_NOISE_METHODS_NO_COMA_PLUS_SCORE_CE = PRE_NOISE_METHODS_NO_COMA + SCORE_T2_CE_ENTRY

SWEEP_PARAMS = [
    ("epistemic_rho", METHODS_NO_COMA),
    ("awareness_alpha", PRE_NOISE_METHODS_PLUS_SCORE_CE),
    ("fatigue_beta", PRE_NOISE_METHODS_NO_COMA_PLUS_SCORE_CE),
]

sweep_results_by_param = {}      # param -> {value: {(label, chooser): (mean, ci)}}
sweep_ce_by_param = {}           # param -> {value: {(label, chooser): raw_ce}}
sweep_paired_diff_by_param = {}  # param -> {value: {(label, baseline_label): (mean, ci)}}
primary_corruption_by_value_by_param = {}  # param -> {value: primary_corruption_sink} -- Section 24
SWEEP_VALUES_TO_RUN = [v for v in SWEEP_VALUES if v != 1.0]

# STAR's betrayal diagnostic, threaded through ALL THREE sweeps below (previously epistemic_rho
# only -- see Section 23's per-parameter betrayal breakdown) -- this rides the exact same
# simulation runs the paired-diff pairs just below already need, so widening it to all three
# params is close to free, not a new simulation pass.
STAR_BETRAYAL_TARGETS = [("STAR", STAR_TOP_RANK)]
# (The notebook declared three empty per-value betrayal accumulators here. Those are run
# state rather than configuration -- stages.py builds them fresh per run, so importing
# this module never carries numbers from a previous run.)

# Real paired STAR-vs-Score-Top-2(Clear-Eyed) and STAR-vs-Score5 gaps, one parameter at a time --
# same "genuine paired comparison, not independent point estimates" convention as every other
# paired_diff_pairs use in this notebook (see run_vse_simulation's own docstring). Answers "which
# of the three parameters drives the STAR vs Score-Top-2(Clear-Eyed) gap most" (Section 22/23).
SCORE_STAR_PAIRED_DIFF_PAIRS = [("Score Top-2 (Clear-Eyed)", "STAR"), ("Score5", "STAR")]


# ---------------------------------------------------------------------------
# Joint 'realistic conditions' scenarios (notebook section 16)
# ---------------------------------------------------------------------------

SCENARIO_VALUES = [1.0, 0.9, 0.8, 0.7]  # ideal -> heavy friction

JOINT_SCENARIOS = {
    "Ideal":              {"epistemic_rho": 1.0,  "awareness_alpha": 1.0,  "fatigue_beta": 1.0},
    "Mild friction":      {"epistemic_rho": SCENARIO_VALUES[1], "awareness_alpha": SCENARIO_VALUES[1], "fatigue_beta": SCENARIO_VALUES[1]},
    "Moderate friction":  {"epistemic_rho": SCENARIO_VALUES[2],  "awareness_alpha": SCENARIO_VALUES[2],  "fatigue_beta": SCENARIO_VALUES[2]},
    "Heavy friction":     {"epistemic_rho": SCENARIO_VALUES[3],  "awareness_alpha": SCENARIO_VALUES[3],  "fatigue_beta": SCENARIO_VALUES[3]},
}


# ---------------------------------------------------------------------------
# Runoff sweeps (notebook section 21)
# ---------------------------------------------------------------------------

RUNOFF_BASELINE_NAMES = ["Mild friction", "Moderate friction", "Heavy friction"]  # reuse
# JOINT_SCENARIOS as-is -- Mild included for completeness/consistency with the learn sweep below,
# even though its curve is expected to be the flattest of the three (least friction to recover from).

MILD_BASELINE = JOINT_SCENARIOS["Mild friction"]["epistemic_rho"]
MODERATE_BASELINE = JOINT_SCENARIOS["Moderate friction"]["epistemic_rho"]
HEAVY_BASELINE = JOINT_SCENARIOS["Heavy friction"]["epistemic_rho"]

# Swept across the FULL 0-1 range (not just [own baseline, 1.0]) so the chart shows the real
# shape of the curve, not just its already-high-information tail. Each baseline's own primary
# epistemic_rho is explicitly unioned in as a real grid point (not just a nearby one) -- with the
# paired noise above, the fresh runoff_rho=<baseline> point should land on (or, given independent
# per-election draws, very near) the runoff_rho=None (Groggy) result plotted alongside it: a genuine
# sanity check, not just a visual approximation. A fine linspace(baseline, 1.0, 5) is unioned in
# too, on top of the coarse base grid -- same "add resolution around the values that matter"
# pattern as RUNOFF_KAPPA_VALUES' linspace(0.2, 0.4, 5) below: [baseline, 1.0] is the only range
# that corresponds to an actual runoff-information story for THIS scenario (the runoff can only
# get cleaner than the primary's own noise floor, never noisier), so that's where extra grid
# points pay for themselves.
MILD_RHO_VALUES = np.array(sorted(set(np.linspace(0.0, 1.0, 6)) | set(np.linspace(MILD_BASELINE, 1.0, 5)) | {MILD_BASELINE}))
MODERATE_RHO_VALUES = np.array(sorted(set(np.linspace(0.0, 1.0, 6)) | set(np.linspace(MODERATE_BASELINE, 1.0, 5)) | {MODERATE_BASELINE}))
HEAVY_RHO_VALUES = np.array(sorted(set(np.linspace(0.0, 1.0, 6)) | set(np.linspace(HEAVY_BASELINE, 1.0, 5)) | {HEAVY_BASELINE}))

RUNOFF_RHO_VALUES_BY_BASELINE = {
    "Mild friction": [None] + list(MILD_RHO_VALUES),
    "Moderate friction": [None] + list(MODERATE_RHO_VALUES),
    "Heavy friction": [None] + list(HEAVY_RHO_VALUES),
}
RUNOFF_METHOD_FACTORIES = {
    "Approval Top-2": lambda rt, aw: ApprovalTop2(runoff_rho=rt, runoff_awareness_alpha=aw),
}
# Fatigue is always pinned at 1.0 for the runoff (low-controversy: 2 candidates isn't a long
# ballot to get fatigued by). Awareness is the real, contestable assumption -- run it two
# ways rather than asserting one, so the sensitivity of the whole story to this one modeling
# choice is visible rather than hidden. Each mode is a function of (rt, primary_awareness_alpha),
# so awareness can be pinned or held at the primary's own level. (A third mode used to tie
# awareness to move together with runoff_rho itself -- dropped: now that "chance to learn who the
# finalists are" and "chance to correct a noisy preference" are treated as genuinely separate
# mechanisms, see the kappa sweep below, yoking them to one shared slider no longer makes
# sense as something to test.)
RUNOFF_AWARENESS_MODES = {
    "Awareness resets to 1.0": lambda rt, primary_aw: 1.0,
    "Awareness carries over from primary": lambda rt, primary_aw: primary_aw,
}
# Only "resets to 1.0" runs at full precision below -- it's the mode that brackets the Groggy/
# Clear-Eyed models (see the runoff-t-sweep chart's X markers). "Carries over from primary"
# doesn't bracket any named model, so it's relegated to the lower-precision secondary section
# further down instead of doubling this section's main runtime.
RUNOFF_AWARENESS_MODES_MAIN = {"Awareness resets to 1.0": RUNOFF_AWARENESS_MODES["Awareness resets to 1.0"]}


RUNOFF_KAPPA_VALUES = np.array(
    sorted(
        set(np.linspace(0.0, 1.0, 6))
        | set(np.linspace(0.1, 0.3, 7))
        | {0.25}
        | {1 / 3}
    )
)  # adds 0.25/0.3/0.35 between the existing 0.2/0.4 grid points, to narrow down where AT2
    # crosses significantly ahead of STAR (see the paired threshold table below). Same range for
    # all three baselines -- unlike runoff_rho, runoff_kappa's meaning doesn't depend on the
    # primary's own AWARENESS_ALPHA.
RUNOFF_T_FIXED_VARIANTS = {
    "primary's own noise (runoff_rho=None)": None,
    "perfect runoff information (runoff_rho=1.0)": 1.0,
}
# Only "runoff_rho=None" runs at full precision below -- it's the variant that brackets both Coma
# (kappa=0) and Groggy (kappa=1). "runoff_rho=1.0" only brackets Clear-Eyed at its kappa=1 endpoint, so it's
# relegated to the lower-precision secondary section further down instead of doubling this
# section's main runtime.
RUNOFF_T_FIXED_VARIANTS_MAIN = {
    "primary's own noise (runoff_rho=None)": RUNOFF_T_FIXED_VARIANTS["primary's own noise (runoff_rho=None)"],
}
RUNOFF_LEARN_METHOD_FACTORIES = {
    "Approval Top-2": lambda rt, kappa: ApprovalTop2(runoff_rho=rt, runoff_kappa=kappa),
}


# ---------------------------------------------------------------------------
# Candidate-count sweep (notebook section 25)
# ---------------------------------------------------------------------------

NCAND_SWEEP_LABELS = ["Approval Top-2", "Plurality Top-2"]
# Adjust NCAND_SWEEP_NITER for this cell in Section 5 (Parameters).
NCAND_VALUES = [3, 5, 6, 8, 10, 15]


# ---------------------------------------------------------------------------
# Presentation-only label sets (notebook sections 22 and 26)
# ---------------------------------------------------------------------------

STAR_SCORE_LABELS = ["Score5", "STAR"]
HIST_LABELS = ["STAR", "Approval", "Approval Top-2", "Plurality", "Plurality Top-2", "Condorcet (Schulze)"]

CLAMP_NEGATIVE_VALUES = True  # True: collapse every VSE < 0 into the single leftmost bucket (at
                               # 0%) instead of stretching the x-axis to fit an absurdly long,
                               # sparse negative tail that hides the shape of the real (mostly
                               # positive) distribution. Flip to False to see the true unclamped
                               # tail, with an x=0 reference line instead.

# Shared x-range per method (pooled across all 4 scenarios) so the four separate figures below
# are visually comparable panel-to-panel for a given method -- the whole point is spotting
