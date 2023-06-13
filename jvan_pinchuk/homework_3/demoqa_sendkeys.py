import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demoqa.com/')
chrome_driver.maximize_window()

btn_elements = chrome_driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")
res_elements = btn_elements.is_displayed()
check.is_true(res_elements)
btn_elements.click()

btn_text_box = chrome_driver.find_element(By.XPATH, "(//li[@id='item-0'])[1]")
res_elements = btn_text_box.is_displayed()
check.is_true(res_elements)
btn_text_box.click()
time.sleep(5)

field_name = chrome_driver.find_element(By.CSS_SELECTOR, "#userName")
field_name.send_keys("Jvan Pinchuk")

field_email = chrome_driver.find_element(By.CSS_SELECTOR, "#userEmail")
field_email.send_keys("j.v.a.n.pinchuk@gmail.com")

field_adress = chrome_driver.find_element(By.CSS_SELECTOR, "#currentAddress")
field_adress.send_keys("c. Minsk, st. K.Marks, 22-11")

field_per_adress = chrome_driver.find_element(By.CSS_SELECTOR, "#permanentAddress")
field_per_adress.send_keys("c. Minsk, st. K.Marks, 22-11")

btn_submit = chrome_driver.find_element(By.CSS_SELECTOR, "#submit")
res_sub = btn_submit.is_displayed()
check.is_true(res_sub)
btn_submit.click()
time.sleep(5)

# находим элемент с выводом данных
output_element = chrome_driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")

# проверяем, что введенные данные соответствуют ожидаемому результату

EXPECTED_OUTPUT = "Name:Jvan Pinchuk\nEmail:j.v.a.n.pinchuk@gmail.com\n" \
                  "Current Address :c. Minsk, st. K.Marks, 22-11\n" \
                  "Permananet Address :c. Minsk, st. K.Marks, 22-11"
assert output_element.text == EXPECTED_OUTPUT, 'Not the same text'
if output_element.text == EXPECTED_OUTPUT:
    print("the same text")

btn_check = chrome_driver.find_element(By.XPATH, "(//li[@id='item-1'])[1]")
btn_check.click()

dropdown_list_home = chrome_driver.find_element\
    (By.XPATH, "//button[@title='Toggle']//*[name()='svg']")
dropdown_list_home.click()

dropdown_list_desk = chrome_driver.find_element(By.XPATH, "(//button[@title='Toggle'])[2]")
dropdown_list_desk.click()
dropdown_list_doc = chrome_driver.find_element(By.XPATH, "(//button[@title='Toggle'])[3]")
dropdown_list_doc.click()
dropdown_list_down = chrome_driver.find_element(By.XPATH, "(//button[@title='Toggle'])[4]")
dropdown_list_down.click()

# находим все чекбоксы на странице
checkboxes = chrome_driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# проверяем каждый чекбокс
NUM = 1
for checkbox in checkboxes:
    chrome_driver.find_element(By.XPATH, f"(// span[@class ='rct-checkbox'])[{NUM}]").click()
    print("is-selected : ", checkbox.is_selected())
    print()
    NUM += 1

time.sleep(5)
# Close the driver
chrome_driver.quit()
