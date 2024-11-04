import json
import allure
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_browser = Chrome(options=options)
    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture
def main_page(browser):
    return MainPage(browser)
