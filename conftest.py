from playwright.sync_api import Playwright, Page, sync_playwright
import pytest
import os
from datetime import datetime
import allure

from POM.SauceDemo_Dashboard import SauceDemo_Inventory
from POM.SauceDemo_Login_Page import Sauce_LoginPage

@pytest.fixture(scope="session")
def base_url():
    env=os.getenv("ENV","qa")
    urls={
        "qa":"https://www.saucedemo.com",
        "dev":"https://www.saucedemo.com"
    }
    return urls[env]

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def logged_in_page(page,base_url):
    page.goto(base_url)
    login=Sauce_LoginPage(page)
    login.sauce_login("standard_user", "secret_sauce")
    return page

@pytest.fixture
def inventory_page(logged_in_page):
    return SauceDemo_Inventory(logged_in_page)


def pytest_configure(config):
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    if config.option.htmlpath:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        config.option.htmlpath = os.path.join(
            reports_dir, f"report_{timestamp}.html"
        )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            timestamp = datetime.now().strftime("%H%M%S")
            screenshot_path = f"reports/{item.name}_{timestamp}.png"
            # Take screenshot once
            screenshot_bytes = page.screenshot(path=screenshot_path)

            # Attach same screenshot to Allure
            allure.attach(
                screenshot_bytes,
                name=f"{item.name}_failure",
                attachment_type=allure.attachment_type.PNG
            )