import pytest


def get_data():
    return [
        ['me', 'basava'],
        ['me1', 'shiva'],
        ['me2', 'shankara']

    ]


@pytest.mark.parametrize("username,password", get_data())
def test_login(username, password):
    print('username is :'+username, 'password is: ' + password)
