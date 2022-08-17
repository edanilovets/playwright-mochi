import pytest
from playwright.sync_api import Page

from pages.login import LoginPage
from pages.sidebar import Sidebar


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def sidebar(page: Page) -> Sidebar:
    return Sidebar(page)
