#!/usr/bin/env node
// Cross-platform wrapper so `npm run notebook -- <name>` finds the repo's
// .venv Python (falling back to python3/python on PATH) and streams the
// child process's stdout/stderr straight to this terminal in real time.

const path = require("path");
const fs = require("fs");
const { spawnSync } = require("child_process");

const repoRoot = path.resolve(__dirname, "..");

function findPython() {
  const venvPython =
    process.platform === "win32"
      ? path.join(repoRoot, ".venv", "Scripts", "python.exe")
      : path.join(repoRoot, ".venv", "bin", "python");
  if (fs.existsSync(venvPython)) return venvPython;
  return process.platform === "win32" ? "python" : "python3";
}

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error("Usage: npm run notebook -- <notebook-name-or-path> [--timeout SECONDS] [--kernel NAME]");
  process.exit(1);
}

const python = findPython();
const script = path.join(repoRoot, "bin", "run_notebook.py");
const result = spawnSync(python, [script, ...args], {
  stdio: "inherit",
  cwd: repoRoot,
  env: { ...process.env, PYTHONUNBUFFERED: "1" },
});

process.exit(result.status === null ? 1 : result.status);
