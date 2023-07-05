from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from natalya_ivanenko.hw_6.tests.locators import header_locators

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

driver.maximize_window()
# Открытие страницы
driver.get("https://www.tesla.com/")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located(header_locators.header))

buttons = driver.find_elements(header_locators.header_btn)
for item in buttons:
    ActionChains(driver).move_to_element(item).perform()
    assert(item.is_displayed())

# Нахождение элементов на странице
logo = driver.find_element(header_locators.header_logo)
ActionChains(driver).move_to_element(logo).perform()
assert(logo.is_displayed())

# Закрытие браузера
driver.quit()