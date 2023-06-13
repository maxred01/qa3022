from selenium import webdriver
import time

# создаем экземпляр драйвера для Chrome
driver = webdriver.Chrome()

# переходим на страницу https://demoqa.com/checkbox
driver.get("https://demoqa.com/checkbox")

# ждем, пока страница полностью загрузится
time.sleep(2)

# находим все чекбоксы на странице
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

# проверяем каждый чекбокс
for checkbox in checkboxes:
    # если чекбокс не выбран, то кликаем на него
    if not checkbox.is_selected():
        checkbox.click()

# закрываем браузер
driver.quit()
