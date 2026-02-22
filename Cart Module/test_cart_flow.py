from playwright.sync_api import Page,expect

from POM.SauceDemo_Dashboard import SauceDemo_Inventory
from POM.SauceDemo_Login_Page import CART_URL
from POM.SauceDemo_Checkout import CartPage

def test_TC03_cart_flow(logged_in_page):
    page=logged_in_page
    inventory = SauceDemo_Inventory(page)

    inventory.add_item("sauce-labs-backpack")
    inventory.add_item("sauce-labs-bike-light")
    inventory.add_item("test.allthethings()-t-shirt-(red)")
    inventory.remove_item("sauce-labs-bike-light")

    assert inventory.get_cart_count()==2
    inventory.navigate_to_cart()
    expect(page).to_have_url(CART_URL)

def test_TC04_total_product_prices_cart_price_match(logged_in_page):
    page=logged_in_page
    inventory = SauceDemo_Inventory(page)
    checkout=CartPage(page)
    # Step 1: Capture product prices
    prices=inventory.product_prices()
    # Step 2: Add all items
    inventory.add_all_items()
    # Step 3: Verify cart badge count
    inventory.check_product_cart_count(len(prices))
    # Step 4: Navigate to cart
    inventory.navigate_to_cart()
    # Step 5: Proceed to checkout overview
    checkout.click_checkout()
    checkout.enter_checkout_details("nikita", "kataria", "324009")
    #Step 6: Proceed to continue
    checkout.click_continue()
    # Step 7: Capture total
    total = inventory.get_total_price()

    # Step 8: Validate total
    assert total == sum(prices), \
        (f"Expected t"
         f"total {sum(prices)} but got {total}")

def test_TC05_sort_items_by_low_to_high_price(logged_in_page):
    page=logged_in_page
    inventory = SauceDemo_Inventory(page)
    checkout=CartPage(page)

    # Step 1: Apply sort
    inventory.sort_by("Price (low to high)")

    # Step 2: Capture prices
    prices = inventory.product_prices()

    # Step 3: Validate sorting
    assert prices == sorted(prices), \
        f"Prices are now sorted low to high: {prices}"

def test_TC06_sort_items_by_high_to_low_price(logged_in_page):
    page=logged_in_page
    inventory = SauceDemo_Inventory(page)
    checkout=CartPage(page)

    # Step 1: Apply sort
    inventory.sort_by("Price (high to low)")

    # Step 2: Capture prices
    prices = inventory.product_prices()

    # Step 3: Validate sorting
    assert prices == sorted(prices,reverse=True), \
        f"Prices are now sorted low to high: {prices}"


def test_TC07_low_to_high_first_item(logged_in_page):
    page = logged_in_page
    inventory = SauceDemo_Inventory(page)

    # Apply sort
    inventory.sort_by("Price (low to high)")

    # Get first item
    first_item = inventory.get_first_item_name()

    # Validate
    assert first_item == "Sauce Labs Onesie", \
        f"Expected 'Sauce Labs Onesie' but got {first_item}"


