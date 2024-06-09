import time

from selenium import webdriver


chro_opt = webdriver.ChromeOptions()
chro_opt.add_argument("--headless")

d = webdriver.Chrome(chro_opt)
d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.execute_script('window.open("https://www.geeksforgeeks.org/how-to-handle-alert-prompts-in-selenium-python/")')
time.sleep(7)



