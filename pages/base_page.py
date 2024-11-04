from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.windows = None
        self.browser = browser

    def find(self, locator):
        return self.browser.find_element(*locator)

    def open(self, url):
        self.browser.get(url)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(("tag name", "body"))
        )
