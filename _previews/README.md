# Previews

Place draft posts here to make them accessible at `/preview/<title>/` without appearing on the public blog, RSS feed, sitemap, or search engines.

Posts in this folder use the same front matter as regular `_posts/` files (e.g. `layout: distill`). The `draft_preview: true`, `sitemap: false`, and `feed: false` flags are set automatically via `_config.yml` defaults — no need to add them manually.

Preview pages also rewrite simple relative post links from `../post-slug` to `/blog/post-slug/`, so you can use the same short links in drafts and published posts.

For `layout: distill` previews, you can set `published: true` in front matter after the matching post is live under `_posts/`. When that flag is true, `/preview/<title>/` automatically redirects to `/blog/<title>/`. Keep it `false` (or omit it) while the draft is still in preview.

## Workflow

1. Write your post in `_previews/` with the same format as a regular post.
2. Push to deploy — the post will be live at `/preview/<title>/`.
3. Share the direct link for feedback.
4. After publishing the final post in `_posts/`, optionally set `published: true` in the preview file so old preview links forward to `/blog/<title>/`.
5. Move the file from `_previews/` to `_posts/` when you no longer need the preview URL.
