from playwright.sync_api import Page,expect

from POM.SauceDemo_Dashboard import SauceDemo_Inventory
from POM.SauceDemo_Login_Page import CART_URL


def test_cart_flow(logged_in_page):
    page=logged_in_page
    inventory = SauceDemo_Inventory(page)

    inventory.add_item("sauce-labs-backpack")
    inventory.add_item("sauce-labs-bike-light")
    inventory.add_item("test.allthethings()-t-shirt-(red)")
    inventory.remove_item("sauce-labs-bike-light")

    assert inventory.get_cart_count()==2
    inventory.navigate_to_cart()
    expect(page).to_have_url(CART_URL)