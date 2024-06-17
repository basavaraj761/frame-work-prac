import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    d = webdriver.Edge()
    d.maximize_window()
    d.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    d.implicitly_wait(4)
    print(d.current_url)
    print(d.title)
    request.cls.d = d
    yield
    d.close()
