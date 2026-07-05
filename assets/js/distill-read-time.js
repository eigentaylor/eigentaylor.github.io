window.addEventListener("load", function () {
  document.querySelectorAll("d-byline[data-read-time]").forEach(function (byline) {
    const readTime = byline.getAttribute("data-read-time");
    const bylineGrid = byline.querySelector(".byline.grid");

    if (!bylineGrid || !readTime || bylineGrid.querySelector(".read-time")) {
      return;
    }

    const readTimeDiv = document.createElement("div");
    readTimeDiv.className = "read-time";

    const heading = document.createElement("h3");
    heading.textContent = "Read Time";
    readTimeDiv.appendChild(heading);

    const value = document.createElement("p");
    value.textContent = readTime;
    readTimeDiv.appendChild(value);

    bylineGrid.appendChild(readTimeDiv);
  });
});
