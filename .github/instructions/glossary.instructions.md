# Glossary Instructions (v1.x)

Scope: `_data/glossary/**`, `assets/js/glossary.js`, `_plugins/glossary_data_tag.rb`, `_sass/_distill.scss`

## What this is

An inline term-popover component for distill posts, independent of the
gem-vendored `assets/js/distillpub/*` runtime (`d-cite`/`d-footnote`), so it
survives `al_folio_distill`/`al_folio_core` upgrades untouched.

`_plugins/glossary_data_tag.rb` defines the `{% glossary_data %}` Liquid tag
that emits the `<script id="d-glossary-data">` JSON payload (wired into
`_layouts/distill.liquid` as `{% if page.glossary %}{% glossary_data %}{% endif %}`).
It's a Ruby tag rather than a plain `{% include %}` specifically so it can
call `site.regenerator.add_dependency` and register `_data/glossary/<topic>.yml`
as an explicit dependency of the page at render time -- without that, editing
only the YAML data file (not the post's own `.md`) doesn't trigger a
re-render under `--incremental`/`jekyll serve --watch`, so the page keeps
serving stale glossary JSON. `jekyll-scholar`'s `{% bibliography %}` tag
solves the identical problem for `.bib` files the same way; `_plugins/jupyter_cell_embed.rb`
in this repo does it for notebook files.

## Authoring a glossary

1. Add or edit a topic file at `_data/glossary/<topic>.yml`, a YAML list of entries:
   ```yaml
   - key: some_term_key
     term: "Display Name"
     definition: "One or two plain-text sentences."
     link: "https://example.com/optional-learn-more" # omit if there is none
   ```
2. In a post's front matter, set `glossary: <topic>` (matching the filename, no
   extension) to load that topic's data — mirrors the `bibliography: <file>.bib`
   convention.
3. In the post body, wrap the exact existing term text (do not rewrite prose)
   in `<d-glossary key="some_term_key">Display Text</d-glossary>`.

## Appendix summary

Every distill post's `<d-appendix>` includes an unconditional
`<d-glossary-list></d-glossary-list>`, right alongside `<d-footnote-list>`/
`<d-citation-list>`. It scans the page for every `<d-glossary>` key actually
used, and — if there's at least one — renders a "Glossary" heading and an
alphabetical `<ol>` of full definitions with their links, in light DOM so it
inherits this repo's existing `d-appendix h3, li, span, a` styling for free.
If a post never uses `<d-glossary>` (or doesn't set `glossary:` in its front
matter at all), the element stays invisible, exactly like an empty footnote
list — no extra guarding needed when adding new tags to a post.

## Anchors

The first occurrence of each key gets `id="d-glossary-<key>"`, so
`post-url#d-glossary-<key>` jumps to (and briefly highlights) it -- handy for
spot-checking tags. Later occurrences get no id. Each appendix entry ends with
a `↩` link back to that anchor, like the footnote list.

## Repeat-occurrence convention

Tag a term's first meaningful appearance, and only tag it again later if it
resurfaces after a real gap (a different section, not the next sentence) —
per Wikipedia's [MOS:DL "duplicate and repeat links"](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Linking#Duplicate_and_repeat_links)
convention. The component automatically renders the first occurrence of a
key on the page with the active (theme-colored) underline and every later
occurrence muted — both stay fully interactive, so a reader who lands on a
muted instance directly (e.g. via the table of contents) can still open it.

Avoid tagging inside headings or direct quotations — it can read as
editorializing inside someone else's words. Tagging inside a `<blockquote>`
is fine (confirmed working in practice).

## Validation

Use the validated command set in `AGENTS.md`. `assets/js/glossary.js` and
`_plugins/glossary_data_tag.rb` are new files (not gem-owned overrides), but
`_layouts/distill.liquid`, `_includes/distill_scripts.liquid`, and
`_sass/_distill.scss` each carry one small addition wiring this feature in —
all three are already tracked in `.al-folio-overrides.yml`; re-run
`bundle exec al-folio upgrade overrides audit` after editing any of them
further.
