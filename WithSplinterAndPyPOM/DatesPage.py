import time
import math
from collections import namedtuple

import allure
from splinter import Browser
from pypom import page, Region
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from .AnyPageAbstracts import Base


class Dates(Base):

    @property
    def main_content(self):
        return self.MainContent(self)

    @property
    def log_sidebar(self):
        return self.LogSidebar(self)

    class MainContent(Region):
        _root_locator = ('css', 'main-content')
        _slider_size = '.ui-slider'
        _css_left_slider = '.uui-slider a'
        _elem = ('css', '.uui-slider a:nth-child(1)')
        _span_val = '.uui-slider a span'

        '''
        def move_left_slider_right_left(self, position):
            action = ActionChains(self.driver.driver)
            switch = self.driver.driver.find_elements_by_css_selector(self._css_left_slider)[0]
            action.click(switch).perform()
            current_switch_value = int(self.driver.driver.find_elements_by_css_selector(self._span_val)[0].text)
            key = Keys.ARROW_LEFT if position < current_switch_value else Keys.ARROW_RIGHT
            for counter in range(abs(position - current_switch_value)):
                action.send_keys(key).perform()
        '''
        @allure.step('Moving')
        def move_slider_to_position(self, desired_value: int, switch, switch_value):
            slider = self.driver.driver.find_element_by_css_selector(self._slider_size)
            slider_width = slider.size['width']
            shift = (slider_width / 100) * (
                    desired_value - switch_value) if desired_value == switch_value else (slider_width / 100) * (
                        desired_value - switch_value) - slider_width / 100
            action = ActionChains(self.driver.driver)
            action.drag_and_drop_by_offset(switch, shift, 0).perform()

        @allure.step('Moving left slider to position')
        def move_left_switch(self, desired_value: int):
            left_switch = self.driver.driver.find_elements_by_css_selector(self._css_left_slider)[0]
            current_switch_value = int(self.driver.driver.find_elements_by_css_selector(self._span_val)[0].text)
            self.move_slider_to_position(desired_value=desired_value, switch=left_switch,
                                         switch_value=current_switch_value)

        @allure.step('Moving right slider to position')
        def move_right_switch(self, desired_value: int):
            left_switch = self.driver.driver.find_elements_by_css_selector(self._css_left_slider)[1]
            current_switch_value = int(self.driver.driver.find_elements_by_css_selector(self._span_val)[1].text)
            self.move_slider_to_position(desired_value=desired_value, switch=left_switch,
                                         switch_value=current_switch_value)

        @allure.step('Get right slider current position')
        def get_right_slider_current_position(self):
            return int(self.driver.driver.find_elements_by_css_selector(self._span_val)[1].text)

        @allure.step('Get left slider current position')
        def get_left_slider_current_position(self):
            return int(self.driver.driver.find_elements_by_css_selector(self._span_val)[0].text)

    class LogSidebar(Region):
        _root_locator = ('tag', 'div[name="log-sidebar"]')
        _log_records = ('css', '.panel-body-list li')

        @allure.step('Get last log main info')
        def last_log_records_main_options(self):
            log_rows = self.find_element(*self._log_records)
            latest_row_words = log_rows.text.split()
            main_info = latest_row_words[2]
            to_or_from = main_info[main_info.find("(") + 1:main_info.find(")")]
            value = int(main_info[main_info.find(":") + 1:])
            words = namedtuple('words', ['to_or_from', 'value'])
            return words(to_or_from, value)

    @allure.step('Assert last log row matches current slider state')
    def check_last_log_match_actual_element_state(self):
        log_state = self.log_sidebar.last_log_records_main_options()
        if log_state.to_or_from == 'To':
            assert self.main_content.get_right_slider_current_position() == log_state.value
        elif log_state.to_or_from == 'From':
            assert self.main_content.get_left_slider_current_position() == log_state.value
