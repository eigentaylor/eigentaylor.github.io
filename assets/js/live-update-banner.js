/**
 * Polls a tiny per-page sidecar file (`live-update.json`, written by
 * `_plugins/live_update_sidecar.rb`) for a content hash and shows an
 * unobtrusive "this page was updated" banner when it changes. Never
 * reloads on its own -- the reader clicks Refresh.
 *
 * Loaded only when front matter has `live_update: true` (see
 * `_includes/distill_scripts.liquid`).
 */
(function () {
  var POLL_INTERVAL_MS = 3 * 60 * 1000; // 3 minutes
  var SIDECAR_FILENAME = "live-update.json";

  var banner = null;
  var refreshBtn = null;
  var sidecarUrl = null;
  var initialHash = null;
  var pollTimer = null;
  var fetchInFlight = false;
  var updateDetected = false;

  function getSidecarUrl() {
    var path = window.location.pathname;
    if (path.charAt(path.length - 1) !== "/") {
      path += "/";
    }
    return path + SIDECAR_FILENAME;
  }

  function fetchHash(callback) {
    if (typeof fetch !== "function") return;
    fetch(sidecarUrl, { cache: "no-store", credentials: "same-origin" })
      .then(function (response) {
        if (!response.ok) throw new Error("live-update sidecar status " + response.status);
        return response.json();
      })
      .then(function (data) {
        callback(null, data && data.hash);
      })
      .catch(function (err) {
        callback(err, null);
      });
  }

  function showBanner() {
    if (banner) banner.style.display = "block";
  }

  function stopPolling() {
    if (pollTimer) {
      clearInterval(pollTimer);
      pollTimer = null;
    }
  }

  function checkForUpdate() {
    if (updateDetected || fetchInFlight || !initialHash) return;
    fetchInFlight = true;
    fetchHash(function (err, hash) {
      fetchInFlight = false;
      if (err || !hash) return;
      if (hash !== initialHash) {
        updateDetected = true;
        showBanner();
        stopPolling();
      }
    });
  }

  function startPolling() {
    if (pollTimer || updateDetected) return;
    pollTimer = setInterval(checkForUpdate, POLL_INTERVAL_MS);
  }

  function handleVisibilityChange() {
    if (updateDetected) return;
    if (document.visibilityState === "visible") {
      // Catch up immediately on refocus rather than waiting for the next tick.
      checkForUpdate();
      startPolling();
    } else {
      stopPolling();
    }
  }

  function init() {
    banner = document.getElementById("live-update-banner");
    if (!banner) return;
    refreshBtn = document.getElementById("live-update-refresh-btn");
    sidecarUrl = getSidecarUrl();

    if (refreshBtn) {
      refreshBtn.addEventListener("click", function () {
        window.location.reload();
      });
    }

    document.addEventListener("visibilitychange", handleVisibilityChange);

    // Baseline fetch doubles as the first check -- same code path as
    // polling, one source of truth for what "hash" means.
    fetchHash(function (err, hash) {
      if (!err && hash) {
        initialHash = hash;
      }
      if (document.visibilityState === "visible") {
        startPolling();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
