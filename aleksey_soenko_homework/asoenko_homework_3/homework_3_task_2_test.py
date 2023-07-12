import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demoqa.com/checkbox"

chrome_driver = webdriver.Chrome()

chrome_driver.get(URL)

chrome_driver.maximize_window()

time.sleep(2)

checkboxes = chrome_driver.find_elements(By.XPATH, '//*[@class="rct-checkbox"]')

btn_open = chrome_driver.find_element(By.XPATH, '//*[@title="Expand all"]')

btn_open.click()

time.sleep(3)

chrome_driver.execute_script("window.scrollBy(0, 300);")

for checkbox in checkboxes:
    checkbox.click()
    print(checkbox.is_selected())

time.sleep(3)

chrome_driver.quit()
