from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализация браузера
driver = webdriver.Chrome()
driver.get("https://demoqa.com/auto-complete")

# Ожидание загрузки страницы
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-group")))

# Получаем все поля ввода на странице
input_fields = driver.find_elements(By.CSS_SELECTOR, ".form-group input[type='text']")

for input_field in input_fields:
    # Вводим значение в поле ввода
    input_field.send_keys("s")

    # Ожидаем появления выпадающего списка
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".auto-complete__menu")))

    # Получаем все элементы в выпадающем списке
    menu_items = driver.find_elements(By.CSS_SELECTOR, ".auto-complete__menu-item")

    # Проверяем, что хотя бы один элемент в списке соответствует ожидаемому значению
    expected_value = "Sri Lanka"
    found_value = False
    for menu_item in menu_items:
        if expected_value in menu_item.text:
            found_value = True
            break
    assert found_value, f"Expected value '{expected_value}' not found in dropdown menu for input field with placeholder '{input_field.get_attribute('placeholder')}'"

# Закрываем браузер
driver.quit()
