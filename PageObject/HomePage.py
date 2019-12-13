import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium import webdriver

from .AnyPage import AnyPage


class EpamIndexPage(AnyPage):
    url = "https://epam.github.io/JDI/index.html"

    class Locators:
        LOGIN_FORM = (By.ID, "user-icon")
        LOGIN_USER_FIELD = (By.TAG_NAME, 'input[id="name"]')
        LOGIN_USER_PWD = (By.TAG_NAME, 'input[id="password"]')
        BTN_SUBMIT = (By.TAG_NAME, 'button[type="submit"]')
        LOGGED_IN_USER = (By.ID, 'user-name')
        FAILED_LOGIN = (By.CLASS_NAME, "login-txt")
        NAV_BAR_ELEMS = (By.CSS_SELECTOR, "ul.nav.m-l8>li")
        TXT_ICONS = (By.CSS_SELECTOR, ".col-sm-3 .benefit-txt")
        FRAME = (By.TAG_NAME, "iframe")
        LOGO_EPAM = (By.ID, "epam_logo")
        LINK_NAME = (By.LINK_TEXT, "JDI GITHUB")

    def __init__(self, driver, url=url):
        super().__init__(driver, url)
        self.locators = self.Locators()

    def login(self, user_name, pwd):
        self.driver.find_element(*self.locators.LOGIN_FORM).click()
        self.driver.find_element(*self.locators.LOGIN_USER_FIELD).send_keys(user_name)
        self.driver.find_element(*self.locators.LOGIN_USER_PWD).send_keys(pwd)
        self.driver.find_element(*self.locators.BTN_SUBMIT).click()
        # to-do: add check the login succeeded
        self.driver.find_element(*self.locators.FAILED_LOGIN)
        if self.driver.find_element(*self.locators.FAILED_LOGIN).is_displayed():
            raise Exception("It seems the login has failed!")

    def check_user_is_logged(self, user_name):
        try:
            logged_in_user = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.locators.LOGGED_IN_USER))
        except TimeoutException as e:
            logged_in_user = False
        assert logged_in_user and logged_in_user.text.lower() == user_name.lower(), f"There is no icon 'user-name' on the page or the text of the icon does not match given pattern: '{user_name}'"

    def nav_bar_sections_displayed_names(self):
        all_section_objects_insluding_iframe = self.driver.find_elements(*self.locators.NAV_BAR_ELEMS)
        section_names = [name.text.lower() for name in all_section_objects_insluding_iframe if name.is_displayed()]
        return section_names

    def check_expected_navbar_names_presented(self, *args):
        section_names = self.nav_bar_sections_displayed_names()
        assert [section.lower() in section_names for section in args]

    def get_texts_under_main_icons(self):
        texts_under_icons = [txt.text.lower() for txt in self.driver.find_elements(*self.locators.TXT_ICONS) if
                             txt.is_displayed()]
        return texts_under_icons

    def check_expected_text_under_icons(self, text):
        presented_texts = self.get_texts_under_main_icons()
        assert text.lower() in presented_texts

    def switch_to_frame(self):
        try:
            frame = self.driver.find_element(*self.locators.FRAME)
        except NoSuchElementException:
            raise NoSuchElementException("The frame is not present on the page!")
        if frame.is_displayed():
            self.driver.switch_to.frame(frame)
        else:
            raise ElementNotVisibleException("The frame is not displayed!")

    def check_frame_has_epam_logo(self):
        self.switch_to_frame()
        assert self.driver.find_element(*self.locators.LOGO_EPAM).is_displayed()

    def switch_back_to_default_content(self):
        self.driver.switch_to.default_content()

    def check_main_link_is_correct(self, link_text):
        link = self.driver.find_element(*self.locators.LINK_NAME)
        assert link.get_attribute("href") == link_text




