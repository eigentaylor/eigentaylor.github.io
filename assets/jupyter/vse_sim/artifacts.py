"""Reading and writing the committed simulation results.

Every expensive stage in this project returns nothing but small numeric summaries, so the
elections themselves never need to be kept. That is what lets the notebook render in
seconds instead of re-running for an hour: the numbers are computed once, written here,
and read back.

**What gets stored.** The raw accumulators `(n, sum, sum_sq)`, not the reduced
`(mean, ci)`. Those three numbers are the complete sufficient statistics for a mean and
its confidence interval, so nothing is lost:

    s^2 = (sum_sq - sum^2 / n) / (n - 1)        CI_z = z * s / sqrt(n)

Storing them means a reader can re-derive a bound at any confidence level -- the 99%
re-check in section 27, or anything else -- straight from the committed file, without
re-running a simulation and without trusting an arithmetic rescaling of a 95% interval.

**Why records rather than dicts.** The stage outputs are keyed by tuples
(`(label, chooser)`), by floats (`0.3`, and `1/3` out of `np.linspace`), and in one case
by `None` (a runoff that reuses its primary's electorate). None of those survive a JSON
round-trip as object keys. So every mapping is flattened into a list of records with the
key components as ordinary fields, and rebuilt on load from a declared `levels` spec.
`np.float64` and friends are coerced to plain Python numbers on the way out, loudly:
anything that is not JSON-representable raises rather than being silently dropped.

**Staleness.** Each file carries a `spec` -- the parameters the run was defined by -- and
its SHA-256. Loading an artifact whose spec doesn't match the live `config.py` raises and
names the command that would rebuild it, so a changed parameter can never quietly render
against numbers from before the change.

**Verification.** `content_hash` covers the data itself. `python -m vse_sim.run --verify`
re-runs every stage from `config.SEED` and compares, which is the whole argument for the
published numbers: nobody has to take the committed JSON on faith, they can regenerate it.
"""
import hashlib
import json
import pathlib

import numpy as np

SCHEMA = 1
RESULTS_DIR = pathlib.Path(__file__).resolve().parent / "results"


class StaleArtifact(RuntimeError):
    """A stored result no longer matches the configuration that would produce it."""


class MissingArtifact(RuntimeError):
    """A stage has not been run yet."""


# --------------------------------------------------------------------------------
# JSON coercion
# --------------------------------------------------------------------------------

def jsonable(obj):
    """Coerce NumPy scalars/arrays to plain Python; raise on anything else.

    Deliberately strict. A `np.float64` left in the tree would abort the write with an
    opaque TypeError halfway through; worse, a silently-dropped value would produce a
    result file that looks complete and isn't.
    """
    if isinstance(obj, np.generic):
        return obj.item()
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (set, frozenset)):
        return sorted(obj)
    raise TypeError(f"{type(obj).__name__} is not JSON-representable: {obj!r}")


def canonical(obj):
    """A stable JSON string: sorted keys, no incidental whitespace. Used for hashing."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=jsonable)


def sha256(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()


# --------------------------------------------------------------------------------
# Nested dicts <-> records
# --------------------------------------------------------------------------------

def _leaf_to_fields(leaf, scalar_name="value"):
    if isinstance(leaf, (list, tuple)) and len(leaf) == 3 and all(
            isinstance(x, (int, float, np.generic)) for x in leaf):
        n, total, total_sq = leaf
        return {"n": int(n), "sum": float(total), "sum_sq": float(total_sq)}
    if isinstance(leaf, dict):
        return {k: (v.item() if isinstance(v, np.generic) else v) for k, v in leaf.items()}
    if isinstance(leaf, (int, float, np.generic)):
        return {scalar_name: leaf.item() if isinstance(leaf, np.generic) else leaf}
    raise TypeError(f"don't know how to store leaf of type {type(leaf).__name__}: {leaf!r}")


def _fields_to_leaf(fields, scalar_name="value"):
    if set(fields) == {"n", "sum", "sum_sq"}:
        return [fields["n"], fields["sum"], fields["sum_sq"]]
    if set(fields) == {scalar_name}:
        return fields[scalar_name]
    return dict(fields)


def _key_part(key):
    if isinstance(key, np.generic):
        return key.item()
    return key


def to_records(mapping, levels, scalar_name="value"):
    """Flatten a nested mapping into JSON-safe records.

    `levels` names each level of nesting: a string for a level keyed by one value, or a
    tuple of strings for a level keyed by a tuple. So `{(label, chooser): acc}` is
    `levels=[("label", "chooser")]`, and `{scenario: {(label, chooser): acc}}` is
    `levels=["scenario", ("label", "chooser")]`.

    `scalar_name` is the field a bare number is stored under. Name it for what it holds
    whenever a caller will nest the result under keys of its own -- the default collides
    with a level called "value", which is how a swept parameter is keyed. A collision
    raises here rather than silently overwriting a key with a count.
    """
    rows = []

    def walk(node, depth, prefix):
        if depth == len(levels):
            fields = _leaf_to_fields(node, scalar_name)
            clash = set(prefix) & set(fields)
            if clash:
                raise ValueError(f"leaf field(s) {sorted(clash)} collide with level names "
                                 f"{sorted(prefix)}; pass a distinct scalar_name")
            rows.append({**prefix, **fields})
            return
        names = levels[depth]
        names = (names,) if isinstance(names, str) else tuple(names)
        for key, value in node.items():
            parts = key if isinstance(key, tuple) else (key,)
            if len(parts) != len(names):
                raise ValueError(f"level {depth} expects {len(names)} key parts, got {key!r}")
            walk(value, depth + 1, {**prefix, **dict(zip(names, map(_key_part, parts)))})

    walk(mapping, 0, {})
    level_names = {n for names in levels for n in ((names,) if isinstance(names, str) else names)}
    for row in rows[:1]:
        clash = level_names & (set(row) - level_names)
        if clash:
            raise ValueError(f"leaf field(s) {sorted(clash)} collide with level names; "
                             f"pass a distinct scalar_name")
    return rows


def from_records(rows, levels, scalar_name="value"):
    """Rebuild the nested mapping `to_records` flattened, tuple keys and all."""
    out = {}
    flat_names = []
    for names in levels:
        flat_names.append((names,) if isinstance(names, str) else tuple(names))
    for row in rows:
        node = out
        for depth, names in enumerate(flat_names):
            parts = tuple(row[n] for n in names)
            key = parts[0] if len(parts) == 1 else parts
            if depth == len(flat_names) - 1:
                node[key] = _fields_to_leaf(
                    {k: v for k, v in row.items()
                     if k not in {n for ns in flat_names for n in ns}}, scalar_name)
            else:
                node = node.setdefault(key, {})
    return out


# --------------------------------------------------------------------------------
# Files
# --------------------------------------------------------------------------------

def code_version():
    """A digest of the simulation code, for provenance.

    Recorded alongside each result but deliberately NOT part of `spec_hash`. The spec
    guards parameters, and is checked on every notebook load, so it must not fire on a
    comment or a docstring -- an 80-minute re-run is too blunt an answer to a typo fix.
    Code drift is caught by `python -m vse_sim.run --verify`, which re-runs and compares
    the results themselves; that is a stronger check than any hash of the source.
    """
    root = pathlib.Path(__file__).resolve().parent
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*.py")):
        if any(part in {"tests", "tools", "__pycache__"} for part in path.parts):
            continue
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()[:16]


def path_for(stage, results_dir=RESULTS_DIR):
    return pathlib.Path(results_dir) / f"{stage}.json"


def write(stage, spec, data, results_dir=RESULTS_DIR, runs=1):
    """Write one stage's results. `data` maps a section name to a list of records."""
    payload = {
        "schema": SCHEMA,
        "stage": stage,
        "runs": runs,
        "generated_by": f"python -m vse_sim.run --stage {stage}",
        "spec": spec,
        "spec_hash": sha256(spec),
        "content_hash": sha256(data),
        "code_version": code_version(),
        "data": data,
    }
    path = path_for(stage, results_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=1, default=jsonable, sort_keys=True) + "\n",
                    encoding="utf-8")
    return path


