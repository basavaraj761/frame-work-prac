from selenium import webdriver

chrome_opt=webdriver.ChromeOptions()
chrome_opt.add_argument("--headless")

d=webdriver.Chrome(chrome_opt)
d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.maximize_window()
title=d.title
print("extracted title is",title)