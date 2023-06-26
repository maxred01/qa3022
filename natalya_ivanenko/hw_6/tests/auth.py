import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

driver.maximize_window()
# Открытие страницы
driver.get("https://www.tesla.com/teslaaccount")

email = 'aosuvy@mailto.plus'
password = 'helloworld1'

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.ID, "form-input-identity")))

input = driver.find_element(By.ID, "form-input-identity")
input.send_keys(email)

time.sleep(3)

button = driver.find_element(By.ID, "form-submit-continue")
assert(button.is_displayed())
assert(button.is_enabled())
button.click()

time.sleep(10)


# Закрытие браузера
driver.quit()