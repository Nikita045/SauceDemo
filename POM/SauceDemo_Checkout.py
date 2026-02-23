from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def checkout_btn(self):
        return self.page.locator('[data-test="checkout"]')

    @property
    def firstname_inp(self):
        return self.page.get_by_placeholder("First Name")

    @property
    def lastname_inp(self):
        return self.page.get_by_placeholder("Last Name")

    @property
    def postal_code_inp(self):
        return self.page.get_by_placeholder("Zip/Postal Code")

    @property
    def continue_shop_btn(self):
        return self.page.locator('[data-test="continue-shopping"]')

    @property
    def continue_btn(self):
        return self.page.get_by_role("button", name="Continue")

    @property
    def finish_btn(self):
        return self.page.get_by_role("button", name="Finish")

    @property
    def error_message(self):
        return self.page.locator('[data-test="error"]')

    def click_checkout(self):
        self.checkout_btn.click()

    def enter_checkout_details(self, firstname, lastname, postal_code):
        self.firstname_inp.fill(firstname)
        self.lastname_inp.fill(lastname)
        self.postal_code_inp.fill(postal_code)

    def click_continue_shop(self):
        self.continue_shop_btn.click()

    def click_continue(self):
        self.continue_btn.click()

    def click_finish(self):
        self.finish_btn.click()