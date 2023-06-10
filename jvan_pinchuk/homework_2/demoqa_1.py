import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check


chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demoqa.com/')
chrome_driver.maximize_window()

# Elements
btn_elements = chrome_driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")
a = btn_elements.is_displayed()
print(a)
check.is_true(a)
btn_elements.click()
btn_main = chrome_driver.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
btn_main.click()

time.sleep(5)
# Forms
btn_forms = chrome_driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[2]")

b = btn_forms.is_displayed()
print(b)
check.is_true(b)
btn_forms.click()
btn_main = chrome_driver.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
btn_main.click()


# Alerts
btn_alerts = chrome_driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[3]")
c = btn_alerts.is_displayed()
print(c)
check.is_true(c)
btn_alerts.click()
btn_main = chrome_driver.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
btn_main.click()


# Widgets
btn_widgets = chrome_driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[4]")
d = btn_widgets.is_displayed()
print(d)
check.is_true(d)
btn_widgets.click()
btn_main = chrome_driver.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
btn_main.click()

# Interactions
btn_interactions = chrome_driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[5]")
e = btn_interactions.is_displayed()
print(e)
check.is_true(e)
btn_interactions.click()
btn_main = chrome_driver.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
btn_main.click()

# Book store
chrome_driver.execute_script("window.scrollBy(0, 500);")
btn_bookstore = chrome_driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[6]")
g = btn_bookstore.is_displayed()
print(g)
check.is_true(g)
btn_bookstore.click()
time.sleep(5)
chrome_driver.quit()

