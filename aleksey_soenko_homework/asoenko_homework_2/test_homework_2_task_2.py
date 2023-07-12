import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

URL = "https://demoqa.com/"

chrome_driver = webdriver.Chrome()

chrome_driver.get(URL)

chrome_driver.maximize_window()
# Чек элемента elements
btn_elmnts = chrome_driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"])[1]')

display_elmnts = btn_elmnts.is_displayed()

check.is_true(display_elmnts)

btn_elmnts.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента forms
btn_forms = chrome_driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"])[2]')

display_forms = btn_forms.is_displayed()

check.is_true(display_forms)

btn_forms.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента alerts, frame and windows
btn_afw = chrome_driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"])[3]')

display_afw = btn_afw.is_displayed()

check.is_true(display_afw)

btn_afw.click()

time.sleep(5)

chrome_driver.back()
# Чек элемента widgets
btn_widgets = chrome_driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"])[4]')

display_widgets = btn_widgets.is_displayed()

check.is_true(display_widgets)

btn_widgets.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента interactions
btn_interactions = chrome_driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"])[5]')

display_interactions = btn_interactions.is_displayed()

check.is_true(display_interactions)

btn_interactions.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента book store application
btn_book = chrome_driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"])[6]')

display_book = btn_book.is_displayed()

check.is_true(display_book)

btn_book.click()

time.sleep(5)

chrome_driver.quit()
