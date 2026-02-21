from playwright.sync_api import Page,expect

from POM.SauceDemo_Dashboard import SauceDemo_Inventory
from POM.SauceDemo_Checkout import CartPage

def test_checkout_positive_flow(logged_in_page):
    page=logged_in_page
    inventory = SauceDemo_Inventory(page)
    checkout = CartPage(page)

    inventory.add_item("sauce-labs-backpack")
    inventory.add_item("sauce-labs-bike-light")
    inventory.add_item("test.allthethings()-t-shirt-(red)")
    inventory.navigate_to_cart()
    checkout.click_checkout()
    checkout.enter_checkout_details("nikita","kataria","324009")
    checkout.click_continue()
    checkout.click_finish()

def test_continue_shop_flow(logged_in_page):
    page = logged_in_page
    inventory = SauceDemo_Inventory(page)
    checkout = CartPage(page)

    inventory.add_item("sauce-labs-backpack")
    inventory.add_item("sauce-labs-bike-light")
    inventory.add_item("test.allthethings()-t-shirt-(red)")
    inventory.navigate_to_cart()
    checkout.click_continue_shop()
    inventory.remove_item("sauce-labs-backpack")
    inventory.remove_item("sauce-labs-bike-light")




def test_checkout_negative_flow(logged_in_page):
    page = logged_in_page
    inventory = SauceDemo_Inventory(page)
    checkout = CartPage(page)

    inventory.add_item("sauce-labs-backpack")
    inventory.add_item("sauce-labs-bike-light")
    inventory.navigate_to_cart()
    checkout.click_checkout()
    checkout.enter_checkout_details("","","324009")
    checkout.click_continue()
    expect(checkout.error_message).to_be_visible()
    expect(checkout.error_message).to_contain_text("Error: First Name is required")