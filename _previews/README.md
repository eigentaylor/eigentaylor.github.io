# Previews

Posts in this folder are live at `/preview/<title>/` without appearing on the public blog, RSS feed, sitemap, or search engines. They are **public to anyone with the link, and to anyone reading this repo**, so this folder only holds drafts that are ready for feedback.

Drafting happens in `_scratch/` instead (see below). Each `.md` here is a copy written by `bin/promote.py`, so don't edit these files directly. VS Code opens them read-only, and promote refuses to overwrite one that was edited by hand.

## Drafting in `_scratch/` (local only)

`_scratch/` is gitignored and never reaches GitHub. Instead it is synced to pCloud (`P:\blog`) by `bin/sync_scratch.py`:

- **When the dev server starts** (`npm start`, or the VS Code "Jekyll Serve" task), it does a full sync before the first build.
- **After every rebuild**, meaning each time you save a draft while the server runs, it pushes what changed.
- **`npm run pull`** brings in another machine's edits while a server is already running here. The pulled files trigger a normal rebuild.
- **`npm run sync`** pulls and pushes without a server running. You can also run either one from VS Code with Tasks: Run Task.

Drafts render locally at `/scratch/<title>/` with the same draft banner and live-update behavior as previews, and they show up in the local `/blog/` listing. Subfolders whose names start with `_` (like `_scratch/_scraps/`, which holds old drafts and notes) are synced but not built. Move a file up into `_scratch/` to work on it.

If a file was edited on both machines between syncs, the pCloud version is saved next to yours as `<name>.conflict-<time>-pcloud.md` and both are kept. Deleted files go to `P:\blog\.trash\` or `.scratch-sync/trash\`, never straight to oblivion. The script's docstring has the details.

## Workflow

1. Write the post in `_scratch/` with the same front matter as a regular post (e.g. `layout: distill`).
2. When it's ready for feedback, run `npm run promote -- <slug>` (e.g. `npm run promote -- runoff-accuracy`). This copies it here.
3. Commit and push the copy. The post goes live at `/preview/<title>/`, and you can share that link.
4. Keep editing in `_scratch/`, and rerun promote and push again whenever reviewers should see the update. `npm run promote -- --list` shows which previews are behind their drafts.
5. After publishing the final post in `_posts/`, the preview link automatically starts forwarding to `/blog/<title>/`, as long as `preview_redirect` is left true.
6. Delete the file from `_previews/` once you no longer need the preview URL.

## Details

The `draft_preview: true`, `sitemap: false`, `feed: false`, and `preview_redirect: true` flags are set automatically by the `_config.yml` defaults, so you don't need to add them. `_scratch/` gets the same defaults apart from the redirect.

Preview and scratch pages also rewrite simple relative post links from `../post-slug` to `/blog/post-slug/`, so drafts and published posts can use the same short links.

For `layout: distill` previews, redirecting is controlled by `preview_redirect`. A preview only redirects from `/preview/<title>/` to `/blog/<title>/` if a matching post URL exists under `_posts/`. Otherwise it keeps rendering the preview page.

`published` is a built-in Jekyll key that controls whether a document is generated. Setting `published: false` stops a document from being generated at all, including previews.
