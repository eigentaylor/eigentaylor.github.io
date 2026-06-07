module.exports = {
  content: ["_site/**/*.html", "_site/**/*.js"],
  css: ["_site/assets/css/*.css"],
  output: "_site/assets/css/",
  skippedContentGlobs: ["_site/assets/**/*.html"],
  safelist: {
    standard: [
      "collapse",
      "collapsing",
      "show",
      "dropdown-menu",
      "dropdown-item",
      "table",
      "table-dark",
      "table-hover",
      "table-responsive",
      "af-tooltip",
      "af-popover",
      "font-weight-bold",
      "font-weight-medium",
      "font-weight-lighter",
      // Custom navbar classes from header.liquid override
      "navbar-collapse-main",
      "navbar-menu-list",
      "navbar-toggler-main",
      // Draft preview body class (only on preview pages, may not appear in built _site)
      "is-preview",
    ],
    patterns: [
      /^navbar/, // keep all navbar-* classes (Bootstrap + custom al-folio)
    ],
  },
};
