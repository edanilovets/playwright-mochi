"""
Login tests suite. Doing login only once and then reuses the context.
"""
import os
import time

import pytest
from playwright.sync_api import Page, expect

MOCHI_EMAIL = os.getenv("MOCHI_EMAIL")
MOCHI_PASSWORD = os.getenv("MOCHI_PASSWORD")


@pytest.fixture(scope="session", autouse=True)
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
    expect(account_holder_name).to_have_text("Eugene", use_inner_text=True, timeout=20000)
    page.wait_for_load_state()
    context.storage_state(path="state.json")

    yield context


@pytest.fixture(scope="function")
def login(browser):
    context = browser.new_context(storage_state="state.json")
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
