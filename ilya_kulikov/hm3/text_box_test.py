from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check
import time

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demoqa.com/')
chrome_driver.maximize_window()

# Кнопка вкладки
btn_elements = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"]'
                                                    '[position()=1]')
btn_elements.click()

# Кнопка "Text_Box"
btn_text = chrome_driver.find_element(By.XPATH, '(//*[@id="item-0"])[1]')
btn_text.click()

# Заполнение поля "Full Name"
field_full_name = chrome_driver.find_element(By.XPATH, '//*[@placeholder="Full Name"]')
field_full_name.send_keys('Ilya')

# Заполнение поля "Email"
field_email = chrome_driver.find_element(By.XPATH, "//*[@id='userEmail']")
field_email.send_keys('ilya123@mail.com')

# Заполнение поля "Current address"
field_current_address = chrome_driver.find_element(By.ID, "currentAddress")
field_current_address.send_keys('smth')

# Заполнение поля "Permanent address"
field_permanent_address = chrome_driver.find_element(By.ID,'permanentAddress')
field_permanent_address.send_keys('smth123')

# Проскролить к кнопке "Submit" + нажать на нее
chrome_driver.execute_script("window.scrollBy(0, 500);")
btn_submit = chrome_driver.find_element(By.XPATH, '//*[@id="submit"]')
res_submit = btn_submit.is_displayed()
if pytest_check.is_true(res_submit, 'element is not found'):
    btn_submit.click()


# находим элемент с выводом данных
output_element = chrome_driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")

# проверяем, что введенные данные соответствуют ожидаемому результату
EXPECTED_OUTPUT = "Name:Ilya\nEmail:ilya123@mail.com\n" \
                  "Current Address :smth\nPermananet Address :smth123"
# КТО ВМЕСТО Permanent написал в результате Prmananet !!!!!

# Проверка
assert output_element.text == EXPECTED_OUTPUT

time.sleep(5)
chrome_driver.quit()
