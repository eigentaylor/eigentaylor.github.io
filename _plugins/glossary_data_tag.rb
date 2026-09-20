# Emits the `<script id="d-glossary-data">` JSON payload for a distill post's
# `glossary: <topic>` front matter, reading `_data/glossary/<topic>.yml` via
# `site.data`.
#
# This used to be a plain `{% include glossary_data.liquid %}` that read
# `site.data.glossary[page.glossary]` directly in Liquid. That silently broke
# under `--incremental`/`jekyll serve --watch`: Jekyll's incremental
# regenerator only re-renders a page when the page's own source file (or an
# explicitly registered dependency) changes. A post's own `.md` file doesn't
# change when someone only edits `_data/glossary/<topic>.yml` (e.g. fixing a
# definition or a Wikipedia link), so the post kept rendering its
# already-cached (now stale) glossary JSON -- reading `site.data` in a plain
# `{% include %}` gives Jekyll no way to know the post depends on that data
# file, unlike `_includes/*.liquid` files themselves, which Jekyll's own
# `include` tag *does* register as dependencies automatically.
#
# `jekyll-scholar` solves the identical problem for `bibliography: some.bib`
# by calling `site.regenerator.add_dependency` inside its `{% bibliography %}`
# Liquid::Tag at render time (see `Jekyll::Scholar::Utilities#update_dependency_tree`,
# called from `Jekyll::Scholar::BibliographyTag#render`) -- which is why
# citations/footnotes rebuild reliably under `--incremental` while the
# glossary didn't. `jupyter_cell_embed.rb` in this same `_plugins/` directory
# already uses this exact pattern for notebook files; this tag follows suit
# for glossary data files.
#
# Usage (front matter `glossary: polisci` implied): {% glossary_data %}
module Jekyll
  module Tags
    class GlossaryDataTag < Liquid::Tag
      def render(context)
        site = context.registers[:site]
        page = context.registers[:page]
        topic = page['glossary']
        return '' unless topic

        data_path = site.in_source_dir('_data', 'glossary', "#{topic}.yml")
        register_glossary_dependency(site, page, data_path)

        entries = (site.data['glossary'] || {})[topic]
        <<~HTML
          <script type="application/json" id="d-glossary-data">
            #{entries.to_json}
          </script>
        HTML
      end

      private

      def register_glossary_dependency(site, page, data_path)
        page_path = site.in_source_dir(page['path'])
        site.regenerator.add_dependency(page_path, data_path)
      end
    end
  end
end

Liquid::Template.register_tag('glossary_data', Jekyll::Tags::GlossaryDataTag)
