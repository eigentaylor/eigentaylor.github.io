require 'digest/md5'

# Writes a tiny sidecar file (`live-update.json`, `{"hash":"<md5>"}`) next to
# any built page opted into `live_update: true`, so a reader's browser can
# poll a few bytes instead of re-fetching the whole page to notice an edit.
#
# Hashes the raw source file (not the rendered output) so the hash only
# changes when *this* page's own content changes -- not when an unrelated
# site-wide template/footer change touches every page's rendered HTML on
# every deploy, which would otherwise cause false-positive "updated" banners
# across the whole site.
module Jekyll
  module LiveUpdate
    SIDECAR_FILENAME = 'live-update.json'.freeze

    def self.write_sidecar(document)
      return unless document.respond_to?(:data)
      return unless document.data['live_update']
      return unless document.data['layout'].to_s == 'distill'
      return unless File.file?(document.path)

      dest_path = document.destination(document.site.dest)
      dir = File.dirname(dest_path)
      return unless Dir.exist?(dir)

      hash = Digest::MD5.hexdigest(File.read(document.path, mode: 'rb'))
      File.write(File.join(dir, SIDECAR_FILENAME), %({"hash":"#{hash}"}))
    end
  end
end

Jekyll::Hooks.register(:documents, :post_write) do |document|
  Jekyll::LiveUpdate.write_sidecar(document)
end
