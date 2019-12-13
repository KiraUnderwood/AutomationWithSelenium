from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from selenium import webdriver


class AnyPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open(self):
        return self.driver.get(self.url)

    def close(self):
        return self.driver.quit()
