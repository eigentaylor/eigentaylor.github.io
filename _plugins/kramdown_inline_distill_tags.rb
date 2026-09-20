# Teaches kramdown to treat <d-glossary>, <d-cite> and <d-footnote> as inline
# (span-level) HTML, like <em> or <span>.
#
# Kramdown classifies any HTML tag it doesn't know as *block-level*. So a line
# that begins with one of these tags (a paragraph opening with a glossary term
# or citation, `> <d-glossary ...>` inside a blockquote, ...) is parsed as a raw
# HTML block instead of a paragraph: no <p> is emitted, the tags end up as
# direct children of <d-article>'s CSS grid, and every tag/text run lands on its
# own line. The same rule also lets such a line cut a paragraph short when it
# appears mid-paragraph after a soft line wrap.
#
# This overrides only the two block-vs-inline decisions -- not the HTML content
# model -- so the tags' own contents are still passed through untouched, exactly
# as they already were when these tags appeared mid-line.
require 'kramdown'
require 'kramdown/parser/kramdown'

module Jekyll
  module InlineDistillTags
    TAGS = %w[d-glossary d-cite d-footnote].freeze
    # `(?![\w-])` rather than `\b`: `\b` would also match `d-footnote-list`.
    TAG_AT_LINE_START = %r{#{Kramdown::Parser::Kramdown::OPT_SPACE}</?(?:#{TAGS.join('|')})(?![\w-])}

    PARAGRAPH_END_CACHE = {}

    def parse_block_html
      return false if @src.check(TAG_AT_LINE_START)

      super
    end

    # `paragraph_end` is kramdown's own override hook for the paragraph-ending
    # regex; vetoing it when the next line starts with one of our tags keeps the
    # paragraph going. Cached per parser class (GFM defines its own PARAGRAPH_END).
    def paragraph_end
      PARAGRAPH_END_CACHE[self.class] ||=
        /(?!#{TAG_AT_LINE_START})#{super}/
    end
  end
end

Kramdown::Parser::Kramdown.prepend(Jekyll::InlineDistillTags)
