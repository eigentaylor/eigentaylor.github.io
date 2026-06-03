$(window).on("load", function () {
  function enforceNewTabForExternalLinks(root) {
    if (!root) {
      return;
    }

    root.querySelectorAll("a[href]").forEach(function (link) {
      const href = link.getAttribute("href");

      if (!href || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) {
        return;
      }

      try {
        const url = new URL(href, window.location.href);
        if (url.origin !== window.location.origin) {
          link.setAttribute("target", "_blank");

          const relTokens = new Set((link.getAttribute("rel") || "").split(/\s+/).filter(Boolean));
          relTokens.add("noopener");
          relTokens.add("noreferrer");
          link.setAttribute("rel", Array.from(relTokens).join(" "));
        }
      } catch (_error) {
        // Ignore malformed URLs.
      }
    });
  }

  document.querySelectorAll("d-footnote").forEach(function (footnote) {
    footnote.shadowRoot.querySelector("sup > span").setAttribute("style", "color: var(--global-theme-color);");
    footnote.shadowRoot
      .querySelector("d-hover-box")
      .shadowRoot.querySelector("style")
      .sheet.insertRule(".panel {background-color: var(--global-bg-color) !important;}");
    footnote.shadowRoot
      .querySelector("d-hover-box")
      .shadowRoot.querySelector("style")
      .sheet.insertRule(".panel {border-color: var(--global-divider-color) !important;}");
  });
  // Override styles of the citations.
  document.querySelectorAll("d-cite").forEach(function (cite) {
    cite.shadowRoot.querySelector("div > span").setAttribute("style", "color: var(--global-theme-color);");
    cite.shadowRoot.querySelector("style").sheet.insertRule("ul li a {color: var(--global-text-color) !important; text-decoration: none;}");
    cite.shadowRoot.querySelector("style").sheet.insertRule("ul li a:hover {color: var(--global-theme-color) !important;}");
    const hoverBoxRoot = cite.shadowRoot.querySelector("d-hover-box").shadowRoot;
    hoverBoxRoot.querySelector("style")
      .sheet.insertRule(".panel {background-color: var(--global-bg-color) !important;}");
    hoverBoxRoot.querySelector("style")
      .sheet.insertRule(".panel {border-color: var(--global-divider-color) !important;}");

    // d-cite and its hover content are shadow DOM islands, so common.js cannot reach these links.
    enforceNewTabForExternalLinks(cite.shadowRoot);
    enforceNewTabForExternalLinks(hoverBoxRoot);

    const observer = new MutationObserver(function () {
      enforceNewTabForExternalLinks(cite.shadowRoot);
      enforceNewTabForExternalLinks(hoverBoxRoot);
    });

    observer.observe(cite.shadowRoot, { childList: true, subtree: true });
    observer.observe(hoverBoxRoot, { childList: true, subtree: true });
  });
});
