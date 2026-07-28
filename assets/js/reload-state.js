/**
 * Preserves reading state (open <details> disclosures + scroll position)
 * across a reload, so refreshing to see an update -- or a plain F5 -- doesn't
 * drop the reader back at a collapsed top-of-page. Snapshots on `pagehide`,
 * restores on the next load via sessionStorage, keyed per page path.
 *
 * Loaded only when front matter has `live_update: true` (see
 * `_includes/distill_scripts.liquid`), and must load after proof-disclosure.js
 * so its toggle listeners are already attached before this may set
 * `.open = true` on a <details>.
 */
(function () {
  var STORAGE_PREFIX = "liveUpdateReload:";
  var CORRECTION_WINDOW_MS = 2000;

  function storageKey() {
    return STORAGE_PREFIX + window.location.pathname;
  }

  function classify(el) {
    if (el.classList.contains("proof-disclosure")) return "proof-disclosure";
    if (el.classList.contains("appendix-disclosure")) return "appendix-disclosure";
    if (el.hasAttribute("data-jupyter-notebook-disclosure")) return "jupyter-notebook-disclosure";
    return "details";
  }

  // One pass over every <details> on the page, in document order, assigning
  // each a stable-enough key: its real id when it has one, else an ordinal
  // position within its kind. Used identically for snapshot and restore so
  // the ordinals line up as long as the disclosure structure above a given
  // block hasn't changed between the two.
  function buildKeyIndex() {
    var all = document.querySelectorAll("details");
    var counters = {};
    var out = [];
    for (var i = 0; i < all.length; i++) {
      var el = all[i];
      var key;
      if (el.id) {
        key = "id:" + el.id;
      } else {
        var bucket = classify(el);
        var n = counters[bucket] || 0;
        counters[bucket] = n + 1;
        key = "sel:" + bucket + "#" + n;
      }
      out.push({ el: el, key: key });
    }
    return out;
  }

  function snapshotState() {
    var entries = buildKeyIndex();
    var openKeys = [];
    for (var i = 0; i < entries.length; i++) {
      if (entries[i].el.open) openKeys.push(entries[i].key);
    }
    var snapshot = { v: 1, scrollY: window.scrollY, openKeys: openKeys };
    try {
      sessionStorage.setItem(storageKey(), JSON.stringify(snapshot));
    } catch (e) {
      // sessionStorage unavailable (private browsing quota, etc.) -- nothing to do.
    }
  }

  // Embedded notebook iframes resize their container asynchronously after
  // load (see jupyter_notebook_crawlable.rb's onload handler), which can
  // shift the page's layout/scroll position after we've already restored
  // it. Re-apply once per newly-opened iframe, bounded so a slow notebook
  // can't yank the reader's view after they've started scrolling on their own.
  function attachCorrective(iframe, targetY, deadline) {
    var handled = false;
    iframe.addEventListener("load", function () {
      if (handled) return;
      handled = true;
      if (Date.now() > deadline) return;
      if (Math.abs(window.scrollY - targetY) > 4) return;
      window.scrollTo(0, targetY);
    });
  }

  function applyScroll(targetY, reopenedEls) {
    window.scrollTo(0, targetY);
    if (window.requestAnimationFrame) {
      requestAnimationFrame(function () {
        window.scrollTo(0, targetY);
        requestAnimationFrame(function () {
          window.scrollTo(0, targetY);
        });
      });
    }

    var deadline = Date.now() + CORRECTION_WINDOW_MS;
    for (var i = 0; i < reopenedEls.length; i++) {
      var frames = reopenedEls[i].querySelectorAll("iframe");
      for (var f = 0; f < frames.length; f++) {
        attachCorrective(frames[f], targetY, deadline);
      }
    }
  }

  function restoreState() {
    var raw;
    try {
      raw = sessionStorage.getItem(storageKey());
      // Clear before use: a mid-restore error can't leave a stale
      // snapshot around to misfire on a later, unrelated visit.
      if (raw) sessionStorage.removeItem(storageKey());
    } catch (e) {
      return;
    }
    if (!raw) return;

    var snapshot;
    try {
      snapshot = JSON.parse(raw);
    } catch (e) {
      return;
    }
    if (!snapshot || !snapshot.openKeys) return;

    var openSet = {};
    for (var i = 0; i < snapshot.openKeys.length; i++) {
      openSet[snapshot.openKeys[i]] = true;
    }

    // Only ever ADD .open = true, never close anything -- this unions
    // with whatever proof-disclosure.js's own hash-based auto-open
    // already did, rather than overriding it.
    var entries = buildKeyIndex();
    var reopened = [];
    for (var j = 0; j < entries.length; j++) {
      if (openSet[entries[j].key] && !entries[j].el.open) {
        entries[j].el.open = true;
        reopened.push(entries[j].el);
      }
    }

    applyScroll(snapshot.scrollY, reopened);
  }

  // pagehide (not beforeunload) fires for both a banner-triggered
  // location.reload() and a reader's own manual F5/Ctrl+R, and is
  // bfcache-friendly -- one listener covers both cases.
  window.addEventListener("pagehide", snapshotState);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", restoreState);
  } else {
    restoreState();
  }
})();
