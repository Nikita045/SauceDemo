from playwright.sync_api import Page,expect

class SauceDemo_Inventory:

    def __init__(self,page:Page):
        self.page = page
    #newly added
    def add_all_items(self):
        buttons = self.page.locator('button[data-test^="add-to-cart"]')
        count = buttons.count()

        for i in range(count):
            buttons.nth(0).click()

    def add_item(self,item_name:str):
        # sauce - labs - backpack, sauce-labs-bike-light, test.allthethings()-t-shirt-(red),
        self.page.locator(f'[data-test="add-to-cart-{item_name}"]').click()
    #newly added
    def remove_all_items(self):
        for button in self.page.locator('[data-test^="remove"]').all():
            button.click()

    def remove_item(self,item_name:str):
        #from-cart-sauce-labs-backpack,sauce-labs-bike-light,test.allthethings()-t-shirt-(red)
        self.page.locator(f'[data-test="remove-{item_name}"]').click()

    def navigate_to_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def get_cart_count(self) -> int:
        cart_badge = self.page.locator(".shopping_cart_badge")
        if cart_badge.count() == 0:
            return 0
        return int(cart_badge.inner_text())

    def check_product_cart_count(self, expected_count: int) -> None:
        cart_badge = self.page.locator(".shopping_cart_badge")

        if cart_badge.count() == 0:
            badge_count = 0
        else:
            badge_count = int(cart_badge.inner_text())

        assert badge_count == expected_count, \
            f"Cart count {badge_count} does not match expected count {expected_count}"

    # newly added
    def product_prices(self):
        price_locators=self.page.locator('[data-test="inventory-item-price"]')
        prices=[]
        for i in range(price_locators.count()):
            price_text=price_locators.nth(i).inner_text()
            price_value=float(price_text.replace('$','').strip())
            prices.append(price_value)

        return prices

    def get_total_price(self):
        total_text=self.page.locator(".summary_subtotal_label")
        total_value=float(total_text.inner_text().split("$")[1])
        return total_value

    def sort_by(self, option: str):
        #option-["Name (A to Z)", "Name (Z to A)", "Price (low to high)","Price (high to low)"]
        self.page.locator(".product_sort_container").select_option(label=option)

    def get_first_item_name(self) -> str:
        return self.page.locator(".inventory_item_name").first.inner_text()