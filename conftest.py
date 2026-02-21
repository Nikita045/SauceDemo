from playwright.sync_api import Page
import pytest
import os
from datetime import datetime

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
