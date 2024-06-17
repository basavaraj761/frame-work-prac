import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Demo:
    def test_login(self):
        # d = webdriver.Edge()
        #
        # d.maximize_window()
        # d.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        # d.implicitly_wait(4)
        # print(d.current_url)
        # print(d.title)
        self.d.find_element(By.NAME, "username").send_keys('Admin')
        self.d.find_element(By.NAME, "password").send_keys('admin123')
        self.d.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # if self.d.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed():
        #     pass


d = Demo()
d.test_login()
