import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from .HomePage import EpamIndexPage


class TestPageCases:

    @pytest.fixture(scope="session")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver

    @pytest.fixture(scope="class")
    def page(self, driver):
        home_page = EpamIndexPage(driver)
        home_page.open()
        yield home_page
        home_page.close()

    def test_perform_login(self, page):
        page.login("epam", "1234")
        page.check_user_is_logged('PITER CHAILOVSKII')

    def test_expected_navbar_sections(self, page):
        page.check_expected_navbar_names_presented("HOME", "CONTACT FORM", "SERVICE", "METALS & COLORS")

    @pytest.mark.parametrize("text", ['To include good practices\nand ideas from successful\nEPAM project',
                                      'To be flexible and\ncustomizable', 'To be multiplatform',
                                      'Already have good base\n(about 20 internal and\nsome external projects),'
                                      '\nwish to get more…'])
    def test_texts_below_icon_elements(self, page, text):
        page.check_expected_text_under_icons(text)

    def test_frame_has_epam_logo(self, page):
        page.check_frame_has_epam_logo()
        page.switch_back_to_default_content()

    @pytest.mark.parametrize("link_txt", ['https://github.com/epam/JDI'])
    def test_main_link_is_correct(self, page, link_txt):
        page.check_main_link_is_correct(link_txt)
