import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://demoqa.com")
chrome_driver.maximize_window()

card = chrome_driver.find_element(By.CSS_SELECTOR, '.category-cards>:nth-child(1)')
card.click()

panel = chrome_driver.find_element(By.CSS_SELECTOR, '.left-pannel')
panel.is_displayed()

time.sleep(3)

# button = chrome_driver.find_element(By.CSS_SELECTOR, '.left-pannel .element-group:nth-child(1)')
# button.is_displayed()
# button.click()

chrome_driver.execute_script("window.scrollBy(0, 500);")
button = chrome_driver.find_element(By.CSS_SELECTOR, '.left-pannel .element-group:nth-child(2)')
button.is_displayed()
button.click()

time.sleep(1)

chrome_driver.execute_script("window.scrollBy(0, 500);")
button = chrome_driver.find_element(By.CSS_SELECTOR, '.left-pannel .element-group:nth-child(3)')
button.is_displayed()
button.click()

time.sleep(1)

chrome_driver.execute_script("window.scrollBy(0, 500);")
button = chrome_driver.find_element(By.CSS_SELECTOR, '.left-pannel .element-group:nth-child(4)')
button.is_displayed()
button.click()

time.sleep(1)

chrome_driver.execute_script("window.scrollBy(0, 500);")
button = chrome_driver.find_element(By.CSS_SELECTOR, '.left-pannel .element-group:nth-child(5)')
button.is_displayed()
button.click()

time.sleep(1)

chrome_driver.execute_script("window.scrollBy(0, 500);")
button = chrome_driver.find_element(By.CSS_SELECTOR, '.left-pannel .element-group:nth-child(6)')
button.is_displayed()
button.click()

