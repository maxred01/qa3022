import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# создаем экземпляр драйвера для Chrome
driver = webdriver.Chrome()

# переходим на страницу https://demoqa.com/text-box
driver.get("https://demoqa.com/text-box")

# ждем, пока страница полностью загрузится
time.sleep(2)

# находим поле ввода имени
name_input = driver.find_element(By.ID, "userName")
# заполняем поле ввода имени
name_input.send_keys("John Doe")

# находим поле ввода email
email_input = driver.find_element(By.ID, "userEmail")
# заполняем поле ввода email
email_input.send_keys("johndoe@example.com")

# находим поле ввода адреса
address_input = driver.find_element(By.ID, "currentAddress")
# заполняем поле ввода адреса
address_input.send_keys("123 Main St, Anytown, USA")

# находим поле ввода почтового индекса
postal_input = driver.find_element(By.ID, "permanentAddress")
# заполняем поле ввода почтового индекса
postal_input.send_keys("98765")

# находим кнопку submit
submit_button = driver.find_element(By.ID, "submit")
# кликаем на кнопку submit
submit_button.click()

# ждем, пока страница перезагрузится
time.sleep(2)

# находим элемент с выводом данных
output_element = driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']/p")

# проверяем, что введенные данные соответствуют ожидаемому результату
EXPECTED_OUTPUT = "Name:John Doe\nEmail:johndoe@example.com\n" \
                  "Current Address :123 Main St, Anytown, USA\nPermanent Address :98765"
assert output_element.text == EXPECTED_OUTPUT

driver.quit()
