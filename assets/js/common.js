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

  // add css to jupyter notebooks
  const cssLink = document.createElement("link");
  cssLink.href = "../css/jupyter.css";
  cssLink.rel = "stylesheet";
  cssLink.type = "text/css";

  let jupyterTheme = determineComputedTheme();

  $(".jupyter-notebook-iframe-container iframe").each(function () {
    $(this).contents().find("head").append(cssLink);

    if (jupyterTheme == "dark") {
      $(this).bind("load", function () {
        $(this).contents().find("body").attr({
          "data-jp-theme-light": "false",
          "data-jp-theme-name": "JupyterLab Dark",
        });
      });
    }
  });

  // trigger popovers
  $('[data-toggle="popover"]').popover({
    trigger: "hover",
  });
});
