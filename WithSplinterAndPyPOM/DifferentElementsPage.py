from string import Template
import time
from collections import namedtuple

from splinter import Browser
from pypom import page, Region

from .AnyPageAbstracts import Base


class DifferentElements(Base):

    @property
    def main_content(self):
        return self.MainContent(self)

    @property
    def log_sidebar(self):
        return self.LogSidebar(self)

    class MainContent(Region):
        _root_locator = ('css', 'main-content')
        _tag_checkboxes = ('tag', 'input[type="checkbox"]')
        _css_checkbox_text = ('css', '.label-checkbox')
        _checkbox_text = '.label-checkbox'
        _tag_radiobuttons = ('tag', 'input[type="radio"]')
        _css_radio_text = ('css', '.label-radio')
        _radio_text = '.label-radio'
        _tag_dropdownlist = ('tag', 'select')
        _tag_list_options = ('css', 'select option')
        _css_buttons = ('css', '.main-content .uui-button')
        _side_bar = ('name', 'log-sidebar')
        _radio_btn_name = 'metal'
        _list_option_xpath = Template('//select/option[text()="$option"]')

        def check_checkboxes_present_count(self, expected_number: int):
            list_of_checkbox = self.find_elements(*self._tag_checkboxes)
            assert len(list_of_checkbox) == expected_number

        def check_radiobuttons_present_count(self, expected_number: int):
            list_of_radiobuttons = self.find_elements(*self._tag_radiobuttons)
            assert len(list_of_radiobuttons) == expected_number

        def check_dropdownlist_present_count(self, expected_number: int):
            list_of_dropdowns = self.find_elements(*self._tag_dropdownlist)
            assert len(list_of_dropdowns) == expected_number

        def check_buttons_present_count(self, expected_number: int):
            list_of_buttons = self.find_elements(*self._css_buttons)
            assert len(list_of_buttons) == expected_number

        def select_given_checkboxes(self, *args):
            processed_args = [ar.lower().strip() for ar in args]
            list_of_checkbox = self.find_elements(*self._css_checkbox_text)
            [box.click() for box in list_of_checkbox if box.text.lower().strip() in processed_args]

        def select_given_radiobutton(self, option: str):
            radios = self.find_elements(*self._css_radio_text)
            [rad.click() for rad in radios if rad.text.lower().strip() == option.lower().strip()]

        def select_from_dropdown(self, option: str):
            self.find_element(*self._tag_dropdownlist).click()
            self.find_element('xpath', self._list_option_xpath.substitute(option=option)).click()
            time.sleep(20)

        def get_current_list_option(self):
            options = {option.text: option.checked for option in self.find_elements(*self._tag_list_options)}
            for key, value in options.items():
                if value:
                    return key.lower().strip()

        def get_current_checkboxes_statuses(self):
            names = [option_name.text for option_name in self.find_elements(*self._css_checkbox_text)]
            values = [option_value.checked for option_value in self.find_elements(*self._tag_checkboxes)]
            return dict(zip(names, values))

        def get_current_toggle(self):
            names = [option_name.text for option_name in self.find_elements(*self._css_radio_text)]
            values = [option_value.checked for option_value in self.find_elements(*self._tag_radiobuttons)]
            option = dict(zip(names, values))
            for key, value in option.items():
                if value:
                    return key.lower().strip()

        def untick_all_checkboxes(self):
            [option_value.uncheck() for option_value in self.find_elements(*self._tag_checkboxes)]



    class LogSidebar(Region):
        _root_locator = ('tag', 'div[name="log-sidebar"]')
        _tag_root = 'div[name="log-sidebar"]'
        _log_records = ('css', '.panel-body-list li')

        def last_log_records_main_options(self):
            log_rows = self.find_element(*self._log_records)
            latest_row_words = log_rows.text.split()
            words = namedtuple('words', ['first', 'last'])
            return words(latest_row_words[1], latest_row_words[-1])

        def is_present(self):
            return self.driver.is_element_present_by_tag(self._tag_root)

        def is_displayed(self):
            return self.is_element_displayed(*self._root_locator)

    def check_last_log_match_actual_element_state(self):
        log_status = self.log_sidebar.last_log_records_main_options()
        if log_status.first == "Colors:":
            print(log_status.first, ' color ', log_status.last)
            actual_list_option = self.main_content.get_current_list_option()
            assert actual_list_option == log_status.last.lower().strip(), f"{actual_list_option} does not match {log_status.last.lower().strip()}"
        elif log_status.first == "metal:":
            print(log_status.first, ' metal ', log_status.last)
            actual_toggle = self.main_content.get_current_toggle()
            assert actual_toggle == log_status.last.lower().strip(), f"{actual_toggle} does not match {log_status.last.lower().strip()}"
        else:
            print(log_status.first, ' last ', log_status.last)
            log_value = True if log_status.last == 'true' else False
            checkbox_statuses = self.main_content.get_current_checkboxes_statuses()
            assert checkbox_statuses.get(log_status.first.replace(':',
                                                                  '')) == log_value, f"{checkbox_statuses.get(log_status.first.replace(':', ''))} does not match {log_value}"
