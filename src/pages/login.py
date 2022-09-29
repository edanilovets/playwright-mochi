from playwright.sync_api import Page


class LoginPage:

    URL = 'https://app.mochi.cards'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_form = page.locator(".memo_views_modal_log-in_log-in-modal-container")
        self.email_input = page.locator("[placeholder=\"Email\"]")
        self.password_input = page.locator("[placeholder=\"Password\"]")
        self.login_button = page.locator("button:has-text(\"Log in\")")

    def open(self) -> None:
        self.page.goto(self.URL)

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
