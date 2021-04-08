from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

PATH = "C:\code\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://platinumgod.co.uk/repentance")
print(driver.title)

#container = driver.find_element(By.CSS_SELECTOR, 'div')
#title = driver.find_element(By.CSS_SELECTOR, 'h2')
#item = driver.find_element(By.CSS_SELECTOR("body > div.main > div:nth-child(3) > li:nth-child(2) > a > span")).text

items_list = []

main = driver.find_element_by_css_selector(".p").text
#//*[@id="ht"]/body/div[2]/div[2]/li[1]/a/span


print(main)

driver.close()
print('Done')