from selenium import webdriver
import time

# Открываем браузер chrome и переходим на страницу https://demoqa.com/upload-download
driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

# Загружаем файл
upload_input = driver.find_element_by_id("uploadFile")
upload_input.send_keys("/path/to/image.jpg")
time.sleep(2)

# Проверяем, что файл загружен
uploaded_file = driver.find_element_by_id("uploadedFilePath").text
assert uploaded_file != "", "Файл не был загружен"

# Закрываем браузер
driver.quit()
