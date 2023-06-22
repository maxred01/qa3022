import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://demoqa.com/'

chrome_driver = webdriver.Chrome()

chrome_driver.get(URL)

chrome_driver.maximize_window()

btn_elmnts = chrome_driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"])[1]')

btn_elmnts.click()

btn_text = chrome_driver.find_element(By.XPATH, '(//*[@id="item-0"])[1]')

btn_text.click()

full_name = chrome_driver.find_element(By.XPATH, '//input[@id="userName"]')

full_name.send_keys('Aleksey Titov')

email = chrome_driver.find_element(By.XPATH, '//input[@id="userEmail"]')

email.send_keys('test@gmail.com')

current_address = chrome_driver.find_element(By.XPATH, '//*[@id="currentAddress"]')

current_address.send_keys('Yakubova st')

permananet_address = chrome_driver.find_element(By.XPATH,'//*[@id="permanentAddress"]')

permananet_address.send_keys('220101')

chrome_driver.execute_script("window.scrollBy(0, 500);")

btn_submit = chrome_driver.find_element(By.XPATH, '//button[@id="submit"]')

btn_submit.click()

time.sleep(3)

output_elmnt = chrome_driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")
#Пишу permananet в ожидаемом так как на сайте в форме именно так
EXPECTED_OUTPUT = "Name:Aleksey Titov\nEmail:test@gmail.com\n" \
                  "Current Address :Yakubova st\nPermananet Address :220101"

assert output_elmnt.text == EXPECTED_OUTPUT

time.sleep(3)

chrome_driver.quit()
