import allure
import pytest

from selenium import webdriver

import pytest

"""
link to get snippet to getsshot on failure used in this page:
https://github.com/pytest-dev/pytest/issues/230
"""


def pytest_addoption(parser):
    parser.addoption("--browser",default='chrome',action='store')


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(d.get_screenshot_as_png(), name='failed_test', attachment_type='AttachmentType.png')


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# //Usage and Invocations
@pytest.fixture(scope='class', autouse=True)
def setup(request):
    global d
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        d = webdriver.Chrome()
    elif browser == "ff":
        d = webdriver.Firefox()
    elif browser == "edge":
        d = webdriver.Edge()
    d.maximize_window()
    d.get("https://tutorialsninja.com/demo/")
    d.implicitly_wait(10)
    request.cls.d = d
    yield
    d.quit()
