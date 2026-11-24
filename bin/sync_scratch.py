#!/usr/bin/env python
"""Keep the gitignored _scratch/ drafts folder in sync with pCloud (P:\\blog), both ways.

    python bin/sync_scratch.py sync     # pull what changed on pCloud, push what changed here
    python bin/sync_scratch.py pull     # only bring pCloud's changes here
    python bin/sync_scratch.py push     # only send this machine's changes up
        --quiet           print only when something was copied, deleted or went wrong
        --allow-deletes   let a run delete more files than the safety limit (see below)

You rarely run it by hand: _plugins/scratch_sync.rb runs `sync` when the Jekyll dev server starts and
`push --quiet` after every rebuild, so saving a draft while `npm start` is running sends it to pCloud.
`npm run pull` is for picking up another machine's edits while a server is already running here (the
pulled files trigger an ordinary rebuild).

How it decides: .scratch-sync/state.json (per machine, gitignored) records each file's content hash as of
the last time both sides agreed. Against that base, a file that changed only here is pushed, one that
changed only on pCloud is pulled, and one that changed on both sides is a conflict: the pCloud version is
saved next to yours as `<name>.conflict-<time>-pcloud.<ext>`, yours is kept and pushed, and both end up
on both sides. A file deleted on one side and edited on the other is kept. Nothing is ever deleted
outright: files removed from pCloud go to P:\\blog\\.trash\\<time>\\, files removed here go to
.scratch-sync/trash/<time>/. A run that would delete more than a handful of files (pCloud Drive briefly
showing an empty folder looks exactly like "everything was deleted") skips the deletions and says so;
rerun with --allow-deletes if they're real.

The remote is P:\\blog unless SCRATCH_REMOTE says otherwise. If its drive isn't there (pCloud not running)
the script says so and exits 0, so a dev server never fails because of it.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
# SCRATCH_LOCAL / SCRATCH_STATE exist for testing against throwaway folders.
LOCAL_ROOT = Path(os.environ.get("SCRATCH_LOCAL") or REPO_ROOT / "_scratch")
STATE_DIR = Path(os.environ.get("SCRATCH_STATE") or REPO_ROOT / ".scratch-sync")
STATE_FILE = STATE_DIR / "state.json"
LOCK_FILE = STATE_DIR / "lock"
LOCAL_TRASH = STATE_DIR / "trash"
DEFAULT_REMOTE = r"P:\blog"
REMOTE_TRASH = ".trash"
TMP_SUFFIX = ".scratch-sync-tmp"

IGNORED_DIRS = {".git", "__pycache__", ".ipynb_checkpoints", REMOTE_TRASH}
IGNORED_FILES = ["~$*", "*.tmp", "*" + TMP_SUFFIX, "Thumbs.db", "desktop.ini", ".DS_Store", "*.swp", ".~lock.*"]

# Deletion guard: more deletions than this in one run are skipped unless --allow-deletes.
MAX_DELETES = 5
MAX_DELETE_FRACTION = 0.25

LOCK_WAIT_SECONDS = 30
LOCK_STALE_SECONDS = 120


def stamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def walk(root: Path) -> dict[str, tuple[str, list[int]]]:
    """{casefolded relative path: (relative path as spelled on disk, [size, mtime_ns])}.

    Keys are casefolded because both sides are case-insensitive filesystems: a file renamed only in case
    is the same file, not a deletion plus a new file."""
    found: dict[str, tuple[str, list[int]]] = {}
    if not root.is_dir():
        return found
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for name in filenames:
            if any(fnmatch.fnmatch(name, pattern) for pattern in IGNORED_FILES):
                continue
            full = Path(dirpath) / name
            try:
                st = full.stat()
            except OSError:
                continue
            rel = full.relative_to(root).as_posix()
            found[rel.casefold()] = (rel, [st.st_size, st.st_mtime_ns])
    return found


def file_hash(path: Path) -> str:
    digest = hashlib.sha1()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stat_of(path: Path) -> list[int]:
    st = path.stat()
    return [st.st_size, st.st_mtime_ns]


def copy_file(src: Path, dest: Path) -> None:
    """Copy through a temp file so a half-written file is never seen under the real name."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + TMP_SUFFIX)
    shutil.copy2(src, tmp)
    os.replace(tmp, dest)


def to_trash(path: Path, root: Path, trash_root: Path) -> Path:
    target = trash_root / path.relative_to(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(target))
    return target


