import time

from selenium import webdriver
from selenium.webdriver.common.by import By as by

chrome_opt=webdriver.ChromeOptions()
chrome_opt.add_argument("--headless")


d=webdriver.Chrome(chrome_opt)
d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.maximize_window()
d.implicitly_wait(10)
d.find_element(by.ID,"openwindow").click()
time.sleep(3)
curren_w=d.current_window_handle
print(curren_w)
windows=d.window_handles
print(windows)
for w in windows:
    if w!=curren_w:
        d.switch_to.window(w)
    tag1=[]
    tag=d.find_elements(by.TAG_NAME,"h2")
    for i in tag:
        tag1.append(i.text)
    print(tag1)
    d.switch_to.window(curren_w)
    d.find_element(by.ID,"name").send_keys('basava')
    t=d.find_element(by.CSS_SELECTOR,".blinkingText").text
    print(t)
