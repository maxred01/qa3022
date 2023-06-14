import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

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

driver.execute_script("window.scrollBy(0, 500);")


# находим кнопку submit
submit_button = driver.find_element(By.ID, "submit")
# кликаем на кнопку submit
submit_button.click()

# ждем, пока страница перезагрузится
time.sleep(2)

# находим элемент с выводом данных
name = driver.find_element(By.ID, "name")
assert name.text == "Name:John Doe"
email = driver.find_element(By.ID, "email")
assert email.text == "Email:johndoe@example.com"
address = driver.find_element(By.CSS_SELECTOR, "p[id='currentAddress']")
assert address.text == "Current Address :123 Main St, Anytown, USA"
address = driver.find_element(By.CSS_SELECTOR, "p[id='permanentAddress']")
assert address.text == "Permananet Address :98765"


driver.get("https://demoqa.com/checkbox")

# ждем, пока страница полностью загрузится
time.sleep(2)

checkboxes = driver.find_elements(By.CSS_SELECTOR, "label")

for checkbox in checkboxes:
    checkbox.click()

# находим все чекбоксы на странице
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# проверяем каждый чекбокс
for checkbox in checkboxes:
    # если чекбокс не выбран, то кликаем на него
    assert checkbox.is_selected() is True
