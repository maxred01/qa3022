import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

crome_driver = webdriver.Chrome()
URL = "https://demoqa.com/"
crome_driver.get(URL)
crome_driver.set_window_size(2000,1000)

button_elements = crome_driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div/div[1]")
button_elements.is_displayed()
if check.is_true(button_elements):
    button_elements.click()
    time.sleep(4)
else:
    pass
crome_driver.get(URL)
button_elements = crome_driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div/div[2]")
button_elements.is_displayed()
if check.is_true(button_elements):
    button_elements.click()
    time.sleep(4)
else:
    pass
crome_driver.get(URL)
button_elements = crome_driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div/div[3]")
button_elements.is_displayed()
if check.is_true(button_elements):
    button_elements.click()
    time.sleep(4)
else:
    pass
crome_driver.get(URL)
button_elements = crome_driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div/div[4]")
button_elements.is_displayed()
if check.is_true(button_elements):
    button_elements.click()
    time.sleep(4)
else:
    pass
crome_driver.get(URL)
button_elements = crome_driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div/div[5]")
button_elements.is_displayed()
if check.is_true(button_elements):
    button_elements.click()
    time.sleep(4)
else:
    pass

crome_driver.get(URL)
crome_driver.execute_script("window.scrollTo(0,500)")
time.sleep(4)
button_elements = crome_driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div/div[6]")
button_elements.is_displayed()
if check.is_true(button_elements):
    button_elements.click()
    time.sleep(4)
    crome_driver.execute_script("window.scrollTo(0,500)")
    time.sleep(4)
else:
    pass
