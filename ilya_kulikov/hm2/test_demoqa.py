from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check
import time

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demoqa.com/')
chrome_driver.maximize_window()

# Проверка 1-ой карточки
btn_elements = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"]'
                                                    '[position()=1]')
res_elements = btn_elements.is_displayed()
pytest_check.is_true(res_elements)
btn_elements.click()
# time.sleep(4)
chrome_driver.back()

# Проверка 2-ой карточки
btn_forms = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][position()=2]')
res_forms = btn_forms.is_displayed()
pytest_check.is_true(res_forms)
btn_forms.click()
# time.sleep(4)
chrome_driver.back()

# Проверка 3-ей карточки
btn_alerts = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][position()=3]')
res_alerts = btn_alerts.is_displayed()
pytest_check.is_true(res_alerts)
btn_alerts.click()
# time.sleep(3)
chrome_driver.back()

# Проверка 4-ой карточки
btn_widgets = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][position()=4]')
res_widgets = btn_widgets.is_displayed()
pytest_check.is_true(res_widgets)
btn_widgets.click()
# time.sleep(2)
chrome_driver.back()

# Проверка 5-ой карточки
btn_interactions = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"]'
                                                        '[position()=5]')
res_interactions = btn_interactions.is_displayed()
pytest_check.is_true(res_interactions)
btn_interactions.click()
# time.sleep(3)
chrome_driver.back()

# Проверка 6-ой карточки
btn_book_store = chrome_driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"]'
                                                      '[position()=6]')
res_book_store = btn_book_store.is_displayed()
pytest_check.is_true(res_book_store)
btn_book_store.click()

# time.sleep(5)
chrome_driver.quit()
