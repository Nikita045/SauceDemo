from playwright.sync_api import Page
import pytest
import os
from datetime import datetime
import allure
from POM.SauceDemo_Login_Page import Sauce_LoginPage


@pytest.fixture
def logged_in_page(page):
    login=Sauce_LoginPage(page)
    login.sauce_login("standard_user", "secret_sauce")
    return page

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