from playwright.sync_api import Page,expect

from POM.SauceDemo_Dashboard import SauceDemo_Inventory

BASE_URL = "https://www.saucedemo.com"
INVENTORY_URL = f"{BASE_URL}/inventory.html"
CART_URL=f"{BASE_URL}/cart.html"
class Sauce_LoginPage:

    def __init__(self,page:Page):
        self.page=page
        self.page.goto(BASE_URL)
        self.username_inp=self.page.get_by_placeholder("Username")
        self.password_inp=self.page.get_by_placeholder("Password")
        self.login_btn=self.page.get_by_role("button",name="Login")
        self.error_val=self.page.locator("div.error-message-container.error")


    def sauce_login(self,username,password):
        self.username_inp.fill(username)
        self.password_inp.fill(password)
        self.login_btn.click()
        return SauceDemo_Inventory(self.page)


