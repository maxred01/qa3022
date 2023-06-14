import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demoqa.com/')
chrome_driver.maximize_window()

# Кнопка вкладки
card_elements = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"]'
                                                    '[position()=1]')
card_elements.click()

# Вход на вкладку "Check Box"
card_check_box = chrome_driver.find_element(By.XPATH, '(//*[@id="item-1"])[1]')
card_check_box.click()

# Помещение всех чекбоксов в переменную btns
buttons = chrome_driver.find_elements(By.XPATH, '//*[@class="rct-checkbox"]')

# Раскрытие панели с чекбоксами
opn_btn = chrome_driver.find_element(By.XPATH, '//*[@title="Expand all"]')
opn_btn.click()


chrome_driver.execute_script("window.scrollBy(0, 300);")


for i in buttons:
    print(i.is_selected())
    i.click()
    print(i.is_selected())

time.sleep(5)
chrome_driver.quit()
