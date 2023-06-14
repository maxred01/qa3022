'''Input data in the fields with command send_keys'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#open site
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://demoqa.com/elements")
chrome_driver.maximize_window()

#click button text_box
btn_text_box = chrome_driver.find_element(By.XPATH, '//span[contains(text(),"Text Box")]')
btn_text_box.is_displayed()
btn_text_box.click()
time.sleep(2)

#input data in the field username
input_user_name = chrome_driver.find_element(By.ID, 'userName')
input_user_name.send_keys('sergey')

#input data in the field email
input_user_email = chrome_driver.find_element(By.ID, 'userEmail')
input_user_email.send_keys('test@gmail.com')

#input data in the field permanent_address
input_current_address = chrome_driver.find_element(By.ID, 'currentAddress')
input_current_address.send_keys('belarus')

#input data in the field permanent_address
input_permanent_adress = chrome_driver.find_element(By.ID, 'permanentAddress')
input_permanent_adress.send_keys('minsk')

#wait and click button submit
time.sleep(2)
btn_submit = chrome_driver.find_element(By.ID, 'submit')
btn_submit.is_displayed()
btn_submit.click()

#find element with output data
output_element = chrome_driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")

#our input data
OUTPUT_DATA = 'Name:sergey\nEmail:test@gmail.com\nCurrent ' \
              'Address :belarus\nPermananet Address :minsk'
assert output_element.text == OUTPUT_DATA

#wait and close chrome
time.sleep(2)
chrome_driver.quit()
