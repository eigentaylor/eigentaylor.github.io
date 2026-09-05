#!/usr/bin/env python
"""Execute a Jupyter notebook from the console with live progress and streamed output.

Runs entirely as an OS process detached from any editor UI, so it keeps
executing at full speed even when the terminal window loses focus (unlike
the VS Code notebook UI, which can stall in the background). All of the
notebook's print/stdout output is streamed live as it's produced, and a
one-line progress status ("cell 50/150 558s/800s") is printed on a fixed
interval (default: every 60s) regardless of how long the current cell runs.

Usage:
    python bin/run_notebook.py vse_simulation
    python bin/run_notebook.py assets/jupyter/vse_simulation.ipynb --timeout 3600

The notebook is saved back to its original path after every cell (and on
error or Ctrl-C), so a long run that fails partway through does not lose
the outputs already computed.
"""

from __future__ import annotations

import argparse
import re
import sys
import threading
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

REPO_ROOT = Path(__file__).resolve().parent.parent
JUPYTER_DIR = REPO_ROOT / "assets" / "jupyter"

# On Windows, stdout/stderr default to the legacy ANSI codepage when not
# attached to a real console (e.g. piped or redirected), which crashes on
# any non-ASCII character a notebook prints. Force UTF-8 unconditionally.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


def resolve_notebook_path(name_or_path: str) -> Path:
    p = Path(name_or_path)
    if p.suffix != ".ipynb":
        p = p.with_suffix(".ipynb")
    if not p.exists() and not p.is_absolute():
        candidate = JUPYTER_DIR / p.name
        if candidate.exists():
            return candidate
    if not p.exists():
        raise FileNotFoundError(f"Notebook not found: {name_or_path!r} (looked in {JUPYTER_DIR})")
    return p


def fmt_secs(seconds: float) -> str:
    return f"{seconds:.0f}s"


def display_path(p: Path) -> Path:
    try:
        return p.relative_to(REPO_ROOT)
    except ValueError:
        return p


class ProgressNotebookClient(NotebookClient):
    """NotebookClient that streams output live and prints progress on a timer."""

    def __init__(self, nb, progress_interval: float = 60.0, **kw):
        super().__init__(nb, **kw)
        self.total_cells = len(nb.cells)
        self.progress_interval = progress_interval
        self.run_start: float | None = None
        self.cell_start: float | None = None
        self.current_cell_index: int | None = None
        self._stop_event = threading.Event()
        self._progress_thread: threading.Thread | None = None
        self.on_notebook_start = self._on_notebook_start
        self.on_notebook_complete = self._on_notebook_complete
        self.on_cell_start = self._on_cell_start

    def _on_notebook_start(self, notebook):
        self.run_start = time.monotonic()
        self._stop_event.clear()
        self._progress_thread = threading.Thread(target=self._progress_loop, daemon=True)
        self._progress_thread.start()

    def _on_notebook_complete(self, notebook):
        self._stop_event.set()
        if self._progress_thread is not None:
            self._progress_thread.join(timeout=2)

    def _on_cell_start(self, cell, cell_index):
        if cell.cell_type != "code":
            return
        self.cell_start = time.monotonic()
        self.current_cell_index = cell_index

    def _progress_loop(self):
        while not self._stop_event.wait(self.progress_interval):
            self._print_progress()

    def _print_progress(self):
        if self.current_cell_index is None or self.cell_start is None or self.run_start is None:
            return
        now = time.monotonic()
        cell_dur = now - self.cell_start
        total_dur = now - self.run_start
        print(
            f"[progress] cell {self.current_cell_index + 1}/{self.total_cells} "
            f"{fmt_secs(cell_dur)}/{fmt_secs(total_dur)}",
            flush=True,
        )

    def output(self, outs, msg, display_id, cell_index):
        msg_type = msg["msg_type"]
        content = msg["content"]
        if msg_type == "stream":
            sys.stdout.write(content.get("text", ""))
            sys.stdout.flush()
        elif msg_type == "error":
            sys.stdout.write("\n".join(content.get("traceback", [])) + "\n")
            sys.stdout.flush()
        elif msg_type in ("execute_result", "display_data"):
            data = content.get("data", {})
            text = data.get("text/markdown") or data.get("text/plain")
            is_bare_repr = bool(re.match(r"^<IPython\.core\.display\.\w+ object>$", (text or "").strip()))
            if text and not is_bare_repr:
                sys.stdout.write(text + "\n")
                sys.stdout.flush()
        return super().output(outs, msg, display_id, cell_index)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("notebook", help="Notebook name (e.g. vse_simulation) or path to a .ipynb file")
    parser.add_argument("--timeout", type=int, default=None, help="Per-cell timeout in seconds (default: none)")
    parser.add_argument("--kernel", default=None, help="Kernel name override (default: notebook's own kernelspec)")
    parser.add_argument(
        "--progress-interval",
        type=float,
        default=60.0,
        help="Seconds between progress status lines (default: 60)",
    )
    args = parser.parse_args()

    nb_path = resolve_notebook_path(args.notebook)
    nb = nbformat.read(nb_path, as_version=4)
    code_cells = sum(1 for c in nb.cells if c.cell_type == "code")

    print(f"Executing {display_path(nb_path)}: {len(nb.cells)} cells, {code_cells} code cells")

    extra_kw = {"kernel_name": args.kernel} if args.kernel else {}
    client = ProgressNotebookClient(
        nb,
        progress_interval=args.progress_interval,
        timeout=args.timeout,
        resources={"metadata": {"path": str(nb_path.parent)}},
        **extra_kw,
    )

    exit_code = 0
    try:
        client.execute()
    except CellExecutionError as exc:
        print(f"\n!! Notebook execution failed: {exc}", file=sys.stderr)
        exit_code = 1
    except KeyboardInterrupt:
        print("\n!! Interrupted by user, saving partial progress...", file=sys.stderr)
        exit_code = 130
    finally:
        nbformat.write(nb, nb_path)
        total = time.monotonic() - client.run_start if client.run_start else 0.0
        print(f"Notebook saved to {display_path(nb_path)} (total time {fmt_secs(total)})")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
