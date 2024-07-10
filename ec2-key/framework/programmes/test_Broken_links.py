import requests
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from seleniumwire.undetected_chromedriver import ChromeOptions


def test_broken():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    # url = "https://ybraniumelectric.com/"

    d = webdriver.Chrome(chrome_options)
    d.get("https://ybraniumelectric.com/")

    links = d.find_elements(by.TAG_NAME, "a")
    print(len(links))

    for link in links:
        l = link.get_attribute('href')
        print(l)
        if l == None or len(l) < 10:
            continue
        res = requests.get(url=l)

        if res.status_code >= 400:
            print(l, res.status_code)
