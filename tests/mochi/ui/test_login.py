"""
Login tests suite.
"""
import os
import re

import pytest
from playwright.sync_api import Page, expect

from pages.login import LoginPage
from pages.sidebar import Sidebar

MOCHI_USER = os.getenv("MOCHI_USER")
MOCHI_PASSWORD = os.getenv("MOCHI_PASSWORD")


def test_login_with_valid_credentials(page: Page, login_page: LoginPage, sidebar: Sidebar):
    login_page.open()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Mochi"))

    login_page.login(MOCHI_USER, MOCHI_PASSWORD)

    # Expect a account holder name "to contain" a substring.
    expect(sidebar.account_holder_name).to_have_text("Eugene", use_inner_text=True, timeout=20000)


def test_login_with_invalid_credentials(page: Page, login_page: LoginPage):
    login_page.open()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Mochi"))

    # Specify wrong password
    login_page.login(MOCHI_USER, "password")

    # Expect a account holder name "to contain" a substring.
    expect(login_page.login_form).to_contain_text("Invalid email / password combination")
