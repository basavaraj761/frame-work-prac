import pytest


@pytest.fixture(scope='function',autouse=True)
def setup():
    print('open browser')
    yield
    print('close browser')