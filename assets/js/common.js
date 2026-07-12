$(document).ready(function () {
  // On preview pages, map ../post-slug links to the published /blog/post-slug/ route.
  const baseurl = document.body.dataset.baseurl || "";
  const previewRoot = `${baseurl}/preview/`;
  const isPreviewPage = document.body.classList.contains("is-preview") || window.location.pathname.startsWith(previewRoot);

  if (isPreviewPage) {

    document.querySelectorAll("a[href]").forEach((link) => {
      const rawHref = link.getAttribute("href");

      if (!rawHref || !rawHref.startsWith("../")) {
        return;
      }

      // Only rewrite simple one-segment relative slugs like ../ditch-rcv.
      const slugMatch = rawHref.match(/^\.\.\/([^\/?#]+)\/?([?#].*)?$/);
      if (!slugMatch) {
        return;
      }

      const slug = slugMatch[1];
      const suffix = slugMatch[2] || "";
      link.setAttribute("href", `${baseurl}/blog/${slug}/${suffix}`);
    });
  }

  // Enforce new-tab behavior for external links site-wide.
  document.querySelectorAll("a[href]").forEach((link) => {
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

  // add toggle functionality to abstract, award and bibtex buttons
  $("a.abstract").click(function () {
    $(this).parent().parent().find(".abstract.hidden").toggleClass("open");
    $(this).parent().parent().find(".award.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.award").click(function () {
    $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".award.hidden").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.bibtex").click(function () {
    $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".award.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden").toggleClass("open");
  });
  $("a").removeClass("waves-effect waves-light");

  // bootstrap-toc
  if ($("#toc-sidebar").length) {
    // remove related publications years from the TOC
    $(".publications h2").each(function () {
      $(this).attr("data-toc-skip", "");
    });
    var navSelector = "#toc-sidebar";
    var $myNav = $(navSelector);
    Toc.init($myNav);
    $("body").scrollspy({
      target: navSelector,
      offset: 100,
    });
  }

  // add css to jupyter notebooks and match the site's light/dark theme
  let jupyterTheme = determineComputedTheme();

  const applyJupyterIframeTheme = (iframe) => {
    const $iframe = $(iframe);
    const cssLink = document.createElement("link");
    cssLink.href = "../css/jupyter.css";
    cssLink.rel = "stylesheet";
    cssLink.type = "text/css";
    $iframe.contents().find("head").append(cssLink);

    // The notebook export also bakes in a plain `pre { background-color: #282828;
    // color: #f8f8f0 }` rule from the classic nbconvert template. It's not scoped to
    // any jp-theme class, so it always wins over the reactive .highlight background
    // beneath it — coincidentally fine-looking in dark mode, but unreadable dark-on-
    // dark in light mode. Force it to follow the same reactive variables instead.
    const themeOverride = document.createElement("style");
    themeOverride.textContent = `
      pre, code {
        background: var(--jp-cell-editor-background) !important;
        background-color: var(--jp-cell-editor-background) !important;
        color: var(--jp-mirror-editor-variable-color) !important;
      }
    `;
    $iframe.contents().find("head").append(themeOverride);

    $iframe.contents().find("body").attr({
      "data-jp-theme-light": jupyterTheme == "dark" ? "false" : "true",
      "data-jp-theme-name": jupyterTheme == "dark" ? "JupyterLab Dark" : "JupyterLab Light",
    });

    // jupyter.css's dark theme reads --global-bg-color for its background, but that
    // variable is only defined on the parent site's page, not inside the notebook's
    // own (separate) document, so it resolves to nothing there. Mirror it in so the
    // notebook's background actually matches instead of staying transparent.
    const iframeDoc = iframe.contentDocument;
    const globalBgColor = getComputedStyle(document.documentElement).getPropertyValue("--global-bg-color");
    if (iframeDoc && iframeDoc.documentElement && globalBgColor) {
      iframeDoc.documentElement.style.setProperty("--global-bg-color", globalBgColor.trim());
    }
  };

  $(".jupyter-notebook-iframe-container iframe").each(function () {
    // The iframe may have already finished loading by the time this script runs
    // (deferred scripts execute after DOMContentLoaded), in which case a "load"
    // listener registered now would never fire. Apply immediately when possible,
    // and still listen for "load" as a fallback for slower iframes.
    if (this.contentDocument && this.contentDocument.readyState === "complete") {
      applyJupyterIframeTheme(this);
    } else {
      $(this).on("load", () => applyJupyterIframeTheme(this));
    }
  });

  // trigger popovers
  $('[data-toggle="popover"]').popover({
    trigger: "hover",
  });
});
