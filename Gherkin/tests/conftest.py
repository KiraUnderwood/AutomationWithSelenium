import pytest
import datetime
import allure

from splinter import Browser
from pytest_bdd import scenario, given, when, then, scenarios, parsers

from .MainPage import MainPage
from .AnyPageAbstracts import Base
from .DifferentElementsPage import DifferentElements


@pytest.fixture(scope="session")
def driver(request):
    with Browser(driver_name="chrome") as b:
        b.driver.maximize_window()
        yield b


given('a Chrome browser is open', fixture='driver')


@pytest.fixture(scope="session")
def home_page(driver):
    home_page = MainPage(driver)
    home_page.open()
    yield home_page


given('I am on the Home Page', fixture='home_page')


@pytest.fixture(scope="session")
def elements_page(home_page, driver):
    home_page.header.go_to_different_elements_page()
    yield DifferentElements(driver, driver.url)


given('I went to Different Elements page', fixture='elements_page')


@when(parsers.parse('I login with {user} and {pwd}'))
def login(home_page, user, pwd):
    home_page.header.login(user, pwd)


@then(parsers.parse('I should see user-icon with {expected_user} reflected'))
def check_user(home_page, expected_user):
    home_page.header.check_current_user(expected_user)


