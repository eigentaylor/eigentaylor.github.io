#!/usr/bin/env bash
set -euo pipefail

echo "Running devcontainer postCreate: create venv, install python requirements, run bundle if needed"

PYTHON=${PYTHON:-python3}
VENV_DIR=".venv"

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "Python not found as $PYTHON, trying python..."
  PYTHON=python
fi

if command -v "$PYTHON" >/dev/null 2>&1; then
  echo "Creating venv at $VENV_DIR using $PYTHON"
  "$PYTHON" -m venv "$VENV_DIR" || true
  echo "Upgrading pip and installing requirements if present"
  "$VENV_DIR/bin/python" -m pip install --upgrade pip || true
  if [ -f requirements.txt ]; then
    "$VENV_DIR/bin/python" -m pip install -r requirements.txt || true
  fi
else
  echo "No python found; skipping venv creation"
fi

if [ -f Gemfile ]; then
  if command -v bundle >/dev/null 2>&1; then
    echo "Running bundle install"
    bundle install || true
  else
    echo "Bundler not found; install bundler to manage Ruby dependencies"
  fi
fi

echo "postCreate complete"
