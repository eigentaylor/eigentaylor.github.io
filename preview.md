# Previews

Place draft posts here to make them accessible at `/preview/<title>/` without appearing on the public blog, RSS feed, sitemap, or search engines.

Posts in this folder use the same front matter as regular `_posts/` files (e.g. `layout: distill`). The `draft_preview: true`, `sitemap: false`, `feed: false`, and `preview_redirect: true` flags are set automatically via `_config.yml` defaults — no need to add them manually.

Preview pages also rewrite simple relative post links from `../post-slug` to `/blog/post-slug/`, so you can use the same short links in drafts and published posts.

For `layout: distill` previews, redirecting is controlled by `preview_redirect` (defaults to `true` for `_previews`). A preview will only redirect from `/preview/<title>/` to `/blog/<title>/` if a matching post URL exists under `_posts/`; otherwise it keeps rendering the preview page.

`published` is a built-in Jekyll key for generation visibility. Setting `published: false` prevents a document from being generated at all, including previews.

## Workflow

1. Write your post in `_previews/` with the same format as a regular post.
2. Push to deploy — the post will be live at `/preview/<title>/`.
3. Share the direct link for feedback.
4. After publishing the final post in `_posts/`, the preview link will automatically start forwarding to `/blog/<title>/` (as long as `preview_redirect` is left true).
5. Move the file from `_previews/` to `_posts/` when you no longer need the preview URL.
