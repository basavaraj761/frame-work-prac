import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pynput.keyboard import Key, Controller
from soft_assert import soft_assert


def test_upload():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--log-level=1")

    d = webdriver.Chrome(opt)
    d.maximize_window()
    d.get("https://www.naukri.com/")
    d.implicitly_wait(10)
    d.find_element(by.CSS_SELECTOR, "#login_Layer").click()
    d.find_element(by.XPATH,
                   "//input[@placeholder='Enter your active Email ID / Username' and @type='text']").send_keys(
        "basavaraj761@gmail.com")
    d.find_element(by.XPATH, "//input[@placeholder='Enter your password']").send_keys("Aa@1234567")
    d.find_element(by.CSS_SELECTOR, ".btn-primary.loginButton").click()
    time.sleep(4)
    d.find_element(by.CSS_SELECTOR, ".nI-gNb-drawer__bars").click()
    time.sleep(5)
    d.find_element(by.CSS_SELECTOR, ".nI-gNb-info__sub-link").click()
    d.find_element(by.CSS_SELECTOR, ".uploadBtn").click()
    try:
        ele = d.find_element(by.XPATH, "//span[@class='icon-wrap' and @data-title='delete-resume']")
        ele.is_displayed()
        ele.click()
        time.sleep(2)
        wait = WebDriverWait(d, timeout=5)
        ele1 = d.find_element(by.XPATH, "//div[@class='lightbox model_open flipOpen']/child::div//button")
        wait.until(ec.visibility_of(ele1))
        ele1.click()
        time.sleep(5)
    except Exception as e:
        pass

    finally:
        a = ActionChains(driver=d)
        ele2 = d.find_element(by.XPATH, "//span[text()='Upload resume']")
        a.move_to_element(ele2)
        ele2.click()
        time.sleep(3)
        Keyboard = Controller()
        Keyboard.type(r"C:\Users\basav\Downloads\NAUKRI_BASAVARAJ_M_PATIL.pdf")
        time.sleep(3)
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)
        time.sleep(5)
        ele1 = d.find_element(by.CSS_SELECTOR, "#attachCVMsgBox")
        t = ele1.text
        print(t)
        etext = """GreenTick
Success
Resume has been successfully uploaded."""
        assert etext.__eq__(ele1.text)
        print('printing last line')
        d.quit()
