import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

'''
Task2:
Java: Create two TestNg config files, the first one runs all “Smoke” test, the second runs “Regression”.
Run both of configs must be in parallel by methods mode and with 3 threads. 

In Python:
For parallel run: install plugin pytest-xdist
For tests grouping use pytest fixtures @pytest.mark.   

in the root dir create config file pytest.ini and add there the marks and the parameters for concurrent tests run 
pytest -s -v -m smoke lab2_2_and_2_3.py -n 4


Task3: Copy your HW1 test and refactor it in a such way that the test uses all annotations and instructions listed below.
Each annotation can contain the only 1 instruction.
Create a dedicated TestNG config for particular test. 

In Python:
@python.yield_fixture / @python.fixture  represents setup and tear down of the driver

'''


@pytest.yield_fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://epam.github.io/JDI/")
    yield driver
    driver.close()


class TestGroupTestsSmoke:

    @pytest.mark.smoke
    def test_page_title(self, driver):
        assert driver.title == "Home Page"

    @pytest.mark.smoke
    def test_4_displayed_img(self, driver):
        for image in driver.find_elements_by_tag_name("img"):
            assert image.is_displayed()

    @pytest.mark.smoke
    def test_find_a_frame(self, driver):
        assert driver.find_element_by_id("iframe").is_displayed()


class TestGroupTestsRegression:

    @pytest.mark.regression
    def test_page_title(self, driver):
        assert driver.title == "Home Page"

    @pytest.mark.regression
    def test_4_displayed_img(self, driver):
        for image in driver.find_elements_by_tag_name("img"):
            assert image.is_displayed()

    @pytest.mark.regression
    def test_find_a_frame(self, driver):
        assert driver.find_element_by_id("iframe").is_displayed()


class TestGroupTestsMixed:

    @pytest.mark.regression
    def test_page_title(self, driver):
        assert driver.title == "Home Page"

    @pytest.mark.regression
    def test_4_displayed_img(self, driver):
        for image in driver.find_elements_by_tag_name("img"):
            assert image.is_displayed()

    @pytest.mark.smoke
    def test_find_a_frame(self, driver):
        assert driver.find_element_by_id("iframe").is_displayed()


class TestGroupTestsBoth:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_page_title(self, driver):
        assert driver.title == "Home Page"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_4_displayed_img(self, driver):
        for image in driver.find_elements_by_tag_name("img"):
            assert image.is_displayed()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_find_a_frame(self, driver):
        assert driver.find_element_by_id("iframe").is_displayed()
