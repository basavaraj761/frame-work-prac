import pytest
from seleniumwire import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome",action="store")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        d = webdriver.Chrome()
    elif browser == "ff":
        d = webdriver.Firefox()
    elif browser == "edge":
        d = webdriver.Edge()
        d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    request.cls.d = d
    yield
    d.close()
