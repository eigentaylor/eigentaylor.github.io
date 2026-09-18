#!/usr/bin/env python3
"""Read a notebook's structure without loading its output.

An executed notebook is mostly base64 PNG: `vse_simulation.ipynb` is 7.9MB, of which 89%
is stored chart images, against 350KB of actual source. That makes it awkward to open in
an editor and effectively unreadable for a coding agent, which will burn its whole context
on image data before reaching any code.

    python vse_sim/tools/nb_outline.py vse_simulation.ipynb              # a map
    python vse_sim/tools/nb_outline.py vse_simulation.ipynb --cell 38    # one cell
    python vse_sim/tools/nb_outline.py vse_simulation.ipynb --source     # all source
    python vse_sim/tools/nb_outline.py vse_simulation.ipynb --tag vse-joint
    python vse_sim/tools/nb_outline.py vse_simulation.ipynb --grep run_vse_simulation
"""
import argparse
import json
import pathlib
import re


def load(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))["cells"]


def source(cell):
    return "".join(cell["source"])


def tags(cell):
    return cell.get("metadata", {}).get("tags", [])


def outline(cells, show_tags=True):
    for i, cell in enumerate(cells):
        text = source(cell)
        first = next((line for line in text.split("\n") if line.strip()), "")
        kind = "md" if cell["cell_type"] == "markdown" else "code"
        tag = ("  [" + ",".join(tags(cell)) + "]") if show_tags and tags(cell) else ""
        yield f"{i:4d} {kind:4s} {len(text):6d}  {first[:96]}{tag}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("notebook")
    ap.add_argument("--cell", type=int, action="append", help="print this cell's source")
    ap.add_argument("--tag", action="append", help="print the source of cells with this tag")
    ap.add_argument("--source", action="store_true", help="print every cell's source")
    ap.add_argument("--grep", help="list cells whose source matches this regex")
    ap.add_argument("--stats", action="store_true", help="source vs stored-output sizes")
    args = ap.parse_args(argv)
    cells = load(args.notebook)

    if args.stats:
        src = sum(len(source(c)) for c in cells)
        out = png = 0
        for cell in cells:
            for output in cell.get("outputs", []):
                for mime, value in (output.get("data") or {}).items():
                    size = len("".join(value) if isinstance(value, list) else str(value))
                    out += size
                    png += size if mime == "image/png" else 0
        print(f"cells:  {len(cells)}")
        print(f"source: {src:>12,} chars")
        print(f"output: {out:>12,} chars  ({png:,} of it base64 PNG, "
              f"{png / out * 100:.0f}%)" if out else "output: none")
        return 0

    if args.grep:
        pattern = re.compile(args.grep)
        for i, cell in enumerate(cells):
            for n, line in enumerate(source(cell).split("\n"), 1):
                if pattern.search(line):
                    print(f"{i:4d}:{n:<4d} {line.strip()[:110]}")
        return 0

    wanted = list(args.cell or [])
    for tag in args.tag or []:
        wanted += [i for i, c in enumerate(cells) if tag in tags(c)]
    if args.source:
        wanted = range(len(cells))

    if not wanted:
        print("\n".join(outline(cells)))
        return 0

    for i in wanted:
        tag = ("  tags=" + ",".join(tags(cells[i]))) if tags(cells[i]) else ""
        print(f"{'=' * 30} cell {i} ({cells[i]['cell_type']}){tag}")
        print(source(cells[i]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
