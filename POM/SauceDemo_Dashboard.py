from playwright.sync_api import Page,expect

class SauceDemo_Inventory:

    def __init__(self,page:Page):
        self.page = page


    def add_item(self,item_name:str):
        # sauce - labs - backpack, sauce-labs-bike-light, test.allthethings()-t-shirt-(red),
        self.page.locator(f'[data-test="add-to-cart-{item_name}"]').click()

    def remove_item(self,item_name:str):
        #from-cart-sauce-labs-backpack,sauce-labs-bike-light,test.allthethings()-t-shirt-(red)
        self.page.locator(f'[data-test="remove-{item_name}"]').click()

    def get_cart_count(self) -> int:
        cart_badge = self.page.locator(".shopping_cart_badge")
        if cart_badge.count() == 0:
            return 0
        return int(cart_badge.inner_text())

    def navigate_to_cart(self):
        self.page.locator(".shopping_cart_link").click()