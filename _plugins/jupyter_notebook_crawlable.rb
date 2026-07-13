require 'cgi'

# The jekyll-jupyter-notebook gem renders `{% jupyter_notebook %}` as an <iframe> pointing
# at a separately-built HTML page. Real browsers load that second document automatically,
# but anything that fetches only the post's own HTML (crawlers, LLM/page-fetch tools, curl)
# never follows the iframe and sees no notebook content at all: no code, no text, no plots.
#
# This overrides the same tag name so every existing `{% jupyter_notebook %}` call keeps its
# iframe (unchanged, for real browsers) and additionally gets a plain-HTML rendering of the
# same notebook inlined directly into the page. That inlined copy is visually hidden from
# sighted users (clipped off-screen, not `display:none`) using the standard "sr-only"
# accessibility technique, so it stays in the raw HTML and the accessibility tree without
# adding any visible UI. That's what makes the code/text/plots visible to a plain page fetch.
# Registered from an `:after_init` hook so it wins over the gem's own
# `Liquid::Template.register_tag` call, which runs first (site `_plugins` load before gems).
module Jekyll
  module Tags
    class JupyterNotebookTag < Liquid::Tag
      BODY_CONTENT_PATTERN = /\A.*?<body[^>]*>(.*)<\/body>.*\z/m

      def initialize(tag_name, markup, parse_context)
        super
      end

      def render(context)
        variable = Liquid::Variable.new(@markup, @parse_context)
        notebook_path = variable.render(context)
        if notebook_path.nil?
          Jekyll.logger.warn("Warning:",
                             "Jupyter Notebook path be string literal: " +
                             "<#{@markup.strip.inspect}>")
          notebook_path = @markup.strip # For backward compatibility
        end
        notebook_html_path = "#{notebook_path}.html"

        <<~HTML
          <div
            class="jupyter-notebook"
            style="position: relative; width: 100%; margin: 0 auto;">
            <div class="jupyter-notebook-iframe-container">
              <iframe
                src="#{CGI.escapeHTML(notebook_html_path)}"
                style="position: absolute; top: 0; left: 0; border-style: none;"
                width="100%"
                height="100%"
                onload="this.parentElement.style.paddingBottom = (this.contentWindow.document.documentElement.scrollHeight + 10) + 'px'"></iframe>
            </div>
          </div>
          #{crawlable_text_block(context.registers[:site], notebook_path)}
        HTML
      end

      private

      def crawlable_text_block(site, notebook_path)
        source_path = notebook_source_path(site, notebook_path)
        return "" unless File.file?(source_path)

        body = convert_notebook_body(site, source_path)
        return "" unless body

        # Standard WAI/Bootstrap "sr-only" recipe: clipped to 1x1px and pulled out of flow
        # rather than `display:none`/`visibility:hidden`, so it's dropped from sighted
        # rendering but stays in the raw HTML and the accessibility tree (screen readers,
        # crawlers, page-fetch tools) instead of being removed from both.
        <<~HTML
          <details data-jupyter-notebook-disclosure class="jupyter-notebook-sr-only">
            <summary>View notebook as text (code, output, and plots)</summary>
            <div>#{body}</div>
          </details>
          <style>
            .jupyter-notebook-sr-only {
              position: absolute;
              width: 1px;
              height: 1px;
              padding: 0;
              margin: -1px;
              overflow: hidden;
              clip: rect(0, 0, 0, 0);
              white-space: nowrap;
              border: 0;
            }
          </style>
        HTML
      rescue StandardError => e
        Jekyll.logger.warn("jupyter_notebook:", "skipping text fallback for #{notebook_path}: #{e.message}")
        ""
      end

      def notebook_source_path(site, notebook_path)
        baseurl = site.config["baseurl"].to_s
        path = notebook_path.to_s.strip
        path = path.delete_prefix(baseurl) if !baseurl.empty? && path.start_with?(baseurl)
        path = path.sub(%r{\A/+}, "")
        File.join(site.source, path)
      end

      # Runs nbconvert a second time (independent of the gem's own conversion, which
      # writes the standalone page the iframe points at) so this doesn't depend on
      # Jekyll's page-render ordering. Mirrors the gem's own command shape.
      def convert_notebook_body(site, source_path)
        config = site.config["jupyter_notebook"] || {}
        command = ["jupyter", "nbconvert", "--to", "html", "--stdout"]
        command << "--no-prompt" unless config.fetch("prompt", true)
        command << source_path

        output = IO.popen(command, err: File::NULL, &:read)
        return nil unless $?&.success?

        match = BODY_CONTENT_PATTERN.match(output)
        match && match[1]
      rescue Errno::ENOENT
        nil
      end
    end
  end
end

Jekyll::Hooks.register(:site, :after_init) do
  Liquid::Template.register_tag("jupyter_notebook", Jekyll::Tags::JupyterNotebookTag)
end
