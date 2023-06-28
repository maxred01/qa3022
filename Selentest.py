import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://demoqa.com/radio-button")
time.sleep(5)

radios_yes = chrome_driver.find_element(By.CSS_SELECTOR,'label[for="yesRadio"]')
radios_yes.click()
time.sleep(2)

radios_add = chrome_driver.find_element(By.ID, "addNewRecordButton")
radios_add.click()
time.sleep(2)



a = chrome_driver.find_element(By.CSS_SELECTOR,'input[id="yesRadio"]')
assert a == True

chrome_driver.quit()
