from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\code\isaacbot\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://platinumgod.co.uk/repentance")

outfile = open('data.txt','w')
print(driver.title)

try:
#	div = driver.find_element_by_class_name('repentanceitems-container')
	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[2]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))
	
	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[3]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))
	
	div = driver.find_element_by_xpath('//*[@id="itmlist"]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))
	
	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[5]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))

	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[6]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))
	
	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[7]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))
	
	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[8]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))

	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[9]')
	for item in div.find_elements_by_class_name("textbox"):
#		print(item.get_attribute("textContent"))
		outfile.write(item.get_attribute("textContent"))
	
	div = driver.find_element_by_xpath('//*[@id="ht"]/body/div[2]/div[10]')
	for item in div.find_elements_by_class_name("textbox"):
#	PRINTING TO CONSOLE SINCE IT WON'T WRITE TO FILE	
		print(item.get_attribute("textContent"))

except Exception as e:
    print(f"Failed for '{e}'")

finally:
    driver.quit()

print('Done')