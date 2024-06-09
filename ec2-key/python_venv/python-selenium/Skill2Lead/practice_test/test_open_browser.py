import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.select import Select


def test_rahul():
    from selenium import webdriver

    d=webdriver.Chrome()



    d.get("https://rahulshettyacademy.com/AutomationPractice/")
    title=d.title
    print(title)
    d.maximize_window()
    d.implicitly_wait(8)
    # working on radio button
    radio = []
    radio_button = d.find_elements(by.XPATH, "//input[@type='radio']")
    d.find_element(by.XPATH, "//input[@value='radio2']").click()
    d.get_screenshot_as_file('screenshots\\radio.png')
    for i in radio_button:
        t = (i.get_attribute('value'))
        radio.append(t)
    # autocomplete textbox
    d.find_element(by.CSS_SELECTOR, '#autocomplete').send_keys('ind')
    list_1 = d.find_elements(by.XPATH, "//li[@class='ui-menu-item']")
    auto_sug = []
    for i in list_1:
        auto_sug.append(i.text)
    # print(auto_sug)
    d.find_element(by.XPATH, "//li[@class='ui-menu-item'][1]")
    d.get_screenshot_as_file('screenshots\\autosugg.png')
    # dropdown
    dropdown = []
    ele = d.find_element(by.CSS_SELECTOR, "#dropdown-class-example")
    select = Select(ele)
    select.select_by_index(1)
    d.get_screenshot_as_file('screenshots\\dropdown.png')

    # Alert
    d.find_element(by.CSS_SELECTOR, "#name").send_keys("basava")
    d.find_element(by.CSS_SELECTOR, "#alertbtn").click()
    alert=d.switch_to.alert
    time.sleep(1)
    print(alert.text)
    alert.accept()
    # switch window example


