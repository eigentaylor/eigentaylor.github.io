"""Command-line entry point: run the simulations, or check that they reproduce.

    python -m vse_sim.run --stage all        # the canonical run; writes results/
    python -m vse_sim.run --stage joint      # re-run one stage
    python -m vse_sim.run --verify           # re-run and compare against results/
    python -m vse_sim.run --list             # what is stored, and whether it is current

Every published number comes from `--stage all` at the seed declared in `config.py`, and
nothing else. Because each stage is seeded from that one value and depends on no other
stage, `--verify` re-runs the lot and compares content hashes: a reader does not have to
take the committed JSON on faith, they can regenerate it and see it match.

If you want tighter intervals than the published run has, `--extra-batch` draws a fresh,
independent set of elections and merges them in. A CI half-width scales as n^(-1/2), so
quartering one takes 16x the elections -- easier as several batches than as one job:

    python -m vse_sim.run --stage joint --extra-batch 2 --out ./my_runs
    python -m vse_sim.run --stage joint --extra-batch 3 --out ./my_runs

That path requires an explicit output directory and refuses to touch `results/`, so the
published numbers stay exactly what one clean run produces.
"""
import argparse
import json
import pathlib
import sys
import time

from . import artifacts, config as cfg, electorates, stages


def _fmt_seconds(seconds):
    if seconds < 90:
        return f"{seconds:.1f}s"
    return f"{seconds / 60:.1f}min"


def _status(name, results_dir):
    """Whether the stored results for a stage are missing, stale, or current."""
    try:
        payload = artifacts.read(name, results_dir)
    except artifacts.MissingArtifact:
        return "missing", None
    live = artifacts.sha256(stages.STAGES[name].spec())
    return ("current" if payload["spec_hash"] == live else "stale"), payload


def cmd_list(args):
    print(f"{'stage':17s} {'section':>7s} {'niter':>7s} {'runs':>5s}  {'status':8s} spec")
    for name in stages.ORDER:
        stage = stages.STAGES[name]
        state, payload = _status(name, args.results_dir)
        niter = stage.spec()["niter"]
        runs = payload["runs"] if payload else "-"
        print(f"{name:17s} {stage.section:>7d} {niter:>7d} {str(runs):>5s}  {state:8s} "
              f"{artifacts.sha256(stage.spec())[:12]}")
    print(f"\nresults dir: {args.results_dir}")
    print(f"pool cache:  {electorates.CACHE_DIR} "
          f"({len(list(pathlib.Path(electorates.CACHE_DIR).glob('*.npy')))} pools cached)"
          if pathlib.Path(electorates.CACHE_DIR).exists() else
          f"pool cache:  {electorates.CACHE_DIR} (empty)")
    return 0


def cmd_run(args):
    names = stages.ORDER if args.stage == "all" else [args.stage]
    total = 0.0
    for name in names:
        print(f"=== {name} (section {stages.STAGES[name].section}) ", flush=True)
        path, elapsed = stages.run_stage(name, results_dir=args.results_dir,
                                         niter=args.niter, use_cache=not args.no_cache)
        total += elapsed
        print(f"--- {name} done in {_fmt_seconds(elapsed)} -> {path}\n", flush=True)
    print(f"All done in {_fmt_seconds(total)}.")
    return 0


def cmd_verify(args):
    """Re-run each stage and compare its content hash with what is stored.

    This is the claim the published numbers rest on: same seed, same config, same
    results, down to the last bit. A mismatch is a real problem, not rounding -- the
    simulation is deterministic.
    """
    names = stages.ORDER if args.stage in (None, "all") else [args.stage]
    failures = []
    for name in names:
        try:
            stored = artifacts.read(name, args.results_dir)
        except artifacts.MissingArtifact as exc:
            print(f"MISSING  {name}: {exc}")
            failures.append(name)
            continue
        started = time.time()
        (spec, data, _arrays), _ = stages.run_stage(
            name, results_dir=args.results_dir, niter=stored["spec"]["niter"],
            use_cache=not args.no_cache, write=False)
        ok_spec = artifacts.sha256(spec) == stored["spec_hash"]
        ok_data = artifacts.sha256(data) == stored["content_hash"]
        mark = "OK      " if (ok_spec and ok_data) else "MISMATCH"
        print(f"{mark} {name:17s} ({_fmt_seconds(time.time() - started)})"
              f"{'' if ok_spec else '  [spec differs]'}"
              f"{'' if ok_data else '  [results differ]'}")
        if not (ok_spec and ok_data):
            failures.append(name)
    if failures:
        print(f"\n{len(failures)} stage(s) did not reproduce: {', '.join(failures)}")
        return 1
    print(f"\nAll {len(names)} stage(s) reproduced exactly.")
    return 0


