from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
d=webdriver.Chrome(options=chrome_options)
d.get("https://toolsqa.com/selenium-webdriver/selenium-headless-browser-testing/")
print()
print(d.title)
