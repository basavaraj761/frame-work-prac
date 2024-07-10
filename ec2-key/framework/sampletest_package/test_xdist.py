from selenium import webdriver


def test_orange():
    d = webdriver.Chrome()
    d.maximize_window()
    d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    title = d.title
    print(title)
    d.close()


def test_jquery():
    d = webdriver.Chrome()
    d.maximize_window()
    d.get("https://jquery.com/")
    title = d.title
    print(title)
    d.close()


def test_qa_fox():
    d = webdriver.Chrome()
    d.maximize_window()
    d.get("https://www.qafox.com/")
    title = d.title
    print(title)
    d.close()


def test_mobile_guide():
    d = webdriver.Chrome()
    d.maximize_window()
    d.get("https://www.qafox.com/mobile-testing-tutorial-complete-guide/")
    title = d.title
    print(title)
    d.close()
