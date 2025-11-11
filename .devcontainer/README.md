This devcontainer builds from the repository Dockerfile and performs a small setup when created.

What it does:
- Installs declared container features (Ruby, Node, apt packages) via devcontainer features.
- Runs `.devcontainer/postCreate.sh` after the container is created. That script:
  - Creates a Python virtual environment at `./.venv` (if Python is present)
  - Upgrades pip and installs `requirements.txt` if present
  - Runs `bundle install` if a `Gemfile` is present and `bundler` is available

How to use:
1. Make sure Docker is running.
2. In VS Code: Command Palette → "Dev Containers: Reopen in Container".
3. After the container builds, open a terminal in VS Code and activate the venv:

   - Bash (inside devcontainer): `source .venv/bin/activate`
   - PowerShell (host): `& .\.venv\Scripts\Activate.ps1`

Notes:
- The script is best-effort and won't fail the build if pip/bundle steps error; adjust `postCreate.sh` if you want stricter behavior.
- If your `Dockerfile` sets a non-standard workspace path or requires build args, update `.devcontainer/devcontainer.json` accordingly.
