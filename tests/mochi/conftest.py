import os
from typing import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright, expect
import base64


MOCHI_USERNAME = os.getenv("MOCHI_USERNAME")
MOCHI_EMAIL = os.getenv("MOCHI_EMAIL")
MOCHI_PASSWORD = os.getenv("MOCHI_PASSWORD")
MOCHI_API_KEY = os.getenv("MOCHI_API_KEY")
MOCHI_API_KEY_BASE64 = base64.b64encode(bytes(f"{MOCHI_API_KEY}:{MOCHI_PASSWORD}", "UTF-8")).decode("UTF-8")


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # login steps
    page = context.new_page()
    page.goto('https://app.mochi.cards')
    page.locator("[placeholder=\"Email\"]").fill(MOCHI_EMAIL)
    page.locator("[placeholder=\"Password\"]").fill(MOCHI_PASSWORD)
    page.locator("button:has-text(\"Log in\")").click()
    account_holder_name = page.locator(".memo_views_side-bar_account_account-holder-name")
    expect(account_holder_name).to_have_text(MOCHI_USERNAME, use_inner_text=True, timeout=20000)

    yield context


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    headers = {
        # "Accept": "application/json",
        # "Authorization": f"Bearer {TOKEN}"
        "Authorization": f"Basic {MOCHI_API_KEY_BASE64}"
    }
    request_context = playwright.request.new_context(
        base_url="https://app.mochi.cards", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="function")
def main_page(context_creation):
    page = context_creation.new_page()
    page.goto('https://app.mochi.cards')

    yield page
    page.close()
