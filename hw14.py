from selenium import webdriver
import time  # we might need to insert some delay in the code
from selenium.webdriver.chrome.service import Service
import requests
import json

driver = webdriver.Chrome("C:\\Users\\terepdmi\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://www.ss.com/"
driver.get(url)  # this will open the url in browser
time.sleep(2)  # this will wait for 2 seconds

#

vieglie_auto = driver.find_element_by_id("mtd_97")
print(vieglie_auto.get_attribute("href"))

time.sleep(0.5)
#
vieglie_auto.click()

elektro = driver.find_element_by_id("ahc_290868")
print(elektro.get_attribute("href"))
time.sleep(0.5)
elektro.click()
#
car_list = driver.find_elements_by_class_name("d1")
car = list()
for i in range(len(car_list)):
    car.append(car_list[i].text)

with open("elektro.json", mode="w", encoding="utf-8") as write_file:  # saving data to json
    json.dump(car, write_file, indent=4, ensure_ascii=False)

