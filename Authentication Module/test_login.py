from playwright.sync_api import Page,expect
from POM.SauceDemo_Login_Page import Sauce_LoginPage, INVENTORY_URL
import pytest

@pytest.mark.parametrize("username,password, error_message", [
    ("nikita", "secret_sauce","Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce","Epic sadface: Sorry, this user has been locked out."),])
def test_TC01_invalid_login(page:Page,username,password,error_message):
    login_user=Sauce_LoginPage(page)
    login_user.sauce_login(username,password)
    expect(login_user.error_val).to_have_text(error_message)


@pytest.mark.parametrize("username,password", [
    ("standard_user","secret_sauce"),])
def test_TC02_valid_login(page:Page,username,password):
    login_user=Sauce_LoginPage(page)
    login_user.sauce_login(username,password)
    expect(login_user.page).to_have_url(INVENTORY_URL)

