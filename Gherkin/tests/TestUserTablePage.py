from pytest_bdd import scenario, given, when, then, scenarios, parsers
import pytest

'''
CALL TESTS FROM FEATURES FOLDER:
'''

scenarios('../features/UserTable.feature')

'''
STEPS FOR THE FEATURE User Table:
spliner style (java analog: selenide) w/o page object

'''


@when('I click on "User Table" button in Service dropdown')
def go_to_user_table(driver):
    driver.find_by_css('.dropdown-toggle').click()
    driver.click_link_by_text("User Table ")


@then('"User Table" page is opened')
def check_the_page_is_user_table(driver):
    assert driver.url == 'https://epam.github.io/JDI/user-table.html'


@then('<dropdown> NumberType Dropdowns are displayed on Users Table on User Table Page')
def dropdowns_count(driver, dropdown):
    list_of_checkbox = driver.find_by_tag('select')
    assert len(list_of_checkbox) == int(dropdown)


@then('<name> User names are displayed on Users Table on User Table Page')
def names_count(driver, name):
    list_of_names = driver.find_by_css('td a[href]')
    assert len(list_of_names) == int(name)


@then('<img> Description images are displayed on Users Table on User Table Page')
def imgs_count(driver, img):
    list_of_img = driver.find_by_css('td img')
    assert len(list_of_img) == int(img)


@then('<txt> Description texts under images are displayed on Users Table on User Table Page')
def txts_count(driver, txt):
    list_of_descr = driver.find_by_css('.user-descr span')
    assert len(list_of_descr) == int(txt)


@then('<checkbox> checkboxes are displayed on Users Table on User Table Page')
def chkb_count(driver, checkbox):
    list_of_chkb = driver.find_by_tag('input[type="checkbox"]')
    assert len(list_of_chkb) == int(checkbox)


@then('User table contains following values <number> and <user_name>')
def table_content(driver, number, user_name):
    child = int(number) + 1
    columns = driver.find_by_css(f'table tr:nth-child({child}) td')
    assert columns[0].text.lower().strip() == number and columns[2].text.lower().strip() == user_name.lower().strip()


@when(parsers.parse('I select vip checkbox for "{user}"'))
def select_vip_for_user(driver, user):
    row_no = 2
    number_of_rows = len(driver.find_by_css('table tr')) - 1
    for row in range(number_of_rows):
        columns = driver.find_by_css(f'table tr:nth-child({row_no}) td')
        if columns[2].text.lower().strip() == user.lower().strip():
            driver.find_by_css(f'table tr:nth-child({row_no}) td input').click()
        row_no += 1


@then(parsers.parse('1 log row has "{phrase}" text in log section'))
def log_is_recorded(driver, phrase):
    last_log_row = driver.find_by_css('.info-panel-section li')[0].text.lower().strip()
    assert phrase.lower().strip() in last_log_row


@when(parsers.parse('I click on dropdown in column Type for user {user}'))
def dropdown_for_user(driver, user):
    row_no = 2
    number_of_rows = len(driver.find_by_css('table tr')) - 1
    for row in range(number_of_rows):
        columns = driver.find_by_css(f'table tr:nth-child({row_no}) td')
        if columns[2].text.lower().strip() == user.lower().strip():
            driver.find_by_css(f'table tr:nth-child({row_no}) td select').click()
            break


@then('Dropdown list contains value <value>')
def check_dropdown_contains(driver, value):
    assert driver.find_by_xpath(f'//select/option[text()="{value}"]').visible
