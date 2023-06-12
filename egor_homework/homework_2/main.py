import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import pytest_check as check

chrome_driver = webdriver.Chrome()
main_url = "https://demoqa.com"
chrome_driver.maximize_window()
chrome_driver.get(main_url)

# perform check the Element button
button_element = chrome_driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card'][1]")
displayed_element = button_element.is_displayed()
check.is_true(displayed_element, 'Not display')
button_element.click()
time.sleep(3)
chrome_driver.back()

# perform check the Forms button
button_forms = chrome_driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card'][2]")
displayed_forms = button_forms.is_displayed()
check.is_true(displayed_forms, 'Not display')
button_forms.click()
time.sleep(3)
chrome_driver.back()

# perform check the Alerts, Frame & Windows button
button_alerts = chrome_driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card'][3]")
displayed_alerts = button_alerts.is_displayed()
check.is_true(displayed_alerts, 'Not display')
button_alerts.click()
time.sleep(3)
chrome_driver.back()

# perform check the Widgets
button_widgets = chrome_driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card'][4]")
displayed_widgets = button_widgets.is_displayed()
check.is_true(displayed_widgets, 'Not display')
button_widgets.click()
time.sleep(3)
chrome_driver.back()

# perform check the Interactions
button_interactions = chrome_driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card'][5]")
displayed_interactions = button_interactions.is_displayed()
check.is_true(displayed_interactions, 'Not display')
button_interactions.click()
time.sleep(3)
chrome_driver.back()

chrome_driver.execute_script("window.scrollBy(0, 500);")
# perform check the Book Store Application
button_book = chrome_driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card'][6]")
button_book.click()
time.sleep(3)

chrome_driver.quit()
