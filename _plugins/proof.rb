module Jekyll
  module Tags
    class ProofTag < Liquid::Block
      def initialize(tag_name, markup, tokens)
        super
        @caption = markup.to_s.strip
      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)

        caption_src = @caption.empty? ? "Click to expand proof" : @caption
        caption = converter.convert(caption_src).gsub(/<\/?p[^>]*>/, '').chomp
        body = converter.convert(super(context))

        "<details class=\"proof-disclosure\" data-proof-disclosure><summary>#{caption}</summary><div class=\"proof-disclosure-rail\" data-proof-disclosure-rail aria-hidden=\"true\" title=\"Collapse\"></div><div class=\"proof-content\">#{body}</div></details>"
      end
    end
  end
end

Liquid::Template.register_tag('proof', Jekyll::Tags::ProofTag)
