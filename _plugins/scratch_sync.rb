require 'open3'
require 'timeout'

# Keeps the gitignored _scratch/ drafts folder synced with pCloud while the dev server runs, by calling
# bin/sync_scratch.py (which holds all the logic; see its docstring):
#
# - when the site is created (once per `jekyll serve`/`build` process): a full `sync`, before anything is
#   read, so the first build already has the other machine's edits. Waits for it, up to STARTUP_TIMEOUT.
# - after every write (each rebuild, i.e. each time a draft is saved): `push --quiet` in the background, so
#   a slow pCloud drive never holds up a rebuild. Prints only when it sent something or hit a problem.
#
# Off in production builds (JEKYLL_ENV=production, which every deploy/CI workflow sets), in CI, and when
# SCRATCH_SYNC=0.
module Jekyll
  module ScratchSync
    SCRIPT = File.join('bin', 'sync_scratch.py').freeze
    STARTUP_TIMEOUT = 60

    class << self
      def enabled?(site)
        return false if ENV['JEKYLL_ENV'] == 'production' || ENV['CI'] || ENV['SCRATCH_SYNC'] == '0'

        File.file?(File.join(site.source, SCRIPT))
      end

      def python(site)
        [File.join('.venv', 'Scripts', 'python.exe'), File.join('.venv', 'bin', 'python')]
          .map { |p| File.join(site.source, p) }
          .find { |p| File.file?(p) } || 'python'
      end

      def command(site, *args)
        [python(site), '-u', File.join(site.source, SCRIPT), *args]
      end

      def startup_sync(site)
        return if @started

        @started = true
        Jekyll.logger.info 'Scratch sync:', 'syncing _scratch/ with pCloud...'
        Open3.popen2e(*command(site, 'sync'), chdir: site.source) do |stdin, output, thread|
          stdin.close
          begin
            Timeout.timeout(STARTUP_TIMEOUT) { output.each_line { |line| puts "  #{line.chomp}" } }
          rescue Timeout::Error
            Process.kill('KILL', thread.pid) rescue nil
            Jekyll.logger.warn 'Scratch sync:', "gave up after #{STARTUP_TIMEOUT}s (is pCloud stuck?); " \
                                                'serving without it'
          end
          thread.value
        end
      rescue SystemCallError => e
        Jekyll.logger.warn 'Scratch sync:', "couldn't run #{SCRIPT}: #{e.message}"
      end

      def background_push(site)
        pid = Process.spawn(*command(site, 'push', '--quiet'), chdir: site.source, in: File::NULL)
        Process.detach(pid)
      rescue SystemCallError => e
        Jekyll.logger.warn 'Scratch sync:', "couldn't run #{SCRIPT}: #{e.message}"
      end
    end
  end
end

Jekyll::Hooks.register(:site, :after_init) do |site|
  Jekyll::ScratchSync.startup_sync(site) if Jekyll::ScratchSync.enabled?(site)
end

Jekyll::Hooks.register(:site, :post_write) do |site|
  Jekyll::ScratchSync.background_push(site) if Jekyll::ScratchSync.enabled?(site)
end
