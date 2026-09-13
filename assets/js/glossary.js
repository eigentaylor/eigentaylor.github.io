/*
 * <d-glossary key="..."> -- inline term popovers for distill posts that set
 * `glossary: <topic>` in their front matter (see `_includes/glossary_data.liquid`
 * and `_data/glossary/<topic>.yml`). Deliberately independent of the vendored
 * assets/js/distillpub/* runtime (d-cite/d-footnote), which is gem-owned and not
 * editable here, so this keeps working across al_folio_distill upgrades.
 */
(function () {
  "use strict";

  var DATA_ELEMENT_ID = "d-glossary-data";
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
    "  z-index: 30;",
    "  max-width: 260px;",
    "  padding: 10px 12px;",
    "  font-size: 0.85rem;",
    "  line-height: 1.4;",
    "  background: var(--global-bg-color);",
    "  color: var(--global-text-color);",
    "  border: 1px solid var(--global-divider-color);",
    "  border-radius: 6px;",
    "  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);",
    "  word-wrap: break-word;",
    "  white-space: normal;",
    "}",
    ".popover[hidden] { display: none; }",
    ".popover.align-right { left: auto; right: 0; }",
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

      this.button.addEventListener("mouseenter", () => this.show());
      this.button.addEventListener("focus", () => this.show());
      this.button.addEventListener("mouseleave", () => {
        if (!this.pinned) {
          this.hide();
        }
      });
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
      this.popoverEl.classList.remove("align-right", "align-top");
      var rect = this.popoverEl.getBoundingClientRect();
      if (rect.right > window.innerWidth) {
        this.popoverEl.classList.add("align-right");
      }
      if (rect.bottom > window.innerHeight) {
        this.popoverEl.classList.add("align-top");
      }
      this.button.setAttribute("aria-expanded", "true");
    }

    hide() {
      this.popoverEl.hidden = true;
      this.button.setAttribute("aria-expanded", "false");
    }
  }

  if (!customElements.get("d-glossary")) {
    customElements.define("d-glossary", DGlossary);
  }
})();