class Lock:
    """One sync at a time per machine: rapid saves each spawn a push, and they mustn't interleave."""

    def __init__(self) -> None:
        self.held = False

    def __enter__(self) -> "Lock":
        STATE_DIR.mkdir(exist_ok=True)
        deadline = time.monotonic() + LOCK_WAIT_SECONDS
        while True:
            try:
                fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                self.held = True
                return self
            except FileExistsError:
                try:
                    if time.time() - LOCK_FILE.stat().st_mtime > LOCK_STALE_SECONDS:
                        LOCK_FILE.unlink()  # left behind by a run that was killed
                        continue
                except FileNotFoundError:
                    continue
                if time.monotonic() > deadline:
                    return self
                time.sleep(0.25)

    def __exit__(self, *exc: object) -> None:
        if self.held:
            try:
                LOCK_FILE.unlink()
            except FileNotFoundError:
                pass


def load_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {"files": {}}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(exist_ok=True)
    tmp = STATE_FILE.with_name(STATE_FILE.name + TMP_SUFFIX)
    tmp.write_text(json.dumps(state, indent=1, sort_keys=True), encoding="utf-8")
    os.replace(tmp, STATE_FILE)


class Sync:
    def __init__(self, remote_root: Path, mode: str, quiet: bool, allow_deletes: bool) -> None:
        self.remote_root = remote_root
        self.mode = mode
        self.quiet = quiet
        self.allow_deletes = allow_deletes
        self.state = load_state()
        self.base: dict[str, dict] = self.state.setdefault("files", {})
        self.time = stamp()
        self.actions: list[str] = []
        self.warnings: list[str] = []
        self.errors: list[str] = []

    # --- hashing with the base as a cache ---------------------------------------------------------

    def current_hash(self, key: str, side: str, rel: str, stat: list[int]) -> str:
        """A side whose size and mtime match what the base recorded for it still has the base's content."""
        entry = self.base.get(key)
        if entry and entry.get(side) == stat:
            return entry["hash"]
        root = LOCAL_ROOT if side == "local" else self.remote_root
        return file_hash(root / rel)

    def record(self, key: str, rel: str, digest: str, local_stat: list[int] | None,
               remote_stat: list[int] | None) -> None:
        """Set the base. Pass a side's stat only if that side's content is `digest`, else it gets re-hashed."""
        self.base[key] = {"path": rel, "hash": digest, "local": local_stat, "remote": remote_stat}

    # --- the actions ------------------------------------------------------------------------------

    def pull(self, key: str, rel: str, digest: str, verb: str = "pulled") -> None:
        copy_file(self.remote_root / rel, LOCAL_ROOT / rel)
        self.record(key, rel, digest, stat_of(LOCAL_ROOT / rel), stat_of(self.remote_root / rel))
        self.actions.append(f"{verb} {rel}")

    def push(self, key: str, rel: str, digest: str, verb: str = "pushed") -> None:
        copy_file(LOCAL_ROOT / rel, self.remote_root / rel)
        self.record(key, rel, digest, stat_of(LOCAL_ROOT / rel), stat_of(self.remote_root / rel))
        self.actions.append(f"{verb} {rel}")

    def conflict(self, key: str, local_rel: str, remote_rel: str, local_hash: str, remote_hash: str) -> None:
        """Both sides changed: keep pCloud's version next to this machine's, which then wins the name."""
        path = Path(local_rel)
        copy_rel = path.with_name(f"{path.stem}.conflict-{self.time}-pcloud{path.suffix}").as_posix()
        copy_file(self.remote_root / remote_rel, LOCAL_ROOT / copy_rel)
        # The base is now pCloud's version (it's been seen and kept), so this machine's version counts as the
        # newer change and goes up on the push below or the next one.
        self.record(key, local_rel, remote_hash, None, stat_of(self.remote_root / remote_rel))
        self.warnings.append(f"CONFLICT {local_rel}: edited on both sides since the last sync. Kept this "
                             f"machine's version; pCloud's is saved as {copy_rel}")
        if self.mode != "pull":
            self.push(key, local_rel, local_hash)
            self.push(copy_rel.casefold(), copy_rel, remote_hash)

    # --- one pass ---------------------------------------------------------------------------------

    def run(self) -> None:
        local = walk(LOCAL_ROOT)
        remote = walk(self.remote_root)
        do_pull = self.mode in ("pull", "sync")
        do_push = self.mode in ("push", "sync")
        deletes: list[tuple[str, str, str]] = []  # (key, "local"|"remote", rel)

        for key in sorted(set(local) | set(remote) | set(self.base)):
            entry = self.base.get(key)
            b = entry["hash"] if entry else None
            l_rel, l_stat = local.get(key, (None, None))
            r_rel, r_stat = remote.get(key, (None, None))
            try:
                l = self.current_hash(key, "local", l_rel, l_stat) if l_rel else None
                r = self.current_hash(key, "remote", r_rel, r_stat) if r_rel else None
            except OSError as exc:
                self.errors.append(f"couldn't read {key}: {exc}")
                continue
            try:
                if l == r:
                    if l is None:
                        self.base.pop(key, None)  # gone from both sides
                    else:
                        self.record(key, l_rel, l, l_stat, r_stat)
                elif l == b:  # only pCloud changed
                    if not do_pull:
                        continue
                    if r is None:
                        deletes.append((key, "local", l_rel))
                    else:
                        self.pull(key, r_rel, r)
                elif r == b:  # only this machine changed
                    if not do_push:
                        continue
                    if l is None:
                        deletes.append((key, "remote", r_rel))
                    else:
                        self.push(key, l_rel, l)
                elif l is None:  # deleted here, edited on pCloud: keep the edit
                    if do_pull:
                        self.pull(key, r_rel, r, verb="restored (edited on pCloud after it was deleted here)")
                elif r is None:  # deleted on pCloud, edited here: keep the edit
                    if do_push:
                        self.push(key, l_rel, l, verb="restored to pCloud (edited here after it was deleted there)")
                else:
                    self.conflict(key, l_rel, r_rel, l, r)
            except OSError as exc:
                self.errors.append(f"couldn't sync {key}: {exc}")

        self.apply_deletes(deletes)
        save_state(self.state)

    def apply_deletes(self, deletes: list[tuple[str, str, str]]) -> None:
        if not deletes:
            return
        tracked = max(len(self.base), 1)
        if not self.allow_deletes and (len(deletes) > MAX_DELETES or
                                       (tracked >= 4 and len(deletes) > MAX_DELETE_FRACTION * tracked)):
            where = sorted({side for _, side, _ in deletes})
            self.warnings.append(
                f"skipped {len(deletes)} deletion(s) ({' and '.join(where)}), more than the safety limit: "
                + ", ".join(rel for _, _, rel in deletes[:8]) + (" ..." if len(deletes) > 8 else "")
                + ". If those files really were deleted, run: python bin/sync_scratch.py sync --allow-deletes")
            return
        for key, side, rel in deletes:
            try:
                if side == "local":
                    target = to_trash(LOCAL_ROOT / rel, LOCAL_ROOT, LOCAL_TRASH / self.time)
                    self.actions.append(f"removed {rel} here (deleted on pCloud; kept in {target})")
                else:
                    to_trash(self.remote_root / rel, self.remote_root, self.remote_root / REMOTE_TRASH / self.time)
                    self.actions.append(f"removed {rel} from pCloud (deleted here; kept in "
                                        f"{REMOTE_TRASH}/{self.time}/ there)")
                self.base.pop(key, None)
            except OSError as exc:
                self.errors.append(f"couldn't remove {rel} ({side}): {exc}")

    def report(self) -> None:
        for line in self.actions:
            print(f"scratch-sync: {line}")
        for line in self.warnings:
            print(f"scratch-sync: !! {line}")
        for line in self.errors:
            print(f"scratch-sync: !! ERROR {line}", file=sys.stderr)
        if not (self.actions or self.warnings or self.errors or self.quiet):
            print(f"scratch-sync: up to date ({len(self.base)} files, {self.mode} with {self.remote_root})")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync _scratch/ with pCloud.")
    parser.add_argument("mode", choices=["sync", "pull", "push"])
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--allow-deletes", action="store_true")
    args = parser.parse_args()

    remote_root = Path(os.environ.get("SCRATCH_REMOTE") or DEFAULT_REMOTE)
    if not Path(remote_root.anchor or remote_root).exists():
        print(f"scratch-sync: !! {remote_root.anchor} isn't available (is pCloud running?), so nothing was synced")
        return 0

    with Lock() as lock:
        if not lock.held:
            print("scratch-sync: !! another sync has held the lock for over "
                  f"{LOCK_WAIT_SECONDS}s, so this {args.mode} was skipped (the next one will catch up)")
            return 0
        state_files = load_state().get("files", {})
        if not remote_root.is_dir():
            if state_files:
                print(f"scratch-sync: !! {remote_root} has disappeared but this machine has synced with it "
                      "before, so nothing was done. If it was moved or deleted on purpose, delete "
                      f"{STATE_FILE} and run again.")
                return 1
            remote_root.mkdir(parents=True)
        LOCAL_ROOT.mkdir(exist_ok=True)
        sync = Sync(remote_root, args.mode, args.quiet, args.allow_deletes)
        sync.run()
        sync.report()
        return 1 if sync.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
