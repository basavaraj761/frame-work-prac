import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By as by

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--headless")

d = webdriver.Chrome(chrome_opt)
d.maximize_window()
d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.implicitly_wait(4)

action = ActionChains(d)
ele=d.find_element(by.ID,"mousehover")
action.move_to_element(ele).perform()
time.sleep(3)
d.find_element(by.XPATH,"//div[@class='mouse-hover-content']//a[1]").click()
