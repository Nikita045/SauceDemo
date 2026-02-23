from playwright.sync_api import Page


class Sauce_LoginPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def username_inp(self):
        return self.page.get_by_placeholder("Username")

    @property
    def password_inp(self):
        return self.page.get_by_placeholder("Password")

    @property
    def login_btn(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def error_val(self):
        return self.page.locator('[data-test="error"]')

    def sauce_login(self, username, password):
        self.username_inp.fill(username)
        self.password_inp.fill(password)
        self.login_btn.click()