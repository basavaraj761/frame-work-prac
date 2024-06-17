import pytest


@pytest.mark.smoke
def test_01():
    a = 7
    b = 7
    assert a is b


@pytest.mark.smoke
def test_02():
    q = 6
    t = 9
    assert t > q


@pytest.mark.skip
def test_03():
    a = 'basava'
    b = 'patil123'
    assert a != b


def test_demo():
    print("running demo code")
