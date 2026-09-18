"""Deterministic electorate pools, cached on disk.

Drawing an electorate is not cheap: at the published 101-voter / 6-candidate settings the
"kitchen sink" hierarchical-cluster model takes roughly 20ms per election, which across a
full run of the original notebook came to about 630 seconds -- a quarter of its total
runtime -- spent building electorates rather than counting ballots.

A pool is a pure function of `config.SEED` and the pool's own id, so caching one adds
nothing to what a reader has to trust: delete the cache and it rebuilds byte-identically.
For that reason the cache directory is gitignored. What *is* committed is the results the
pools produced.

Two properties this module depends on, both verified by `tests/test_electorates.py`:

1. **A pool round-trips through a plain float64 array.** `make_perceived_electorate` and
   `_floor_to_genuine` both return plain `Electorate` objects, and nothing in the methods
   or choosers reads the `DimVoter`/`PersonalityVoter` extras (`.personality`, `.cluster`,
   `.dims`, `.elec`) that the model attaches while building. Only the utilities matter.
2. **Pools are prefix-compatible.** Electorate `i` depends only on the seed and on `i`,
   so the first `k` of an `n`-election pool are exactly the pool you would get by asking
   for `k`. A cached pool is therefore reused for any smaller request, and only regrown
   when a larger one arrives.

Stages declare a `pool_id` rather than using their own name, because several of them
must share a pool: section 16's joint scenarios and section 24's Ideal-only Plurality
run are compared election by election, which is only meaningful over identical draws.
"""
import hashlib
import pathlib

import numpy as np

from . import config as cfg
from .vendored.simulation import seedRandomGenerators
from .vendored.voter_models import Electorate, Voter

CACHE_DIR = pathlib.Path(__file__).resolve().parent / ".cache"

# Nonzero only for an EXTRA batch -- elections a reader chose to run on top of the
# published ones, to get tighter intervals than the post reports. Every committed result
# was produced at batch 0. See `run.py --extra-batch`, which refuses to write into the
# committed results directory.
BATCH = 0


def pool_seed(pool_id):
    """The seed a pool is drawn under: one published seed, one id, nothing else.

    Deriving every pool from `config.SEED` this way is what makes a run reproducible
    from a single declared value -- there is no per-stage seed anyone could have picked
    independently of the others.
    """
    suffix = "" if not BATCH else f"/batch{BATCH}"
    return f"{cfg.SEED}/{pool_id}{suffix}"


def _fingerprint(pool_id, nvot, ncand):
    """Everything except the election count that determines a pool's contents."""
    key = f"{pool_seed(pool_id)}|{cfg.MODEL}|{nvot}|{ncand}"
    return hashlib.sha256(key.encode()).hexdigest()[:12]


def _cache_path(pool_id, nvot, ncand, cache_dir=None):
    safe = pool_id.replace("/", "__")
    root = CACHE_DIR if cache_dir is None else cache_dir
    return pathlib.Path(root) / f"{safe}-c{ncand}-{_fingerprint(pool_id, nvot, ncand)}.npy"


def to_array(electorates):
    """A list of electorates as an (niter, nvot, ncand) float64 array."""
    return np.array([[list(voter) for voter in e] for e in electorates], dtype=np.float64)


def from_array(arr):
    """The inverse of `to_array`."""
    return [Electorate(Voter(row) for row in election) for election in arr]


def draw(pool_id, niter, ncand=None, nvot=None):
    """Draw a pool from scratch, ignoring any cache. Deterministic given `pool_id`."""
    ncand = cfg.NCAND if ncand is None else ncand
    nvot = cfg.NVOT if nvot is None else nvot
    seedRandomGenerators(pool_seed(pool_id))
    return [cfg.MODEL(nvot, ncand) for _ in range(niter)]


def pool(pool_id, niter, ncand=None, nvot=None, cache_dir=None, use_cache=True):
    """`niter` true electorates for `pool_id`, from the cache when one is big enough.

    A cached pool of at least `niter` elections is sliced rather than redrawn (see the
    prefix-compatibility note above); a smaller one is regrown to `niter` and rewritten,
    so the cache converges on the largest size anyone has asked for.
    """
    ncand = cfg.NCAND if ncand is None else ncand
    nvot = cfg.NVOT if nvot is None else nvot
    path = _cache_path(pool_id, nvot, ncand, cache_dir)

    if use_cache and path.exists():
        cached = np.load(path)
        if cached.shape[0] >= niter and cached.shape[1:] == (nvot, ncand):
            return from_array(cached[:niter])

    electorates = draw(pool_id, niter, ncand=ncand, nvot=nvot)
    if use_cache:
        path.parent.mkdir(parents=True, exist_ok=True)
        np.save(path, to_array(electorates))
    return electorates


def clear_cache(cache_dir=None):
    """Delete every cached pool. Safe: they are all regenerable from `config.SEED`.

    `cache_dir` is resolved at call time rather than bound as a default, so a test can
    point `CACHE_DIR` somewhere temporary and not delete the real cache out from under
    whoever is running it.
    """
    removed = 0
    for path in pathlib.Path(CACHE_DIR if cache_dir is None else cache_dir).glob("*.npy"):
        path.unlink()
        removed += 1
    return removed
