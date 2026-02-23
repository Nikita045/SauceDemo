from playwright.sync_api import expect
from POM.SauceDemo_Checkout import CartPage


def test_TC08_checkout_positive_flow(inventory_page):
    checkout = CartPage(inventory_page.page)

    inventory_page.add_item("sauce-labs-backpack")
    inventory_page.add_item("sauce-labs-bike-light")
    inventory_page.add_item("test.allthethings()-t-shirt-(red)")

    inventory_page.navigate_to_cart()

    checkout.click_checkout()
    checkout.enter_checkout_details("nikita", "kataria", "324009")
    checkout.click_continue()
    checkout.click_finish()

    expect(inventory_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )


def test_TC09_continue_shop_flow(inventory_page):
    checkout = CartPage(inventory_page.page)

    inventory_page.add_item("sauce-labs-backpack")
    inventory_page.add_item("sauce-labs-bike-light")
    inventory_page.add_item("test.allthethings()-t-shirt-(red)")

    inventory_page.navigate_to_cart()
    checkout.click_continue_shop()

    inventory_page.remove_item("sauce-labs-backpack")
    inventory_page.remove_item("sauce-labs-bike-light")

    assert inventory_page.get_cart_count() == 1


def test_TC10_checkout_negative_flow(inventory_page):
    checkout = CartPage(inventory_page.page)

    inventory_page.add_item("sauce-labs-backpack")
    inventory_page.add_item("sauce-labs-bike-light")

    inventory_page.navigate_to_cart()
    checkout.click_checkout()

    checkout.enter_checkout_details("", "", "324009")
    checkout.click_continue()

    expect(checkout.error_message).to_be_visible()
    expect(checkout.error_message).to_contain_text(
        "Error: First Name is required"
    )