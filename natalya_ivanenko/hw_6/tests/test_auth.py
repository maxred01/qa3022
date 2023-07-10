import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw_6.pages.locators import auth_locators

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

driver.maximize_window()
# Открытие страницы
driver.get("https://www.tesla.com/teslaaccount")

shop_locators.header_logo

email = 'aosuvy@mailto.plus'
password = 'helloworld1'

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located(auth_locators.identity))

input = driver.find_element(auth_locators.identity)
input.send_keys(email)

time.sleep(3)

button = driver.find_element(auth_locators.form_submit_continue)
assert(button.is_displayed())
assert(button.is_enabled())
button.click()

time.sleep(10)


# Закрытие браузера
driver.quit()