from pytest_bdd import scenario, given, when, then, scenarios, parsers
import pytest

'''
CALL TESTS FROM FEATURES FOLDER:
'''

scenarios('../features/DifferentElements.feature')

'''
STEPS FOR THE FEATURE DIFFERENT ELEMENTS:
'''


@pytest.fixture(scope='session')
def service_in_the_header(home_page):
    return home_page.header.get_service_submenu_sections()


given('I click on "Service" in the header to get the dropdownlist options', fixture='service_in_the_header')


@then('I should see <category> subcategory in header:')
def check_subcategories(home_page, service_in_the_header, category):
    home_page.header.check_the_option_is_presented_in_dropdown(expected_option=category, options=service_in_the_header)


@pytest.fixture(scope='session')
def service_in_the_sidebar(home_page):
    return home_page.sidebar.get_service_submenu_sections()


given('I click on "Service" in the side nav-bar', fixture='service_in_the_sidebar')


@then('I should see  <category> subcategory in sidebar:')
def check_subcategories_sidebar(home_page, service_in_the_sidebar, category):
    home_page.sidebar.check_the_option_is_presented_in_dropdown(expected_option=category,
                                                                options=service_in_the_sidebar)


@then('I should be on Different Elements page')
def check_you_are_on_dif_elem_page(elements_page):
    assert elements_page.driver.url == 'https://epam.github.io/JDI/different-elements.html'


@then('I should see <checkboxes> checkboxes')
def checkboxes_count(elements_page, checkboxes):
    elements_page.main_content.check_checkboxes_present_count(int(checkboxes))


@then('I should see <radiobuttons> radiobuttons')
def radiobutton_count(elements_page, radiobuttons):
    elements_page.main_content.check_radiobuttons_present_count(int(radiobuttons))


@then('I should see <dropdown> dropdown list')
def dropdown_count(elements_page, dropdown):
    elements_page.main_content.check_dropdownlist_present_count(int(dropdown))


@then('I should see <buttons> buttons')
def buttons_count(elements_page, buttons):
    elements_page.main_content.check_buttons_present_count(int(buttons))


@when('I select <checkbox> checkbox')
def select_checkbox(elements_page, checkbox):
    elements_page.main_content.select_given_checkboxes(checkbox)


@when('I select <radio> radiobutton')
def select_radio(elements_page, radio):
    elements_page.main_content.select_given_radiobutton(radio)


@when('I select <opt> from dropdown')
def select_dropdown(elements_page, opt):
    elements_page.main_content.select_from_dropdown(opt)


@when('I un-tick all checkboxes')
def uncheck_all(elements_page):
    elements_page.main_content.untick_all_checkboxes()


@then('I should see corresponding log')
def check_the_log(elements_page):
    elements_page.check_last_log_match_actual_element_state()
