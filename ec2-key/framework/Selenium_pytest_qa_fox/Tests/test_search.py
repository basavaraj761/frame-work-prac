import allure
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup', "log_on_failure")
class TestDemo:
    @allure.severity(allure.severity_level.MINOR)
    def test_search_valid_product(self):
        self.d.find_element(By.NAME, 'search').send_keys("HP")
        self.d.find_element(By.CSS_SELECTOR, ".btn-default").click()
        allure.attach(self.d.get_screenshot_as_png(), name='test_search_valid_product', attachment_type='AttachmentType'
                                                                                                        '.png')
        assert self.d.find_element(By.XPATH, "//a[text()='HP LP3065']").is_displayed()
        # d.quit()

    @allure.severity(allure.severity_level.NORMAL)
    def test_search_invalid_product(self):
        # d = webdriver.Chrome()
        # d.maximize_window()
        # d.get("https://tutorialsninja.com/demo/")
        # d.implicitly_wait(10)
        self.d.find_element(By.NAME, 'search').send_keys("Honda")

        self.d.find_element(By.CSS_SELECTOR, ".btn-default").click()
        text = self.d.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        expec_title = "There is no product that matches the search criteria."
        assert text.__eq__(expec_title)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_empty_product(self):
        self.d.find_element(By.NAME, 'search').send_keys("Honda")
        self.d.find_element(By.CSS_SELECTOR, ".btn-default").click()
        allure.attach(self.d.get_screenshot_as_png(), name='test_search_empty_product', attachment_type='AttachmentType'
                                                                                                        '.png')

        text = self.d.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        expec_title = "There is no product that matches the search criteria."
        assert text.__eq__(expec_title)


