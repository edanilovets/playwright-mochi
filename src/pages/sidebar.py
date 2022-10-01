from playwright.sync_api import Page


class Sidebar:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar_container = page.locator(".side-bar-container")
        self.account_holder_name = page.locator(
            ".memo_views_side-bar_account_account-holder-name")
        self.close_sidebar_button = page.locator(
            "text=EugeneproAll syncedSearch⌘ KDashboardDue today39New cardsSettingsDecksGet Starte >> button")
        self.open_sidebar_button = page.locator("button").nth(1)
        self.account_settings_button = page.locator("text=Account settings")

        # Main menu
        self.settings_button = page.locator("text=Settings")

        # Account settings modal
        self.account_settings_modal = page.locator(
            "#modal-container div:has-text(\"Account settingsThanks for using Mochi! If you have any questions about your acc\")").first

        # Review settings modal
        self.review_settings_button = page.locator("text=Review Settings")
        self.review_settings_modal_header = page.locator("h1:has-text('Review Settings')")

    def get_account_holder_name(self) -> str:
        return self.account_holder_name.inner_text(timeout=20000)
