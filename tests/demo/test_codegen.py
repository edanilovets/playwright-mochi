from playwright.sync_api import Playwright


def test_codegen(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://playwright.dev/
    page.goto("https://playwright.dev/")

    # Click a[role="button"]:has-text("Node.js")
    page.locator("a[role=\"button\"]:has-text(\"Node.js\")").click()

    # Click nav >> text=Python
    page.locator("nav >> text=Python").click()
    page.wait_for_url("https://playwright.dev/python/")

    # Click text=Get started
    page.locator("text=Get started").click()
    page.wait_for_url("https://playwright.dev/python/docs/intro")

    # Click [aria-label="Switch between dark and
    # light mode \(currently light mode\)"]
    page.locator(
        "[aria-label=\"Switch between dark and light mode \\(currently light mode\\)\"]").click()

    # ---------------------
    context.close()
    browser.close()
