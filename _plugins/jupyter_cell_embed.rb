require 'json'
require 'base64'
require 'fileutils'
require 'shellwords'
require 'cgi'
require 'digest'

# Extracts specific Jupyter notebook cell outputs (chart images and markdown tables) at
# Jekyll build time, so a post always reflects the notebook's last-saved run instead of a
# hand-copied snapshot that goes stale the moment the notebook is rerun or edited.
#
# Cells are targeted by nbformat cell *tags* (metadata.tags, set via JupyterLab's Cell Tags
# panel), not by cell index/position -- tags survive cells being reordered, inserted, or
# deleted elsewhere in the notebook, whereas a position-based lookup would silently break.
#
# Usage: {% jupyter_cell_embed "assets/jupyter/notebook.ipynb" tag="some-cell-tag" %}
#        {% jupyter_cell_embed "assets/jupyter/notebook.ipynb" tag="some-cell-tag" mode="images" %}
#        {% jupyter_cell_embed "assets/jupyter/notebook.ipynb" tag="some-cell-tag" mode="tables" %}
#
# All cells sharing `tag` are visited in notebook order, replaying each cell's own outputs
# in sequence: `text/markdown` outputs (headings, tables) are converted to HTML with the
# site's own Markdown converter and emitted directly; `image/png` outputs are buffered and
# flushed as a single swipeable `.pswp-gallery` div (the same markup/lightbox already used
# elsewhere in this site, wired by the `al_img_tools` gem's PhotoSwipe integration) the
# moment a non-image output -- or the end of input -- is reached. A run of consecutive
# images across cells sharing one tag (e.g. two different cells each producing one chart)
# therefore becomes a single multi-image gallery.
#
# `mode` (optional, defaults to "all"): "images" suppresses the markdown headings/tables and
# emits only the galleries -- since the tables/headings that would otherwise mark a boundary
# are hidden, every image for the tag merges into ONE swipeable gallery instead of one per
# hidden boundary. "tables" suppresses the images and emits only the converted markdown
# (tables can still get very wide/tall for a blog layout -- this is the escape hatch for
# that). In the default "all" mode, boundaries follow the cell's own original structure: a
# table still ends the preceding image run, so each heading/table gets its own gallery.
#
# A missing notebook, a notebook that fails to parse, or a tag with zero matching cells all
# raise (failing the build loudly) rather than silently rendering nothing -- a deleted or
# renamed tag should be caught at build time, not discovered by a missing chart in prod.
# A tag that *does* match a cell but whose matched cell(s) have no output yet (edited params,
# not re-run -- the notebook takes ~1hr to run, so this is a normal mid-edit state, not an
# error) renders a visible "pending" placeholder instead, so the post stays buildable while
# a run is pending.
#
# Two `--incremental`/`jekyll serve --watch` correctness fixes live here too, found while
# investigating charts silently disappearing between edits:
#   1. This tag reads the notebook file directly via `File.read`, so Jekyll has no built-in way
#      to know a post depends on it. `site.regenerator.add_dependency` registers that
#      relationship explicitly, so editing/re-running the notebook alone (without also
#      touching the post's own .md) correctly triggers a re-render of every post embedding it.
#   2. The generated PNGs only exist in `site.static_files` for regeneration cycles where this
#      tag actually executes (i.e. the owning post gets re-rendered). On any *other* file's
#      incremental rebuild, Jekyll's cleaner deletes destination files that aren't part of that
#      cycle's in-memory file list -- which silently wipes out a post's previously-generated
#      charts the moment some unrelated file changes elsewhere in the repo. Registering the
#      notebook's image directory in `site.keep_files` (Jekyll's own escape hatch for
#      generated-but-not-source-tracked output) opts it out of that sweep entirely.
module Jekyll
  # Writes decoded PNG bytes straight into the destination directory at build time. These
  # images exist only as base64 blobs inside the notebook's own stored outputs -- nothing is
  # ever read from or written to the source tree, so there is nothing new to commit or
  # gitignore. Overrides `modified?`/`write` entirely (rather than delegating to the base
  # class, which stats a real source-file path) since there is no backing file on disk.
  class NotebookCellImageFile < StaticFile
    def initialize(site, base, dir, name, png_bytes)
      super(site, base, dir, name)
      @png_bytes = png_bytes
    end

    def modified?
      true
    end

    def write(dest)
      dest_path = destination(dest)
      FileUtils.mkdir_p(File.dirname(dest_path))
      File.open(dest_path, 'wb') { |f| f.write(@png_bytes) }
      true
    end
  end

  module Tags
    class JupyterCellEmbedTag < Liquid::Tag
      NOTEBOOK_CACHE = {}

      def initialize(tag_name, markup, parse_context)
        super
        @markup = markup.strip
      end

      def render(context)
        site = context.registers[:site]
        notebook_rel_path, cell_tag, mode = parse_markup(@markup)
        notebook_abs_path = File.join(site.source, notebook_rel_path)

        register_notebook_dependency(site, context, notebook_abs_path)

        notebook = load_notebook(notebook_abs_path)
        cells = matching_cells(notebook, cell_tag)
        converter = site.find_converter_instance(Jekyll::Converters::Markdown)

        html_parts = []
        pending_images = []
        last_heading = nil
        gallery_index = 0

        flush = lambda do
          next if pending_images.empty?

          gallery_index += 1
          html_parts << render_gallery(site, notebook_rel_path, cell_tag, gallery_index, pending_images)
          pending_images = []
        end

        cells.each do |cell|
          (cell['outputs'] || []).each do |output|
            data = output['data'] || {}
            if data['image/png']
              unless mode == 'tables'
                pending_images << { bytes: Base64.decode64(join_text(data['image/png'])), alt: last_heading }
              end
            elsif data['text/markdown']
              # In images-only mode, a table/heading boundary is invisible to the reader (it
              # isn't rendered), so it shouldn't split the gallery either -- every image for
              # this tag merges into one swipeable gallery instead of one per hidden boundary.
              flush.call unless mode == 'images'
              md_text = join_text(data['text/markdown'])
              unless mode == 'images'
                converted = converter.convert(md_text)
                converted = "<div class=\"table-responsive\">#{converted}</div>" if converted.include?('<table')
                html_parts << converted
              end
              heading = md_text[/^#+\s+(.+)$/, 1]
              last_heading = heading.strip if heading
            end
          end
        end
        flush.call

        # Cell(s) matched the tag, but none of them currently carry the kind of output `mode`
        # asked for -- most commonly because the notebook was edited (params changed) and
        # hasn't been re-run yet. That's a normal, expected mid-edit state given the ~1hr run
        # time, not a build error, so show it rather than silently leaving a gap in the post.
        html_parts << pending_placeholder(cell_tag, mode) if html_parts.empty?

        html_parts.join("\n")
      end

      private

      def register_notebook_dependency(site, context, notebook_abs_path)
        page_path = site.in_source_dir(context.registers[:page]["path"])
        site.regenerator.add_dependency(page_path, notebook_abs_path)
      end

      def pending_placeholder(cell_tag, mode)
        kind = mode == 'tables' ? 'table' : 'chart'
        <<~HTML
          <div class="jupyter-cell-embed-pending" style="background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 12px 20px; margin: 1em 0; font-size: 0.95rem; color: #664d03;">
            ⏳ <strong>#{CGI.escapeHTML(kind.capitalize)} pending</strong> &mdash; cell(s) tagged <code>#{CGI.escapeHTML(cell_tag)}</code> have no saved output yet. Re-run and save the notebook to fill this in.
          </div>
        HTML
      end

      def join_text(value)
        value.is_a?(Array) ? value.join : value.to_s
      end

      VALID_MODES = %w[all images tables].freeze

      def parse_markup(markup)
        tokens = Shellwords.split(markup)
        path = nil
        cell_tag = nil
        mode = 'all'
        tokens.each do |tok|
          if tok =~ /\Atag=(.+)\z/
            cell_tag = Regexp.last_match(1)
          elsif tok =~ /\Amode=(.+)\z/
            mode = Regexp.last_match(1)
          elsif path.nil?
            path = tok
          end
        end

        if path.nil? || path.empty? || cell_tag.nil? || cell_tag.empty?
          raise "jupyter_cell_embed: expected `jupyter_cell_embed \"path/to/notebook.ipynb\" " \
                "tag=\"cell-tag\"`, got `#{markup}`"
        end
        unless VALID_MODES.include?(mode)
          raise "jupyter_cell_embed: mode=\"#{mode}\" is invalid, expected one of #{VALID_MODES.join(', ')}"
        end

        [path, cell_tag, mode]
      end

      def load_notebook(abs_path)
        raise "jupyter_cell_embed: notebook not found at #{abs_path}" unless File.file?(abs_path)

        mtime = File.mtime(abs_path)
        cached = NOTEBOOK_CACHE[abs_path]
        return cached[1] if cached && cached[0] == mtime

        notebook = JSON.parse(File.read(abs_path, encoding: 'utf-8'))
        NOTEBOOK_CACHE[abs_path] = [mtime, notebook]
        notebook
      rescue JSON::ParserError => e
        raise "jupyter_cell_embed: failed to parse notebook JSON at #{abs_path}: #{e.message}"
      end

      def matching_cells(notebook, cell_tag)
        all_cells = notebook['cells'] || []
        cells = all_cells.select { |cell| Array(cell.dig('metadata', 'tags')).include?(cell_tag) }
        return cells unless cells.empty?

        all_tags = all_cells.flat_map { |c| Array(c.dig('metadata', 'tags')) }.uniq.sort
        raise "jupyter_cell_embed: no cell tagged '#{cell_tag}' found. " \
              "Tags present in notebook: #{all_tags.empty? ? '(none)' : all_tags.join(', ')}"
      end

      def render_gallery(site, notebook_rel_path, cell_tag, gallery_index, images)
        notebook_basename = File.basename(notebook_rel_path, '.ipynb')
        baseurl = site.config['baseurl'].to_s
        dir = "assets/img/notebook-cells/#{notebook_basename}"
        gallery_id = "nb-cell-#{cell_tag}-#{gallery_index}"

        # Without this, any *other* file's incremental rebuild would sweep these PNGs away
        # the moment this particular post isn't the one being re-rendered that cycle -- see
        # the file-level comment above.
        site.keep_files << dir unless site.keep_files.include?(dir)

        anchors = images.each_with_index.map do |image, i|
          width, height = png_dimensions(image[:bytes])
          # The filename is content-addressed (hash of the PNG's own bytes) rather than just
          # `<tag>-<n>.png`, so the URL itself changes the moment a rerun changes the chart --
          # otherwise browsers happily keep serving a cached copy from the old URL even after
          # the notebook, the plugin, and _site are all already showing the new one.
          digest = Digest::SHA256.hexdigest(image[:bytes])[0, 10]
          filename = "#{cell_tag}-#{gallery_index}-#{i + 1}-#{digest}.png"
          site.static_files << NotebookCellImageFile.new(site, site.source, dir, filename, image[:bytes])
          url = "#{baseurl}/#{dir}/#{filename}"
          alt = CGI.escapeHTML(image[:alt] || "Chart generated from notebook cell tagged '#{cell_tag}'")

          <<~HTML
            <a href="#{url}" data-pswp-width="#{width}" data-pswp-height="#{height}" target="_blank">
              <img src="#{url}" class="img-fluid rounded z-depth-1" alt="#{alt}" />
            </a>
          HTML
        end.join

        <<~HTML
          <div class="pswp-gallery mt-3" id="#{gallery_id}">
            #{anchors}
          </div>
        HTML
      end

      def png_dimensions(bytes)
        [bytes[16, 4].unpack1('N'), bytes[20, 4].unpack1('N')]
      end
    end
  end
end

Liquid::Template.register_tag('jupyter_cell_embed', Jekyll::Tags::JupyterCellEmbedTag)
