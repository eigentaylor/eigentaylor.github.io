#!/usr/bin/env bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
tmp_site="${tmp_dir}/site"

cleanup() {
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

bundle exec jekyll build --config "_config.yml" -d "${tmp_site}" >/dev/null

glossary_page="${tmp_site}/blog/uncap/index.html"

if [ ! -f "${glossary_page}" ]; then
  echo "uncap post was not generated at ${glossary_page}" >&2
  exit 1
fi

grep -q '<d-glossary' "${glossary_page}"
grep -q '<d-glossary-list' "${glossary_page}"
grep -q 'id="d-glossary-data"' "${glossary_page}"
grep -q 'alabama_paradox' "${glossary_page}"
grep -q 'agreeable_house_size' "${glossary_page}"
grep -q 'huntington_hill_method' "${glossary_page}"
grep -q '/assets/js/glossary.js' "${glossary_page}"

# A distill post that does not set `glossary:` in its front matter must not pay
# for the glossary script or data payload -- proves the {% if page.glossary %}
# guards in distill.liquid/distill_scripts.liquid actually gate loading.
non_glossary_page="${tmp_site}/blog/iia/index.html"

if [ ! -f "${non_glossary_page}" ]; then
  echo "control (non-glossary) distill page was not generated at ${non_glossary_page}" >&2
  exit 1
fi

if grep -q '/assets/js/glossary.js' "${non_glossary_page}"; then
  echo "glossary.js leaked onto a page without page.glossary set: ${non_glossary_page}" >&2
  exit 1
fi

if grep -q 'id="d-glossary-data"' "${non_glossary_page}"; then
  echo "glossary data payload leaked onto a page without page.glossary set: ${non_glossary_page}" >&2
  exit 1
fi

# <d-glossary-list> is unconditional in _layouts/distill.liquid (matching its
# d-footnote-list/d-citation-list siblings), so it should still appear -- inert,
# since glossary.js never loads here -- on a page without page.glossary set.
grep -q '<d-glossary-list' "${non_glossary_page}"

echo "glossary integration checks passed"
