import pytest
import datetime

import allure
from splinter import Browser

from .MainPage import MainPage
from .DatesPage import Dates


class TestDatesPage:
    @pytest.fixture(scope="session")
    def driver(self):
        with Browser(driver_name="chrome") as b:
            b.driver.maximize_window()
            yield b

    @pytest.fixture(scope="class")
    def home_page(self, driver):
        home_page = MainPage(driver)
        home_page.open()
        yield home_page

    def test_login(self, home_page):
        home_page.header.login("epam", "1234")
        home_page.header.check_current_user('PITER CHAILOVSKII')

    @pytest.fixture(scope="class")
    def dates_page(self, home_page, driver):
        home_page.header.go_to_dates_page()
        yield Dates(driver, driver.url)

    @allure.description("""
    Moving sliders to the edge values of the scale 0/100
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_range_sliders_move_0_100_logs(self, dates_page):
        dates_page.main_content.move_left_switch(0)
        dates_page.check_last_log_match_actual_element_state()
        dates_page.main_content.move_right_switch(100)
        dates_page.check_last_log_match_actual_element_state()

    @allure.description("""
        Moving sliders to the edge values of the scale 0/0
        """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_range_sliders_move_0_0_logs(self, dates_page):
        dates_page.main_content.move_left_switch(0)
        dates_page.check_last_log_match_actual_element_state()
        dates_page.main_content.move_right_switch(0)
        dates_page.check_last_log_match_actual_element_state()

    @allure.description("""
            Moving sliders to the edge values of the scale 100/100
            """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_range_sliders_move_100_100_logs(self, dates_page):
        dates_page.main_content.move_left_switch(100)
        dates_page.check_last_log_match_actual_element_state()
        dates_page.main_content.move_right_switch(100)
        dates_page.check_last_log_match_actual_element_state()

    @allure.description("""
            Moving sliders to any non-edge value of the scale 30/70
            """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_range_sliders_move_30_70_logs(self, dates_page):
        dates_page.main_content.move_left_switch(30)
        dates_page.check_last_log_match_actual_element_state()
        dates_page.main_content.move_right_switch(70)
        dates_page.check_last_log_match_actual_element_state()
