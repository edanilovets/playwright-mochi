from playwright.sync_api import Page


class Sidebar:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.account_holder_name = page.locator(
            ".memo_views_side-bar_account_account-holder-name")

    def get_account_holder_name(self) -> str:
        return self.account_holder_name.inner_text(timeout=20000)
