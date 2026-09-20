/*
 * <d-glossary key="..."> -- inline term popovers for distill posts that set
 * `glossary: <topic>` in their front matter (see `_plugins/glossary_data_tag.rb`
 * and `_data/glossary/<topic>.yml`). Deliberately independent of the vendored
 * assets/js/distillpub/* runtime (d-cite/d-footnote), which is gem-owned and not
 * editable here, so this keeps working across al_folio_distill upgrades.
 */
(function () {
  "use strict";

  var DATA_ELEMENT_ID = "d-glossary-data";
  var ANCHOR_PREFIX = "d-glossary-";
  // Same reading width as the distill footnote hover box (d-hover-box).
  var POPOVER_WIDTH = 704;
  var VIEWPORT_MARGIN = 8;
  var glossaryMap = null;
  var seenKeys = new Set();
  var openInstances = new Set();
  var warnedMissingKeys = new Set();
  var popoverIdCounter = 0;

  function getGlossaryMap() {
    if (glossaryMap) {
      return glossaryMap;
    }
    glossaryMap = new Map();
    var dataScript = document.getElementById(DATA_ELEMENT_ID);
    if (!dataScript) {
      return glossaryMap;
    }
    var entries;
    try {
      entries = JSON.parse(dataScript.textContent);
    } catch (error) {
      console.warn("[d-glossary] could not parse glossary data:", error);
      return glossaryMap;
    }
    if (Array.isArray(entries)) {
      entries.forEach(function (entry) {
        if (entry && entry.key) {
          glossaryMap.set(entry.key, entry);
        }
      });
    }
    return glossaryMap;
  }

  function closeInstance(instance) {
    instance.pinned = false;
    instance.hide();
    openInstances.delete(instance);
  }

  // Shared listeners (one each, not per-instance) back Escape-to-close and
  // click-outside-to-close for every pinned popover on the page.
  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape" || openInstances.size === 0) {
      return;
    }
    openInstances.forEach(function (instance) {
      instance.button.focus();
      closeInstance(instance);
    });
  });

  document.addEventListener("click", function (event) {
    if (openInstances.size === 0) {
      return;
    }
    var path = event.composedPath();
    openInstances.forEach(function (instance) {
      if (path.indexOf(instance) === -1) {
        closeInstance(instance);
      }
    });
  });

  var STYLE = [
    ":host { display: inline; }",
    ".wrap { position: relative; display: inline-block; }",
    "button.term {",
    "  all: unset;",
    "  cursor: help;",
    "  color: inherit;",
    "  font: inherit;",
    "  border-bottom: 1px dashed var(--global-theme-color);",
    "}",
    "button.term:hover, button.term:focus-visible {",
    "  border-bottom-style: solid;",
    "}",
    "button.term.muted {",
    "  color: var(--global-text-color-light);",
    "  border-bottom-color: var(--global-text-color-light);",
    "}",
    "button.term.muted:hover, button.term.muted:focus-visible {",
    "  color: var(--global-text-color);",
    "  border-bottom-color: var(--global-text-color);",
    "}",
    ".popover {",
    "  position: absolute;",
    "  top: 100%;",
    "  left: 0;",
    "  margin-top: 4px;",
    "  z-index: 10000;",
    "  box-sizing: border-box;",
    "  width: 704px;",
    "  max-width: 100vw;",
    "  padding: 12px 16px;",
    "  font-size: 1rem;",
    "  line-height: 1.5;",
    "  background: var(--global-bg-color);",
    "  color: var(--global-text-color);",
    "  border: 1px solid var(--global-divider-color);",
    "  border-radius: 4px;",
    "  box-shadow: 0 0 7px rgba(0, 0, 0, 0.1);",
    "  backdrop-filter: blur(2px);",
    "  word-wrap: break-word;",
    "  white-space: normal;",
    "}",
    ".popover[hidden] { display: none; }",
    ":host(:target) button.term { animation: target-flash 2s ease-out; }",
    "@keyframes target-flash {",
    "  0%, 40% { background: color-mix(in srgb, var(--global-theme-color) 35%, transparent); }",
    "  100% { background: transparent; }",
    "}",
    ".popover.align-top { top: auto; bottom: 100%; margin-top: 0; margin-bottom: 4px; }",
    ".popover p { margin: 0; }",
    ".popover a {",
    "  color: var(--global-theme-color);",
    "  display: inline-block;",
    "  margin-top: 6px;",
    "}",
  ].join("\n");

  class DGlossary extends HTMLElement {
    connectedCallback() {
      // Guards against a spurious rebuild if the element is ever moved in the
      // DOM (which re-fires connectedCallback) -- shadow DOM is built once.
      if (this.shadowRoot) {
        return;
      }

      var key = this.getAttribute("key");
      var entry = key ? getGlossaryMap().get(key) : null;

      if (!entry) {
        if (key && !warnedMissingKeys.has(key)) {
          warnedMissingKeys.add(key);
          console.warn('[d-glossary] unknown key "' + key + '" -- rendering as plain text.');
        }
        return;
      }

      // First occurrence of a key on the page gets the "active" (theme-color)
      // treatment; every later occurrence is visually muted, per Wikipedia's
      // link-once convention -- but stays just as interactive.
      var variant = seenKeys.has(key) ? "muted" : "active";
      seenKeys.add(key);

      // Anchor for deep links (#d-glossary-<key>), first occurrence only so
      // ids stay unique; the appendix list links back here.
      if (variant === "active" && !this.id) {
        this.id = ANCHOR_PREFIX + key;
      }

      this.pinned = false;

      var shadow = this.attachShadow({ mode: "open" });
      var popoverId = "d-glossary-popover-" + ++popoverIdCounter;

      shadow.innerHTML =
        "<style>" +
        STYLE +
        "</style>" +
        '<span class="wrap">' +
        '<button type="button" class="term' +
        (variant === "muted" ? " muted" : "") +
        '" aria-haspopup="true" aria-expanded="false" aria-describedby="' +
        popoverId +
        '"><slot></slot></button>' +
        '<div class="popover" role="tooltip" id="' +
        popoverId +
        '" hidden></div>' +
        "</span>";

      this.button = shadow.querySelector("button.term");
      // NOTE: must NOT be named `this.popover` -- HTMLElement has a native,
      // reflected `popover` IDL property (the browser's own Popover API).
      // Assigning a Node to it stringifies to "[object HTMLDivElement]" and
      // writes that as the real `popover` content attribute, which makes the
      // browser treat the whole custom element as a native popover: yanked
      // into the top layer, given default browser chrome, and detached from
      // its actual position in the article.
      this.popoverEl = shadow.querySelector(".popover");

      var definitionText = document.createElement("p");
      definitionText.textContent = entry.definition || "";
      this.popoverEl.appendChild(definitionText);

      if (entry.link) {
        var link = document.createElement("a");
        link.href = entry.link;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.textContent = "Learn more";
        // The popover lives in shadow DOM, so common.js's site-wide external-link
        // handling can't reach it -- set target/rel here directly instead.
        this.popoverEl.appendChild(link);
      }

      // Like the footnote hover box, hiding is delayed so the mouse can travel
      // from the term into the popover (e.g. to click "Learn more").
      var enter = () => {
        this.cancelHide();
        this.show();
      };
      this.button.addEventListener("mouseenter", enter);
      this.popoverEl.addEventListener("mouseenter", enter);
      this.button.addEventListener("focus", enter);
      this.button.addEventListener("mouseleave", () => this.scheduleHide(300));
      this.popoverEl.addEventListener("mouseleave", () => this.scheduleHide(500));
      this.button.addEventListener("blur", () => {
        if (!this.pinned) {
          this.hide();
        }
      });
      this.button.addEventListener("click", (event) => {
        // Without this, the shared document click-outside listener (added
        // above) would immediately close the popover this same click just pinned.
        event.stopPropagation();
        if (this.pinned) {
          closeInstance(this);
        } else {
          this.pinned = true;
          openInstances.add(this);
          this.show();
        }
      });
    }

    show() {
      this.popoverEl.hidden = false;
      this.popoverEl.classList.remove("align-top");
      // Center the box in the viewport like the footnote hover box, rather than
      // hugging the (often short) term it belongs to. `.wrap` is the containing
      // block, so offset by its left edge.
      var viewportWidth = document.documentElement.clientWidth;
      var width = Math.min(POPOVER_WIDTH, viewportWidth - 2 * VIEWPORT_MARGIN);
      var wrapLeft = this.popoverEl.parentElement.getBoundingClientRect().left;
      this.popoverEl.style.width = width + "px";
      this.popoverEl.style.left = (viewportWidth - width) / 2 - wrapLeft + "px";
      var rect = this.popoverEl.getBoundingClientRect();
      if (rect.bottom > window.innerHeight) {
        this.popoverEl.classList.add("align-top");
      }
      this.button.setAttribute("aria-expanded", "true");
    }

    hide() {
      this.cancelHide();
      this.popoverEl.hidden = true;
      this.button.setAttribute("aria-expanded", "false");
    }

    scheduleHide(delay) {
      this.cancelHide();
      if (this.pinned) {
        return;
      }
      this.hideTimer = setTimeout(() => this.hide(), delay);
    }

    cancelHide() {
      clearTimeout(this.hideTimer);
    }
  }

  if (!customElements.get("d-glossary")) {
    customElements.define("d-glossary", DGlossary);
  }

  // <d-glossary-list> -- summarizes every glossary term actually used on the
  // page, alphabetically, inside <d-appendix> alongside <d-footnote-list> and
  // <d-citation-list>. Rendered in light DOM (no shadow root) on purpose, so
  // it inherits this repo's own `d-appendix h3, li, span, a` styling for free
  // (see _sass/_distill.scss) exactly like its two gem-provided siblings do.
  //
  // Registration order matters: customElements.define() synchronously
  // upgrades every already-parsed matching element (running connectedCallback)
  // before returning, so defining d-glossary first guarantees `seenKeys` is
  // fully populated by the time this element reads it, regardless of where
  // <d-glossary-list> sits in the document.
  class DGlossaryList extends HTMLElement {
    connectedCallback() {
      if (this.childNodes.length > 0) {
        return;
      }

      if (seenKeys.size === 0) {
        this.style.display = "none";
        return;
      }

      var map = getGlossaryMap();
      var entries = Array.from(seenKeys)
        .map(function (key) {
          return map.get(key);
        })
        .filter(Boolean);
      entries.sort(function (a, b) {
        return a.term.localeCompare(b.term);
      });

      var heading = document.createElement("h3");
      heading.textContent = "Glossary";
      this.appendChild(heading);

      var list = document.createElement("ol");
      entries.forEach(function (entry) {
        var item = document.createElement("li");
        var strong = document.createElement("strong");
        strong.textContent = entry.term;
        item.appendChild(strong);
        item.appendChild(document.createTextNode(": " + entry.definition));
        if (entry.link) {
          item.appendChild(document.createTextNode(" "));
          var link = document.createElement("a");
          link.href = entry.link;
          link.target = "_blank";
          link.rel = "noopener noreferrer";
          link.textContent = "Learn more";
          item.appendChild(link);
        }
        var back = document.createElement("a");
        back.href = "#" + ANCHOR_PREFIX + entry.key;
        back.title = "Jump to first use";
        back.textContent = "↩";
        item.appendChild(document.createTextNode(" "));
        item.appendChild(back);
        list.appendChild(item);
      });
      this.appendChild(list);
    }
  }

  if (!customElements.get("d-glossary-list")) {
    customElements.define("d-glossary-list", DGlossaryList);
  }

  // Native fragment scrolling can fire before these elements exist/upgrade and
  // layout shifts after load, so re-scroll to #d-glossary-<key> explicitly.
  function scrollToGlossaryHash() {
    var hash = window.location.hash;
    if (hash.indexOf("#" + ANCHOR_PREFIX) !== 0) {
      return;
    }
    var target = document.getElementById(decodeURIComponent(hash.slice(1)));
    if (target) {
      target.scrollIntoView({ block: "center" });
    }
  }
  window.addEventListener("load", scrollToGlossaryHash);
  window.addEventListener("hashchange", scrollToGlossaryHash);
})();
