from selenium import webdriver


def test_tutorial_ninja():
    d=webdriver.Chrome()
    d.maximize_window()
    d.get('https://www.qafox.com/mobile-testing-tutorial-complete-guide/')
    expected_title="Mobile Testing Tutorial - A Complete, Detailed & Easy "
    title=d.title
    # assert title.__eq__(expected_title)
    d.quit()