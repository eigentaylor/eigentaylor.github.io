@AGENTS.md

## Editing Jupyter notebooks

When editing an existing `.ipynb` file in this repo, always make targeted per-cell edits (read the live file first, then replace/insert/delete specific cells) instead of regenerating the whole notebook from a separate script and overwriting the file. A full-file overwrite has no awareness of edits made directly in the notebook since the last write (e.g. in an IDE) and will silently destroy them.

## Prettier-checking new or edited files

`npm run lint:prettier` (`prettier . --check`, per AGENTS.md's validated command set) only reports files Prettier can actually parse — it silently skips extensions with no parser (`.py`, etc.), so a broken new script of an unsupported type won't show up there and needs a different check. Whenever you add or edit a file with a Prettier-supported extension (`.js`, `.json`, `.yml`/`.yaml`, `.css`/`.scss`, `.html`, `.liquid`, and anything else `.prettierrc`/`.prettierignore` cover), explicitly run `npx prettier --check <path>` on it yourself before calling the task done — don't rely on having eyeballed the project-wide run.

This checkout has `core.autocrlf=true`, so files sit as CRLF on disk locally while the committed blob is LF (`git show HEAD:<path>` confirms it) — Windows-only local `--check` runs can report a "warn" on a file that is otherwise correctly formatted, purely from that EOL mismatch, and it will check out and pass fine in CI. Don't take a local `--check` warning at face value: diff `npx prettier <path>` output against the file's real content (or run `--write` and check `git diff` afterward) to see whether anything besides line endings actually changed before concluding there's a real formatting issue.

## Editing blog post prose

Don't make significant changes to the prose/argument in blog posts (e.g. `_posts/`, `_previews/`) unless explicitly asked. Small, pre-approved edits are fine — fixing typos or factual errors, wording tweaks, adding citations/links/numbers when asked. Anything more substantive (new arguments, reframed sections, rewritten paragraphs) should be offered as suggested language in chat for the user to adopt or adapt themselves, not written directly into the file. The words in a post should stay the user's own, even when the surrounding technical work (data, simulations, notebooks) is AI-assisted.
