import pytest
import allure

from splinter import Browser
from .MainPage import MainPage

'''
def pytest_exception_interact(node, call, report):
    driver = node.instance.driver.driver
    # ...
    allure.attach(
        name='Скриншот',
        contents=driver.get_screenshot_as_png(),
        type=allure.attachment_type.PNG,
    )

'''


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='function', autouse=True)
def test_debug_log(request, driver):
    def test_result():
        if request.node.rep_call.failed:
            # Make the screen-shot if test failed:
            try:
                allure.attach(
                    driver.driver.get_screenshot_as_png(),
                    name=request.function.__name__,
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                pass

    request.addfinalizer(test_result)