def read(stage, results_dir=RESULTS_DIR):
    """The raw stored payload, with no staleness check. Use `load` for rendering."""
    path = path_for(stage, results_dir)
    if not path.exists():
        raise MissingArtifact(
            f"no results for stage {stage!r} at {path}.\n"
            f"    Run:  python -m vse_sim.run --stage {stage}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != SCHEMA:
        raise StaleArtifact(f"{path} uses schema {payload.get('schema')}, expected {SCHEMA}")
    return payload


def load(stage, spec, results_dir=RESULTS_DIR):
    """The stored payload, checked against the spec the live config would produce.

    Raises `StaleArtifact` naming the parameters that changed, so a rendering run can
    never quietly show numbers from before an edit to `config.py`.
    """
    payload = read(stage, results_dir)
    if payload["spec_hash"] == sha256(spec):
        return payload
    stored = payload["spec"]
    changed = sorted(k for k in set(stored) | set(spec)
                     if canonical(stored.get(k)) != canonical(spec.get(k)))
    detail = "\n".join(f"      {k}: stored {stored.get(k)!r} -> config {spec.get(k)!r}"
                       for k in changed)
    raise StaleArtifact(
        f"results for stage {stage!r} were produced under a different configuration:\n"
        f"{detail}\n"
        f"    Re-run:  python -m vse_sim.run --stage {stage}")


def merge(base, extra):
    """Pool two runs of the same stage into one set of records.

    Accumulators add elementwise -- `n`, `sum` and `sum_sq` are each a sum over
    elections, so pooling two independent batches gives exactly the mean and variance of
    the combined sample, not an approximation of it. Every other numeric field in a
    record is an integer count and adds the same way.

    This exists for a reader who wants tighter intervals than the published run has: a CI
    half-width scales as n^(-1/2), so quartering it means 16x the elections, which is
    easier as several batches than one job. Nothing published uses it -- `run.py` refuses
    to merge into the committed `results/` directory, and every committed artifact
    records `runs: 1`.
    """
    if base["spec_hash"] != extra["spec_hash"]:
        raise ValueError("cannot merge results produced under different configurations")
    if set(base["data"]) != set(extra["data"]):
        raise ValueError("cannot merge results with different sections")
    merged = {}
    for section, rows in base["data"].items():
        other = {_row_key(r): r for r in extra["data"][section]}
        out = []
        for row in rows:
            match = other.get(_row_key(row))
            if match is None:
                raise ValueError(f"section {section!r}: no counterpart for {_row_key(row)}")
            out.append({k: (v + match[k] if isinstance(v, (int, float))
                            and not isinstance(v, bool) else v)
                        for k, v in row.items()})
        merged[section] = out
    return {**base, "runs": base["runs"] + extra["runs"], "data": merged,
            "content_hash": sha256(merged)}


def _row_key(row):
    """A record's identity: its non-numeric fields, i.e. everything but the counts."""
    return tuple(sorted((k, v) for k, v in row.items()
                        if not isinstance(v, (int, float)) or isinstance(v, bool)
                        or k not in {"n", "sum", "sum_sq", "value"}))
