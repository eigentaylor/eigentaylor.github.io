require 'cgi'

module Jekyll
  module AppendixWordCount
    APPENDIX_HEADING_REGEX = /<h2\b[^>]*>(.*?)<\/h2>/im
    APPENDIX_MARKDOWN_HEADING_REGEX = /^##\s+Appendix\b.*$/i
    APPENDIX_PREFIX_REGEX = /\AAppendix\b/i

    def content_without_appendix(input)
      content = input.to_s

      html_match = first_appendix_heading_match(content)
      return content[0...html_match.begin(0)] if html_match

      markdown_match = first_markdown_appendix_heading_match(content)
      return content[0...markdown_match.begin(0)] if markdown_match

      content
    end

    def content_without_footnotes(input)
      input.to_s.gsub(/<d-footnote\b[^>]*>.*?<\/d-footnote>/im, '')
    end

    def content_without_proof_blocks(input)
      input.to_s.gsub(/<details\b[^>]*data-proof-disclosure[^>]*>.*?<\/details>/im, '')
    end

    def words_without_appendix(input)
      main_content = content_without_appendix(input)
      count_words_in_html(main_content)
    end

    def collapse_appendix(input)
      content = input.to_s

      html_match = first_appendix_heading_match(content)
      return collapse_html_appendix(content, html_match) if html_match

      markdown_match = first_markdown_appendix_heading_match(content)
      return collapse_markdown_appendix(content, markdown_match) if markdown_match

      content
    end

    private

    def collapse_html_appendix(content, match)
      heading_html = match[0]
      heading_text = strip_tags(match[1]).strip
      summary_text = heading_text.empty? ? 'Appendix' : heading_text

      before_appendix = content[0...match.begin(0)]
      appendix_body = content[match.begin(0)..].sub(heading_html, '')

      <<~HTML.chomp
        #{before_appendix}<details class="appendix-disclosure">
          <summary>#{CGI.escapeHTML(summary_text)}</summary>
          #{appendix_body}
        </details>
      HTML
    end

    def collapse_markdown_appendix(content, match)
      heading_text = match[0].sub(/^##\s+/, '').strip
      summary_text = heading_text.empty? ? 'Appendix' : heading_text

      before_appendix = content[0...match.begin(0)]
      appendix_body = content[match.end(0)..] || ''

      <<~MARKDOWN.chomp
        #{before_appendix}<details class="appendix-disclosure">
          <summary>#{CGI.escapeHTML(summary_text)}</summary>

          #{appendix_body.lstrip}
        </details>
      MARKDOWN
    end

    def first_markdown_appendix_heading_match(content)
      content.match(APPENDIX_MARKDOWN_HEADING_REGEX)
    end

    def first_appendix_heading_match(content)
      content.scan(APPENDIX_HEADING_REGEX) do
        match = Regexp.last_match
        heading_text = strip_tags(match[1]).gsub(/\s+/, ' ').strip
        return match if heading_text.match?(APPENDIX_PREFIX_REGEX)
      end
      nil
    end

    def count_words_in_html(html)
      plain_text = strip_tags(html)
      plain_text.scan(/[[:alnum:]][[:alnum:]_'-]*/).size
    end

    def strip_tags(html)
      text = html.to_s
      text = text.gsub(/<script.*?<\/script>/im, ' ')
      text = text.gsub(/<style.*?<\/style>/im, ' ')
      text = text.gsub(/<[^>]+>/, ' ')
      CGI.unescapeHTML(text)
    end
  end
end

Liquid::Template.register_filter(Jekyll::AppendixWordCount)