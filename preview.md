# Previews

Place draft posts here to make them accessible at `/preview/<title>/` without appearing on the public blog, RSS feed, sitemap, or search engines.

Posts in this folder use the same front matter as regular `_posts/` files (e.g. `layout: distill`). The `draft_preview: true`, `sitemap: false`, and `feed: false` flags are set automatically via `_config.yml` defaults — no need to add them manually.

## Workflow

1. Write your post in `_previews/` with the same format as a regular post.
2. Push to deploy — the post will be live at `/preview/<title>/`.
3. Share the direct link for feedback.
4. When ready to publish, move the file from `_previews/` to `_posts/`.