def cmd_extra_batch(args):
    out = pathlib.Path(args.out).resolve()
    if out == pathlib.Path(artifacts.RESULTS_DIR).resolve():
        print("--extra-batch will not write into the committed results/ directory.\n"
              "Every published number comes from one clean run; pass --out <somewhere else>.",
              file=sys.stderr)
        return 2
    names = stages.ORDER if args.stage == "all" else [args.stage]
    electorates.BATCH = args.extra_batch
    for name in names:
        base_path = artifacts.path_for(name, args.results_dir)
        base = json.loads(base_path.read_text(encoding="utf-8"))
        target = artifacts.path_for(name, out)
        current = json.loads(target.read_text(encoding="utf-8")) if target.exists() else base
        print(f"=== {name}, batch {args.extra_batch} ", flush=True)
        (spec, data, _arrays), elapsed = stages.run_stage(
            name, niter=base["spec"]["niter"], use_cache=not args.no_cache, write=False)
        extra = {"schema": artifacts.SCHEMA, "stage": name, "runs": 1, "spec": spec,
                 "spec_hash": artifacts.sha256(spec), "content_hash": artifacts.sha256(data),
                 "data": data}
        merged = artifacts.merge(current, extra)
        out.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(merged, indent=1, default=artifacts.jsonable,
                                     sort_keys=True) + "\n", encoding="utf-8")
        n = merged["data"]["vse"][0]["n"]
        print(f"--- {name}: {merged['runs']} runs pooled, n={n} per key "
              f"({_fmt_seconds(elapsed)}) -> {target}\n", flush=True)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m vse_sim.run",
                                     description=__doc__.split("\n\n")[0])
    parser.add_argument("--stage", choices=["all", *stages.ORDER],
                        help="which stage to run ('all' for every one, in order)")
    parser.add_argument("--verify", action="store_true",
                        help="re-run and compare against the stored results")
    parser.add_argument("--list", action="store_true", dest="list_stages",
                        help="show what is stored and whether it matches config.py")
    parser.add_argument("--extra-batch", type=int, metavar="N",
                        help="run an Nth independent batch and pool it in (needs --out)")
    parser.add_argument("--out", metavar="DIR",
                        help="where --extra-batch writes; never the committed results/")
    parser.add_argument("--niter", type=int,
                        help="override the election count (for a quick smoke run)")
    parser.add_argument("--results-dir", default=artifacts.RESULTS_DIR, type=pathlib.Path,
                        help=argparse.SUPPRESS)
    parser.add_argument("--no-cache", action="store_true",
                        help="ignore the electorate-pool cache and redraw from the seed")
    args = parser.parse_args(argv)

    print(f"vse_sim: seed={cfg.SEED!r} model={cfg.MODEL} nvot={cfg.NVOT} ncand={cfg.NCAND}\n")
    if args.list_stages:
        return cmd_list(args)
    if args.verify:
        return cmd_verify(args)
    if args.extra_batch is not None:
        if not args.out:
            parser.error("--extra-batch requires --out")
        if not args.stage:
            parser.error("--extra-batch requires --stage")
        return cmd_extra_batch(args)
    if not args.stage:
        parser.error("pass --stage, --verify or --list")
    return cmd_run(args)


if __name__ == "__main__":
    raise SystemExit(main())
