from playwright.sync_api import expect
from src.pages.sidebar import Sidebar


def test_can_open_review_settings_menu(sidebar: Sidebar):

    sidebar.settings_button.click()
    sidebar.review_settings_button.click()
    expect(sidebar.review_settings_modal_header).to_be_visible()


def test_can_open_account_settings_menu(sidebar: Sidebar):

    expect(sidebar.account_settings_modal).to_be_hidden()
    sidebar.account_holder_name.click()
    sidebar.account_settings_button.click()
    expect(sidebar.account_settings_modal).to_be_visible()
