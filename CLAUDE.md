@AGENTS.md

## Editing Jupyter notebooks

When editing an existing `.ipynb` file in this repo, always make targeted per-cell edits (read the live file first, then replace/insert/delete specific cells) instead of regenerating the whole notebook from a separate script and overwriting the file. A full-file overwrite has no awareness of edits made directly in the notebook since the last write (e.g. in an IDE) and will silently destroy them.

## Editing blog post prose

Don't make significant changes to the prose/argument in blog posts (e.g. `_posts/`, `_previews/`) unless explicitly asked. Small, pre-approved edits are fine — fixing typos or factual errors, wording tweaks, adding citations/links/numbers when asked. Anything more substantive (new arguments, reframed sections, rewritten paragraphs) should be offered as suggested language in chat for the user to adopt or adapt themselves, not written directly into the file. The words in a post should stay the user's own, even when the surrounding technical work (data, simulations, notebooks) is AI-assisted.
