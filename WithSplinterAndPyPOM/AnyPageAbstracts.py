import allure

from splinter import Browser
from pypom import Page, Region


class Base(Page):

    @property
    def header(self):
        return self.Header(self)

    @property
    def sidebar(self):
        return self.Sidebar(self)

    def check_tab_title_matches(self, tab_title):
        assert self.driver.title.lower().strip() == tab_title.lower().strip(), f"The page title does not match given expected!"

    class Header(Region):
        _root_locator = ('id', 'header')
        _menu_sections = ('css', 'ul.nav.m-l8>li')
        _logout_displayed = ('css', 'logout')
        _login_displayed = ('id', 'login-form')
        _login_form_call = ('id', 'user-icon')
        ID_Login_Form = 'login-form'
        _field_login = ('tag', 'input[id="name"]')
        _field_pwd = ('tag', 'input[id="password"]')
        _btn_login_submit = ('tag', 'button[type="submit"]')
        _failed_login = ('css', 'login-txt')
        _logged_user = ('id', 'user-name')
        _service_drop = ('css', '.dropdown-toggle')
        _service_drop_elements = ('css', '.dropdown-menu a')

        def is_displayed(self):
            return self.is_element_displayed(*self._root_locator)

        def check_logo_is_displayed(self):
            raise NotImplementedError("The method not yet implemented!")

        @allure.step('Get displayed sections')
        def get_displayed_menu_sections_names(self):
            return [section.text.lower().strip() for section in self.find_elements(*self._menu_sections) if
                    self.is_element_displayed(section)]

        @allure.step('Check the sections names match expected')
        def check_menu_sections_match_expected(self, *args):
            actual = self.get_displayed_menu_sections_names()
            assert len(actual) == len(args)
            assert [section.lower().strip() in actual for section in args]

        def logout(self):
            if self.is_element_displayed(*self._logout_displayed):
                self.find_element(*self._logout_displayed).click()
            else:
                print("No one is logged in")

        @allure.step('Login')
        def login(self, user, pwd):
            self.find_element(*self._login_form_call).click()
            if self.is_element_displayed(*self._login_displayed):
                self.find_element(*self._field_login).type(user)
                self.find_element(*self._field_pwd).type(pwd)
                self.find_element(*self._btn_login_submit).click()
                if self.is_element_displayed(*self._failed_login):
                    raise Exception("Login has failed!")
            else:
                raise Exception("Someone is already logged in")

        @allure.step('Check the user is logged in')
        def check_current_user(self, expected_user):
            if self.is_element_displayed(*self._logged_user):
                assert self.find_element(*self._logged_user).text.lower().strip() == expected_user.lower().strip()

        @allure.step('Get "service" submenu sections')
        def get_service_submenu_sections(self):
            dropdown = self.find_element(*self._service_drop)
            assert dropdown.text.lower().strip() == 'service', f"Dropdown menu is not called 'service', its {dropdown.text}"
            dropdown.click()
            sections = self.find_elements(*self._service_drop_elements)
            if sections:
                names = [sect.text.lower().strip() for sect in sections if sect.visible]
                if names:
                    return names
            else:
                raise Exception("No dropdown elements being displayed were collected")

        @allure.step('Check the sections is present in a drop-down')
        def check_the_option_is_presented_in_dropdown(self, expected_option, options):
            # options = self.get_service_submenu_sections()
            assert expected_option.lower().strip() in options, f"The option {expected_option} is not found in a dropdown"

        @allure.step('Go to "Different Elements" page')
        def go_to_different_elements_page(self):
            self.find_element(*self._service_drop).click()
            self.driver.click_link_by_text("Different elements")

        @allure.step('Go to "Dates" page')
        def go_to_dates_page(self):
            self.find_element(*self._service_drop).click()
            self.driver.click_link_by_text("Dates")


    class Sidebar(Region):
        _root_locator = ('tag', 'div[name="log-sidebar"]')
        _tag_root = 'div[name="log-sidebar"]'
        _service_drop = ('css', '.menu-title[index="3"]')
        _service_drop_elements = ('css', '.menu-title[index="3"] .sub li')

        @allure.step('Return F/T if the log-sidebar presented')
        def is_displayed(self):
            return self.is_element_displayed(*self._root_locator)
            # return self.root.is_displayed()

        @allure.step('Return F/T if the log-sidebar presented')
        def is_present(self):
            return self.driver.is_element_present_by_css(self._tag_root)

        @allure.step('Get "Service" sections')
        def get_service_submenu_sections(self):
            dropdown = self.find_element(*self._service_drop)
            # assert dropdown.text.lower().strip() == 'service', f"Dropdown menu is not called 'service', its {dropdown.text.lower().strip()}"
            dropdown.click()
            sections = self.find_elements(*self._service_drop_elements)
            if sections:
                names = [sect.text.lower().strip() for sect in sections if sect.visible]
                if names:
                    return names
            else:
                raise Exception("No dropdown elements being displayed were collected")

        @allure.step('Check the option is presented in the "Service" dropdown')
        def check_the_option_is_presented_in_dropdown(self, expected_option, options):
            # options = self.get_service_submenu_sections()
            assert expected_option.lower().strip() in options, f"The option {expected_option} is not found in a dropdown"
