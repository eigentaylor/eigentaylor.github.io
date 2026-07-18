@AGENTS.md

## Editing Jupyter notebooks

When editing an existing `.ipynb` file in this repo, always make targeted per-cell edits (read the live file first, then replace/insert/delete specific cells) instead of regenerating the whole notebook from a separate script and overwriting the file. A full-file overwrite has no awareness of edits made directly in the notebook since the last write (e.g. in an IDE) and will silently destroy them.
