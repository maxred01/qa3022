from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest_check as check

URL = "https://demoqa.com/"                        # Кладём линк в переменную URL

chrome_driver = webdriver.Chrome()                 # Инициализируем webdriver

chrome_driver.get(URL)

chrome_driver.maximize_window()
# Чек элемента elements
btn_elements = chrome_driver.find_element(By.XPATH, '//*[text()="Elements"]')

display_elements = btn_elements.is_displayed()

check.is_true(display_elements)

btn_elements.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента forms
btn_forms = chrome_driver.find_element(By.XPATH, '//*[text()="Forms"]')

display_forms = btn_elements.is_displayed()

check.is_true(display_forms)

btn_forms.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента alerts, frame and windows
btn_afw = chrome_driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3) div:nth-child(1) div:nth-child(1)')

display_afw = btn_afw.is_displayed()

check.is_true(display_afw)

btn_afw.click()

time.sleep(5)

chrome_driver.back()
# Чек элемента widgets
btn_widgets = chrome_driver.find_element(By.XPATH, '//*[text()="Widgets"]')

display_widgets = btn_widgets.is_displayed()

check.is_true(display_widgets)

btn_widgets.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента interactions
btn_interactions = chrome_driver.find_element(By.ID, '//*[text()="Interactions"]')

display_interactions = btn_interactions.is_displayed()

check.is_true(display_interactions)

btn_interactions.click()

time.sleep(5)

chrome_driver.back()
#Чек элемента book store application
btn_book = chrome_driver.find_element(By.ID, '//*[text()="Book Store Application"]')

display_book = btn_book.is_displayed()

check.is_true(display_book)

btn_book.click()

time.sleep(5)

chrome_driver.quit()

