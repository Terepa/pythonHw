from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import string
import random

driver = webdriver.Chrome("C:\\Users\\terepdmi\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://juniortestdmitrijsterepa.000webhostapp.com/"
driver.get(url)
time.sleep(2)
#

add_btn = driver.find_element_by_link_text("ADD")
print(add_btn.get_attribute("href"))
add_btn.click()
#
input_sku = driver.find_element_by_id("sku")
randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
input_sku.send_keys(randstring)
time.sleep(2)

input_name = driver.find_element_by_id("name")
input_name.send_keys("Project")

input_price = driver.find_element_by_id("price")
input_price.send_keys("777")
time.sleep(2)

typeSwitcher = driver.find_element_by_id("productType")
product_type = Select(typeSwitcher)
product_type.select_by_value("Furniture")
time.sleep(2)

input_height = driver.find_element_by_id("height")
input_height.send_keys("1")

input_width = driver.find_element_by_id("width")
input_width.send_keys("2")

input_length = driver.find_element_by_id("length")
input_length.send_keys("3")
time.sleep(2)
#
add_btn = driver.find_element_by_id("saveButton")
add_btn.click()
time.sleep(2)
#
checkbox = driver.find_elements_by_id("delete-checkbox")
print(len(checkbox))
new_checkbox = checkbox[0]
new_checkbox.click()
time.sleep(2)
#
add_btn = driver.find_element_by_id("delete-product-btn")
add_btn.click()
time.sleep(2)
