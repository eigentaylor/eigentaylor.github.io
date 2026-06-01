require "liquid"
require_relative "_plugins/appendix_word_count"
raw = File.read("_previews/2026-06-01-av-stratproof.md")
obj = Object.new
obj.extend(Jekyll::AppendixWordCount)
puts "words_without_appendix_raw=#{obj.words_without_appendix(raw)}"
collapsed = obj.collapse_appendix(raw)
puts "has_disclosure_raw=#{collapsed.include?("appendix-disclosure")}" 
