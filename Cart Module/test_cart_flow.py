from playwright.sync_api import expect
from POM.SauceDemo_Checkout import CartPage


def test_TC03_cart_flow(inventory_page, base_url):
    inventory_page.add_item("sauce-labs-backpack")
    inventory_page.add_item("sauce-labs-bike-light")
    inventory_page.add_item("test.allthethings()-t-shirt-(red)")
    inventory_page.remove_item("sauce-labs-bike-light")

    assert inventory_page.get_cart_count() == 2

    inventory_page.navigate_to_cart()
    expect(inventory_page.page).to_have_url(f"{base_url}/cart.html")


def test_TC04_total_product_prices_cart_price_match(inventory_page):
    checkout = CartPage(inventory_page.page)

    # Step 1: Capture product prices
    prices = inventory_page.product_prices()

    # Step 2: Add all items
    inventory_page.add_all_items()

    # Step 3: Verify cart badge count
    inventory_page.check_product_cart_count(len(prices))

    # Step 4: Navigate to cart
    inventory_page.navigate_to_cart()

    # Step 5: Checkout steps
    checkout.click_checkout()
    checkout.enter_checkout_details("nikita", "kataria", "324009")
    checkout.click_continue()

    # Step 6: Capture total
    total = inventory_page.get_total_price()

    # Step 7: Validate total
    assert total == sum(prices), \
        f"Expected total {sum(prices)} but got {total}"


def test_TC05_sort_items_by_low_to_high_price(inventory_page):
    inventory_page.sort_by("Price (low to high)")
    prices = inventory_page.product_prices()

    assert prices == sorted(prices), \
        f"Prices are not sorted low to high: {prices}"


def test_TC06_sort_items_by_high_to_low_price(inventory_page):
    inventory_page.sort_by("Price (high to low)")
    prices = inventory_page.product_prices()

    assert prices == sorted(prices, reverse=True), \
        f"Prices are not sorted high to low: {prices}"


def test_TC07_low_to_high_first_item(inventory_page):
    inventory_page.sort_by("Price (low to high)")
    first_item = inventory_page.get_first_item_name()

    assert first_item == "Sauce Labs Onesie", \
        f"Expected 'Sauce Labs Onesie' but got {first_item}"