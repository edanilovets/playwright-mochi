"""
Login tests suite. Doing login only once and then reuses the context.
"""
import os
import time

import pytest
from playwright.sync_api import Page, expect

from pages.login import LoginPage
from pages.sidebar import Sidebar

MOCHI_USER = os.getenv("MOCHI_USER")
MOCHI_PASSWORD = os.getenv("MOCHI_PASSWORD")


@pytest.fixture(scope="session", autouse=True)
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # login steps
    page = context.new_page()
    page.goto('https://app.mochi.cards')
    page.locator("[placeholder=\"Email\"]").fill(MOCHI_USER)
    page.locator("[placeholder=\"Password\"]").fill(MOCHI_PASSWORD)
    page.locator("button:has-text(\"Log in\")").click()
    account_holder_name = page.locator(".memo_views_side-bar_account_account-holder-name")
    expect(account_holder_name).to_have_text("Eugene", use_inner_text=True, timeout=20000)
    page.wait_for_load_state()

    # Get session storage and store as env variable
    session_storage = page.evaluate("() => JSON.stringify(sessionStorage)")
    os.environ["SESSION_STORAGE"] = session_storage

    yield context


@pytest.fixture(scope="function")
def login(browser):
    context = browser.new_context()
    # Set session storage in a new context
    session_storage = os.environ["SESSION_STORAGE"]
    context.add_init_script("""(storage => {
    if (window.location.hostname === 'app.mochi.cards') {
        const entries = JSON.parse(storage)
        for (const [key, value] of Object.entries(entries)) {
        window.sessionStorage.setItem(key, key)
        }
    }
    })('""" + session_storage + "')")

    page = context.new_page()
    page.goto('https://app.mochi.cards')

    yield page
    # time.sleep(2)
    context.close()


def test_account_holder_name(login):

    page = login
    account_holder_name = page.locator(".memo_views_side-bar_account_account-holder-name")
    # Expect a account holder name "to contain" a substring.
    expect(account_holder_name).to_have_text("Eugene", use_inner_text=True, timeout=20000)


def test_account_holder_name1(login):

    page = login
    account_holder_name = page.locator(".memo_views_side-bar_account_account-holder-name")
    # Expect a account holder name "to contain" a substring.
    expect(account_holder_name).to_have_text("Eugene", use_inner_text=True, timeout=20000)


def test_account_holder_name2(login):

    page = login
    account_holder_name = page.locator(".memo_views_side-bar_account_account-holder-name")
    # Expect a account holder name "to contain" a substring.
    expect(account_holder_name).to_have_text("Eugene", use_inner_text=True, timeout=20000)
