const { test, expect } = require("@playwright/test");
const { preparePage, stabilizeVisuals } = require("./helpers");

const ROUTE = "/al-folio/blog/uncap/";

// Playwright's default actionability scroll ("nearest edge") can land a target
// right under this theme's fixed header/footer chrome, since terms sit deep in
// the article body. Centering the target in the viewport first avoids that.
async function centerOn(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: "center", inline: "center" }));
}

for (const theme of ["light", "dark"]) {
  test(`glossary repeat occurrences render muted vs active (${theme})`, async ({ page }) => {
    await preparePage(page, theme);
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const terms = page.locator('d-glossary[key="alabama_paradox"]');
    await expect(terms).toHaveCount(2);

    const [firstColor, secondColor] = await Promise.all([
      terms
        .nth(0)
        .locator("button")
        .evaluate((el) => getComputedStyle(el).borderBottomColor),
      terms
        .nth(1)
        .locator("button")
        .evaluate((el) => getComputedStyle(el).borderBottomColor),
    ]);

    // First occurrence is styled with --global-theme-color, later occurrences
    // with the muted --global-text-color-light -- they must not match.
    expect(firstColor).not.toBe(secondColor);
  });
}

test.describe("glossary popover interactions", () => {
  test("hover reveals and mouseleave hides an unpinned popover", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const term = page.locator('d-glossary[key="alabama_paradox"]').first();
    const button = term.locator("button");
    const popover = term.locator(".popover");

    await expect(popover).toBeHidden();
    await centerOn(button);
    await button.hover();
    await expect(popover).toBeVisible();
    await expect(popover).toContainText("apportionment");

    await page.mouse.move(0, 0);
    await expect(popover).toBeHidden();
  });

  test("focus reveals and blur hides an unpinned popover", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const term = page.locator('d-glossary[key="agreeable_house_size"]').first();
    const button = term.locator("button");
    const popover = term.locator(".popover");

    await centerOn(button);
    await button.focus();
    await expect(popover).toBeVisible();
    await button.evaluate((el) => el.blur());
    await expect(popover).toBeHidden();
  });

  test("click pins the popover open through a mouseleave, second click closes it", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const term = page.locator('d-glossary[key="alabama_paradox"]').first();
    const button = term.locator("button");
    const popover = term.locator(".popover");

    await centerOn(button);
    await button.click();
    await expect(popover).toBeVisible();

    await page.mouse.move(0, 0);
    await expect(popover).toBeVisible();

    await button.click();
    await expect(popover).toBeHidden();
  });

  test("Escape closes a pinned popover", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const term = page.locator('d-glossary[key="alabama_paradox"]').first();
    const button = term.locator("button");
    const popover = term.locator(".popover");

    await centerOn(button);
    await button.click();
    await expect(popover).toBeVisible();

    await page.keyboard.press("Escape");
    await expect(popover).toBeHidden();
  });

  test("clicking elsewhere on the page closes a pinned popover", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const term = page.locator('d-glossary[key="alabama_paradox"]').first();
    const button = term.locator("button");
    const popover = term.locator(".popover");

    await centerOn(button);
    await button.click();
    await expect(popover).toBeVisible();

    await page.locator("body").click({ position: { x: 5, y: 5 } });
    await expect(popover).toBeHidden();
  });

  test("learn more link opens in a new tab", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const term = page.locator('d-glossary[key="alabama_paradox"]').first();
    const button = term.locator("button");
    const link = term.locator(".popover a");

    await centerOn(button);
    await button.click();
    await expect(link).toHaveAttribute("target", "_blank");
    await expect(link).toHaveAttribute("rel", /noopener/);
  });
});

test.describe("glossary appendix summary", () => {
  test("d-glossary-list renders every used term, alphabetically", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE, { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    const list = page.locator("d-appendix d-glossary-list");
    await list.scrollIntoViewIfNeeded();

    await expect(list.locator("h3")).toHaveText("Glossary");
    const items = list.locator("ol > li");
    await expect(items).toHaveCount(12);

    // Alphabetical by term: "Adams's Method" sorts first, "Webster's Method" last.
    await expect(items.first().locator("strong")).toHaveText("Adams's Method");
    await expect(items.last().locator("strong")).toHaveText("Webster's Method");

    // Each entry with a link opens in a new tab, matching the inline popovers.
    const linkedItem = list.locator("li", { hasText: "Alabama Paradox" });
    await expect(linkedItem.locator("a").first()).toHaveAttribute("target", "_blank");
  });

  test("first occurrence has a #d-glossary-<key> anchor and the appendix links back to it", async ({ page }) => {
    await preparePage(page, "light");
    await page.goto(ROUTE + "#d-glossary-alabama_paradox", { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    // Only the first of the two occurrences carries the id.
    const terms = page.locator('d-glossary[key="alabama_paradox"]');
    await expect(terms.nth(0)).toHaveAttribute("id", "d-glossary-alabama_paradox");
    await expect(terms.nth(1)).not.toHaveAttribute("id", /.+/);
    await expect(terms.nth(0)).toBeInViewport();

    const back = page.locator("d-glossary-list li", { hasText: "Alabama Paradox" }).locator('a[href="#d-glossary-alabama_paradox"]');
    await expect(back).toHaveCount(1);
  });

  test("d-glossary-list stays hidden on a page with no glossary terms used", async ({ page }) => {
    await preparePage(page, "light");
    // A distill page without `page.glossary` set never loads glossary.js at
    // all, so <d-glossary-list> stays an inert, invisible, undefined element.
    await page.goto("/al-folio/blog/iia/", { waitUntil: "networkidle" });
    await stabilizeVisuals(page);

    await expect(page.locator("d-appendix d-glossary-list")).toBeHidden();
  });
});
