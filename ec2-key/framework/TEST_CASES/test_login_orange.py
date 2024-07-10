import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire.undetected_chromedriver import ChromeOptions

from TEST_CASES.Base_class import Baseclass


@pytest.mark.usefixtures("setup")
class TestDemo(Baseclass):
    def test_login(self):

        self.d.find_element(By.NAME, "username").send_keys('Admin')
        log=self.test_getlog()
        log.info("entered un")
        self.d.find_element(By.NAME, "password").send_keys('admin123')
        log.info("entered pwd")
        self.d.find_element(By.CSS_SELECTOR, "button[type='submit']").click()





