window.MathJax = {
  tex: {
    tags: "ams",
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
  },
  options: {
    renderActions: {
      addCss: [
        200,
        function (doc) {
          const style = document.createElement("style");
          style.innerHTML = `
          .mjx-container {
            color: inherit;
          }

          mjx-container[jax="CHTML"][display="true"] {
            display: block;
            width: 100%;
            max-width: 100%;
            overflow-x: auto !important;
            overflow-y: hidden !important;
            -webkit-overflow-scrolling: touch;
            touch-action: pan-x pan-y;
          }

          mjx-container[jax="CHTML"][display="true"] > mjx-math {
            min-width: max-content;
          }

          .MathJax_Display {
            overflow-x: auto !important;
            overflow-y: hidden !important;
            -webkit-overflow-scrolling: touch;
          }
        `;
          document.head.appendChild(style);
        },
        "",
      ],
    },
  },
};
