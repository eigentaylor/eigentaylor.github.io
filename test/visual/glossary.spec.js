const { test, expect } = require("@playwright/test");
const { preparePage, stabilizeVisuals } = require("./helpers");

const ROUTE = "/al-folio/blog/uncap/";

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
    const link = term.locator(".popover a");

    await term.locator("button").click();
    await expect(link).toHaveAttribute("target", "_blank");
    await expect(link).toHaveAttribute("rel", /noopener/);
  });
});
