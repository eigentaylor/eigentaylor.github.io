#!/usr/bin/env python
"""Copy a draft from the gitignored _scratch/ folder into _previews/, ready to commit for feedback.

    python bin/promote.py runoff-accuracy        # slug, filename, or path of a top-level _scratch/ draft
    python bin/promote.py runoff-accuracy --force   # overwrite a preview copy that was edited by hand
    python bin/promote.py --list                 # every preview and whether its _scratch/ source moved on

_scratch/ is the only place drafts are edited; a _previews/ file is a generated copy. Each copy carries a
YAML comment as the first front-matter line naming its source and the hash of what was written, so any
machine can tell whether the copy was edited by hand since (in which case promote stops and shows the diff
rather than silently throwing that edit away). Promoting only writes the file; committing and pushing it is
what puts it at /preview/<slug>/.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRATCH = REPO_ROOT / "_scratch"
PREVIEWS = REPO_ROOT / "_previews"
MARKER = re.compile(r"^# promoted from _scratch/(?P<name>\S+) sha1:(?P<hash>[0-9a-f]{40})\b.*$")


def sha1(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def read(path: Path) -> str:
    # newline="" keeps CRLF/LF exactly as on disk, so the copy matches its source byte for byte
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def write(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def split_marker(text: str) -> tuple[re.Match | None, str]:
    """(the marker match or None, the text with the marker line removed)."""
    lines = text.splitlines(keepends=True)
    if len(lines) > 1 and lines[0].rstrip("\r\n") == "---":
        match = MARKER.match(lines[1].rstrip("\r\n"))
        if match:
            return match, lines[0] + "".join(lines[2:])
    return None, text


def with_marker(name: str, text: str) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise SystemExit(f"_scratch/{name} has no front matter (it should start with ---), so it can't be a preview")
    newline = "\r\n" if lines[0].endswith("\r\n") else "\n"
    marker = (f"# promoted from _scratch/{name} sha1:{sha1(text)} -- edit the _scratch copy and rerun "
              f"bin/promote.py; this file gets overwritten{newline}")
    return lines[0] + marker + "".join(lines[1:])


def find_source(arg: str) -> Path:
    path = Path(arg)
    if path.is_file():
        path = path.resolve()
        if path.parent != SCRATCH.resolve():
            raise SystemExit(f"{arg} isn't directly in _scratch/ (drafts in subfolders like _scraps/ aren't "
                             "built; move it up into _scratch/ first)")
        return path
    slug = Path(arg).name.removesuffix(".md")
    matches = sorted(p for p in SCRATCH.glob("*.md")
                     if p.stem == slug or re.fullmatch(r"\d{4}-\d{2}-\d{2}-" + re.escape(slug), p.stem))
    if not matches:
        raise SystemExit(f"no draft matching '{arg}' directly in _scratch/")
    if len(matches) > 1:
        raise SystemExit(f"'{arg}' matches several drafts: " + ", ".join(p.name for p in matches))
    return matches[0]


def promote(arg: str, force: bool) -> int:
    source = find_source(arg)
    text = read(source)
    dest = PREVIEWS / source.name
    if dest.exists():
        current = read(dest)
        match, body = split_marker(current)
        if match and match["hash"] == sha1(text) and sha1(body) == match["hash"]:
            print(f"_previews/{dest.name} is already up to date with _scratch/{source.name}")
            return 0
        hand_edited = not match or sha1(body) != match["hash"]
        if hand_edited and not force:
            print(f"!! _previews/{dest.name} was edited directly since it was last promoted (or wasn't made by "
                  "promote). The differences, preview copy -> _scratch draft:\n")
            sys.stdout.writelines(difflib.unified_diff(
                body.splitlines(keepends=True), text.splitlines(keepends=True),
                fromfile=f"_previews/{dest.name}", tofile=f"_scratch/{source.name}"))
            print("\nCarry anything worth keeping over into the _scratch draft, then rerun with --force.")
            return 1
    write(dest, with_marker(source.name, text))
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", source.stem)
    print(f"promoted _scratch/{source.name} -> _previews/{dest.name}")
    print(f"commit and push it to put it at /preview/{slug}/")
    return 0


def list_previews() -> int:
    previews = sorted(PREVIEWS.glob("*.md"))
    previews = [p for p in previews if p.name != "README.md"]
    if not previews:
        print("no previews in _previews/")
    for dest in previews:
        match, body = split_marker(read(dest))
        source = SCRATCH / (match["name"] if match else dest.name)
        if not match:
            status = "not made by promote"
        elif sha1(body) != match["hash"]:
            status = "EDITED BY HAND since promoted"
        elif not source.exists():
            status = f"source _scratch/{source.name} is missing on this machine"
        elif sha1(read(source)) != match["hash"]:
            status = "_scratch draft has changed since (rerun promote to update)"
        else:
            status = "up to date"
        print(f"{dest.name}: {status}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Copy a _scratch/ draft into _previews/.")
    parser.add_argument("draft", nargs="?", help="slug, filename or path of a draft in _scratch/")
    parser.add_argument("--force", action="store_true", help="overwrite a hand-edited preview copy")
    parser.add_argument("--list", action="store_true", help="show every preview's status")
    args = parser.parse_args()
    if args.list:
        return list_previews()
    if not args.draft:
        parser.error("name a draft, or pass --list")
    return promote(args.draft, args.force)


if __name__ == "__main__":
    raise SystemExit(main())
