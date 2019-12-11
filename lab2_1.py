import unittest
import time
import pytest
import xdist.plugin

from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://epam.github.io/JDI/")
    yield driver
    driver.close()

@pytest.fixture(scope="function", params=[0, 1, 2, 3])
def idx_number(request):
    return request.param

class TestEpamPageTestSuite:
    '''
    def test_texts_below_icon_elements(self, driver, idx_number):
        expected = ['To include good practices\nand ideas from successful\nEPAM project',
                    'To be flexible and\ncustomizable', 'To be multiplatform',
                    'Already have good base\n(about 20 internal and\nsome external projects),\nwish to get more…']
        get_text = driver.find_elements_by_css_selector(".col-sm-3 .benefit-txt")[idx_number]
        print(get_text.text)
        assert get_text.text in expected
        '''

    @pytest.mark.parametrize("idx", [0, 1, 2, 3])

    def test_texts_below_icon_elements(self, driver, idx):
        expected = ['To include good practices\nand ideas from successful\nEPAM project',
                    'To be flexible and\ncustomizable', 'To be multiplatform',
                    'Already have good base\n(about 20 internal and\nsome external projects),\nwish to get more…']

        get_text = driver.find_elements_by_css_selector(".col-sm-3 .benefit-txt")[idx]
        print(get_text.text)
        assert get_text.text in expected

