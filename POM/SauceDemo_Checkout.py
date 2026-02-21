from playwright.sync_api import Page


class CartPage:

    def __init__(self,page:Page):
        self.page = page
        self.checkout_btn=self.page.locator('[data-test="checkout"]')
        self.firstname_inp=self.page.get_by_placeholder("First Name")
        self.lastname_inp=self.page.get_by_placeholder("Last Name")
        self.postal_code_inp=self.page.get_by_placeholder("Zip/Postal Code")
        self.continue_shop_btn=self.page.locator('[data-test="continue-shopping"]')
        self.continue_btn=self.page.get_by_role("button",name="Continue")
        self.finish_btn=self.page.get_by_role("button",name="Finish")
        self.error_message=self.page.locator('[data-test="error"]')

    def click_checkout(self):
        self.checkout_btn.click()

    def enter_checkout_details(self,firstname,lastname,postal_code):
        self.firstname_inp.fill(firstname)
        self.lastname_inp.fill(lastname)
        self.postal_code_inp.fill(postal_code)

    def click_continue_shop(self):
        self.continue_shop_btn.click()

    def click_continue(self):
        self.continue_btn.click()

    def click_finish(self):
        self.finish_btn.click()
