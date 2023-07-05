import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from natalya_ivanenko.hw_6.tests.locators import demo_locators

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

driver.maximize_window()
# Открытие страницы
driver.get("https://www.tesla.com/drive")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "models")))

models = driver.find_elements(By.CLASS_NAME, 'models')
for item in models:
    ActionChains(driver).move_to_element(item).perform()
    assert(item.is_displayed())
    assert(item.is_enabled())

models[0].click()
assert(models[0])

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

input = driver.find_element(By.ID, "edit-firstname-td")
input.send_keys("Natalja")

input = driver.find_element(By.ID, "edit-lastname-td")
input.send_keys("Ivanenko")

input = driver.find_element(By.ID, "edit-phonenumber-td")
input.send_keys("2015550123")

input = driver.find_element(By.ID, "edit-usermail-td")
input.send_keys("hello@mail.ru")

input = driver.find_element(By.ID, "edit-zipcode-td")
input.send_keys("78585")

driver.execute_script("window.scrollBy(0, 500);")

time.sleep(1)

terms = driver.find_element(By.CLASS_NAME, "tds-form-input-choice-label")
#ActionChains(driver).move_to_element(terms).perform()
terms.click()

errors = driver.find_elements(By.CLASS_NAME, "tds-form-feedback-text")
for error in errors:
    assert(not error.is_displayed())

submit = driver.find_element(By.ID, "edit-submit-td-ajax0")
assert(submit.is_displayed())
assert(submit.is_enabled())
submit.click()


wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "edit-submit-td-ajax-3")))

submit = driver.find_element(By.ID, "edit-submit-td-ajax-3")
assert(submit.is_displayed())
assert(submit.is_enabled())
submit.click()

time.sleep(2)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "edit-submit-complete-later")))

driver.execute_script("window.scrollBy(0, 2500);")
time.sleep(1)

button = driver.find_element(By.ID, "edit-submit-complete-later")
button.click()

wait = WebDriverWait(driver, 10)
time.sleep(2)

success = driver.find_element(By.CLASS_NAME, "success-image")
assert(success.is_displayed())


time.sleep(2)

# Закрытие браузера
driver.quit()