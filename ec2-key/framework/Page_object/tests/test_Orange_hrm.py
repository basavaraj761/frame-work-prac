import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from TEST_CASES.Base_class import TestBaseclass


class TestDemo(TestBaseclass):

    def test_login_orangehrm(self):
        
        self.d.implicitly_wait(10)
        self.d.find_element(by.NAME, "username").send_keys('Admin')
        self.d.find_element(by.NAME, "password").send_keys('admin123')
        self.d.find_element(by.XPATH, "//button[text()=' Login ']").click()
        print(self.d.title)
        self.d.find_element(by.CSS_SELECTOR, ".oxd-layout-context").is_displayed()
        assert True
