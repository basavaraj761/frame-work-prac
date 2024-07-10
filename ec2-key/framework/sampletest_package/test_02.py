import pytest


@pytest.mark.parametrize('username, pwd',[("basava","12345"), ("shiva","098765")])
def test_sample_2_1(username, pwd):
    print(username + " " + pwd)


@pytest.mark.smoke
def test_sample_2_2():
    print("rumming sample from 2")


def test_sample_2_3():
    print("rumming sample from 2")
