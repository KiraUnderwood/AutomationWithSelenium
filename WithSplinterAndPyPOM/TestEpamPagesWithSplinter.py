import pytest
import datetime
import allure

from splinter import Browser

from .MainPage import MainPage
from .DifferentElementsPage import DifferentElements


class TestEpamIndexPage:
    @pytest.fixture(scope="session")
    def driver(self, request):
        with Browser(driver_name="chrome") as b:
            b.driver.maximize_window()
            yield b

    @pytest.fixture(scope="class")
    def home_page(self, driver):
        home_page = MainPage(driver)
        home_page.open()
        yield home_page

    @allure.description("""
                    Browser tab name is reflected
                    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_tab_title(self, home_page):
        home_page.check_tab_title_matches("Home page")

    @allure.description("""
                    Check the user login
                    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, home_page):
        home_page.header.login("epam", "1234")
        home_page.header.check_current_user('PITER CHAILOVSKII')

    @pytest.fixture(scope="class")
    def options(self, home_page):
        return home_page.header.get_service_submenu_sections()

    @allure.description("""
                    Check the content of the top nav bar contains expected sections
                    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("section", ["Supports", "Dates", "Complex Table", "Simple Table", "Table With Pages",
                                         "Different Elements"])
    def test_top_service_list_content(self, home_page, options, section):
        # home_page.header.get_service_submenu_sections()
        home_page.header.check_the_option_is_presented_in_dropdown(section, options)

    @pytest.fixture(scope="class")
    def options_sidebar(self, home_page):
        return home_page.sidebar.get_service_submenu_sections()

    @allure.description("""
                Left-side nav bar should contain certain menu options
                """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("section", ["Support", "Dates", "Complex Table", "Simple Table", "Table With Pages",
                                         "Different Elements"])
    def test_left_service_list_content(self, home_page, options_sidebar, section):
        home_page.sidebar.check_the_option_is_presented_in_dropdown(section, options_sidebar)

    @pytest.fixture(scope="class")
    def elements_page(self, home_page, driver):
        home_page.header.go_to_different_elements_page()
        yield DifferentElements(driver, driver.url)

    @allure.description("""
                Checkboxes, radio and dropdown list presented in expected quantity
                """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("story_1")
    def test_different_elements_page_elements_present(self, elements_page):
        elements_page.main_content.check_checkboxes_present_count(4)
        elements_page.main_content.check_radiobuttons_present_count(4)
        elements_page.main_content.check_dropdownlist_present_count(1)
        elements_page.main_content.check_buttons_present_count(2)

    @allure.description("""
                    Check log section is present on the right
                    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_right_section_present_on_elements_page(self, elements_page):
        assert elements_page.log_sidebar.is_present()

    @allure.description("""
                    Check the left-side nav bar with options is present
                    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_left_section_present_on_elements_page(self, elements_page):
        assert elements_page.sidebar.is_present()

    @allure.description("""
                Logs for checkboxes should be presented and last only reflects the sate of the element
                """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('story_2')
    def test_checkbox_logs(self, elements_page):
        elements_page.main_content.select_given_checkboxes('Water', 'Wind')
        elements_page.check_last_log_match_actual_element_state()

    @allure.description("""
                    Check picking radiobutton produces the log record
                    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_radiobutton_logs(self, elements_page):
        elements_page.main_content.select_given_radiobutton('Selen')
        elements_page.check_last_log_match_actual_element_state()

    @allure.description("""
                    Check picking the option from the drop-down list produces the log record
                    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_list_logs(self, elements_page):
        elements_page.main_content.select_from_dropdown('Yellow')
        elements_page.check_last_log_match_actual_element_state()

    @allure.description("""
                    Check clearing of the check-boxes produces the log record
                    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clear_flags_logs(self, elements_page):
        elements_page.main_content.untick_all_checkboxes()
        elements_page.check_last_log_match_actual_element_state()
