"""this is using hooks  new for me
setup_module launch once before starting execution and after
def setup_module(function)
def tesrdown_module(function)
"""


def setup_function(function):
    print('open browser')


def teardown_function(function):
    print('open browser')


def test_one():
    print('executed test')


def test_two():
    print('executed test two')


def test_three():
    print('executed test three')


def test_four():
    print('executed test four')
