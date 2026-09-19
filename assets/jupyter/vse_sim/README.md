# `vse_sim`

The simulation code behind [`vse_simulation_modular.ipynb`](../vse_simulation_modular.ipynb).

It measures **Voter Satisfaction Efficiency** for Plurality, Approval, IRV, STAR, Score,
Condorcet (Schulze) and four Top-2 hybrids, under three ways that real voters fall short of
the idealised ones a simulation usually assumes: noisy perception of the candidates,
unfamiliarity with some of them, and ballot fatigue.

## Reproducing the published numbers

```bash
cd assets/jupyter
pip install -r ../../requirements.txt

python -m vse_sim.run --stage all      # recompute everything (~25-40 min)
python -m vse_sim.run --verify         # re-run and check it matches what is committed
python -m vse_sim.run --list           # what is stored, and whether it is current
```

`--verify` is the point. Every number in the post comes from one run of `--stage all` at
the single `SEED` declared in [`config.py`](config.py); each stage is seeded from that one
value and depends on no other stage, so re-running reproduces the committed results **bit
for bit**. You do not have to trust `results/*.json` — regenerate it. If `--verify` reports
a mismatch, that is a bug worth reporting.

```bash
python -m pytest vse_sim/tests/
```

`tests/test_parity.py` and `tests/test_sweeps_parity.py` run the original single-file
[`vse_simulation.ipynb`](../vse_simulation.ipynb) — still in this repository, unchanged —
side by side with this package over identical electorates and require every number to match
exactly. `tests/test_sanity.py` carries the mechanism checks that used to sit inline in the
notebook. `tests/test_artifacts.py` covers the storage round-trip and determinism.

## Layout

| | |
|---|---|
| `vendored/` | An unmodified copy of the [`vse-sim`](https://github.com/electionscience/vse-sim) methodology from the Center for Election Science — the `Method` base class and VSE formula, the "kitchen sink" `KSModel` electorate, the choosers, and the five baseline methods. One module per upstream file. Nothing here is original to this project. |
| `noise.py` | Epistemic noise: voters perceive `rho * u + sqrt(1 - rho^2) * sigma * z` instead of their true utility `u`. At `rho = 1` it is an exact no-op. |
| `friction.py` | Participation friction: which candidates a voter has actually evaluated, given unfamiliarity (`awareness_alpha`) and ballot fatigue (`fatigue_beta`). |
| `top2.py` | The Top-2 hybrids: a primary picks two finalists, then a runoff decides between them under its own information assumptions. |
| `condorcet.py` | Whether a true Condorcet winner exists, computed from the true electorate — independent of any method, chooser or noise. |
| `config.py` | Every parameter, in one place. No side effects: importing it seeds nothing and runs nothing. |
| `engine.py` | The per-election loop and its reducers. |
| `sweeps.py` | Drivers that run the loop across a parameter grid. |
| `electorates.py` | Deterministic electorate pools, cached locally. |
| `artifacts.py` | Reading and writing `results/`. |
| `stages.py` | The eight expensive runs. |
| `run.py` | The command line. |
| `render/` | Tables and charts. Reads results; never simulates. |
| `tools/nb_outline.py` | Read a notebook's structure without loading its stored images. |

## The stages

| Stage | Section | Elections | What it answers |
|---|---|---|---|
| `ideal` | 9 | `NITER` | Every method with no degradation, across the full honest/strategic chooser battery. |
| `sweeps` | 13 | `SWEEP_NITER` | Each of the three degradation parameters moved on its own. |
| `joint` | 16 | `JOINT_NITER` | All three moved together: Mild, Moderate and Heavy friction. |
| `plurality_ideal` | 24 | `JOINT_NITER` | The Plurality family at Ideal, over the *same* elections as `joint`, so the two can be compared election by election. |
| `runoff_rho` | 21 | `RUNOFF_RHO_SWEEP_NITER` | How much a better-informed runoff helps. |
| `runoff_learn` | 21 | `RUNOFF_SWEEP_NITER` | The same question as a chance to learn an unfamiliar finalist. |
| `ncand` | 25 | `NCAND_SWEEP_NITER` | Approval Top-2 vs Plurality Top-2 as the field grows. |

Run one on its own with `--stage <name>`.

## What is stored, and why in that form

`results/<stage>.json` holds the raw accumulators `(n, sum, sum_sq)` per key, not the
reduced `(mean, ci)`. Those three numbers are the complete sufficient statistics for a mean
and its confidence interval:

$$s^2 = \frac{\sum x^2 - (\sum x)^2/n}{n-1} \qquad \mathrm{CI}_z = z\,\frac{s}{\sqrt{n}}$$

so any confidence level can be derived from the committed file without re-running anything
— the 99% re-check in section 27 included. Storing `(mean, ci)` instead would throw away
`n` and `s` and make that impossible.

Keys are stored as *records*, not as JSON object keys, because the natural keys here are
tuples (`(label, chooser)`), floats (`1/3`, out of `np.linspace`), and in one case the
literal `None` (a runoff that reuses its primary's electorate). None of those survive as
JSON keys.

Two things need the individual elections rather than their moments, and go to
`results/<stage>_raw_vse.npz` in float64: section 26's histograms, which report an empirical
mode and a negative-value fraction, and section 24's paired table, which counts how many
individual elections got better or worse.

Each file also carries the `spec` it was produced under and that spec's SHA-256. The
notebook checks it on load and raises if `config.py` has changed since, so it cannot
silently render numbers from before an edit.

## Electorate pools

Drawing an electorate costs about 20 ms at the published settings — roughly a quarter of a
full run. `electorates.py` caches them under a gitignored `.cache/`. They are a pure
function of `SEED`, so caching adds nothing to what you have to trust: delete the cache and
it rebuilds identically. Stages reseed before simulating, so a warm cache and a cold one
give the same results (`tests/test_artifacts.py` pins this down).

Pools are keyed by a `pool_id` rather than a stage name, because some stages must share
one: section 24's paired table compares `plurality_ideal` against `joint` election by
election, which is only meaningful over identical draws.

## Running more elections than the post did

Accumulators pool exactly under elementwise addition, so independent batches merge into the
combined sample's mean and variance with no approximation. A confidence half-width scales
as $n^{-1/2}$, so quartering one costs sixteen times the elections — easier as several
batches than one job:

```bash
python -m vse_sim.run --stage joint --extra-batch 2 --out ./my_runs
python -m vse_sim.run --stage joint --extra-batch 3 --out ./my_runs
```

This is for a reader who wants tighter intervals than the post reports. Nothing published
uses it: `--extra-batch` requires an explicit output directory and refuses to write into
`results/`, and every committed artifact records `runs: 1`.
