from playwright.sync_api import Page


class SauceDemo_Inventory:

    def __init__(self, page: Page):
        self.page = page

    # ---------------- ADD ITEMS ---------------- #

    def add_all_items(self):
        add = self.page.locator('button[data-test^="add-to-cart"]')
        count = add.count()
        for i in range(count): add.nth(0).click()

    def add_item(self, item_name: str):
        self.page.locator(
            f'[data-test="add-to-cart-{item_name}"]'
        ).click()

    # ---------------- REMOVE ITEMS ---------------- #

    def remove_all_items(self):
        buttons = self.page.locator('[data-test^="remove"]')
        count = buttons.count()

        for i in range(count):
            buttons.nth(i).click()

    def remove_item(self, item_name: str):
        self.page.locator(
            f'[data-test="remove-{item_name}"]'
        ).click()

    # ---------------- NAVIGATION ---------------- #

    def navigate_to_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()
        self.page.wait_for_url("**/cart.html")

    # ---------------- CART ---------------- #

    def get_cart_count(self) -> int:
        cart_badge = self.page.locator(".shopping_cart_badge")

        if cart_badge.count() == 0:
            return 0

        return int(cart_badge.inner_text())

    def check_product_cart_count(self, expected_count: int):
        actual_count = self.get_cart_count()

        assert actual_count == expected_count, \
            f"Cart count {actual_count} does not match expected {expected_count}"

    # ---------------- PRICES ---------------- #

    def product_prices(self):
        price_locators = self.page.locator('[data-test="inventory-item-price"]')
        count = price_locators.count()

        prices = []
        for i in range(count):
            price_text = price_locators.nth(i).inner_text()
            price_value = float(price_text.replace("$", "").strip())
            prices.append(price_value)

        return prices

    def get_total_price(self):
        total_locator = self.page.locator(".summary_subtotal_label")
        total_text = total_locator.inner_text()

        return float(total_text.split("$")[1])

    # ---------------- SORTING ---------------- #

    def sort_by(self, option: str):
        self.page.locator('[data-test="product-sort-container"]').select_option(
            label=option
        )

    def get_first_item_name(self) -> str:
        return self.page.locator(".inventory_item_name").first.inner_text()
