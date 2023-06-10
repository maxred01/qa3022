'''Click on six buttons'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check  # type: ignore

chrome_driver = webdriver.Chrome()
URL = "https://demoqa.com/"
chrome_driver.get(URL)
chrome_driver.set_window_size(1024, 768)

btn_elements = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
a_btn = btn_elements.is_displayed()
if check.is_true(a_btn):
    print('Button Elements is displayed')
    btn_elements.click()
    time.sleep(2)
else:
    print('Button Elements is NOT displayed')

chrome_driver.get(URL)

btn_forms = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]')
b_btn = btn_forms.is_displayed()
if check.is_true(b_btn):
    print('Button Forms is displayed')
    btn_forms.click()
    time.sleep(2)
else:
    print('Button Forms is NOT displayed')

chrome_driver.get(URL)

btn_alerts_frame_windows = chrome_driver.find_element(By.XPATH,
                                                      '//*[@id="app"]/div/div/div[2]/div/div[3]')
c_btn = btn_alerts_frame_windows.is_displayed()
if check.is_true(c_btn):
    print('Button Alerts, Frame & Windows is displayed')
    btn_alerts_frame_windows.click()
    time.sleep(2)
else:
    print('Button Alerts, Frame & Windows is NOT displayed')

chrome_driver.get(URL)

btn_widgets = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]')
d_btn = btn_widgets.is_displayed()
if check.is_true(d_btn):
    print('Button Widgets is displayed')
    btn_widgets.click()
    time.sleep(2)
else:
    print('Button Widgets is NOT displayed')

chrome_driver.get(URL)

btn_interactions = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]')
e_btn = btn_interactions.is_displayed()
if check.is_true(e_btn):
    print('Button Interactions is displayed')
    btn_interactions.click()
    time.sleep(2)
else:
    print('Button Interactions is NOT displayed')

chrome_driver.get(URL)

btn_book_store_application = chrome_driver.find_element(By.XPATH,
                                                        '//*[@id="app"]/div/div/div[2]/div/div[6]')
f_btn = btn_book_store_application.is_displayed()
if check.is_true(f_btn):
    print('Button Book Store Application is displayed')
    btn_book_store_application.click()
    time.sleep(2)
else:
    print('Button Book Store Application is NOT displayed')

chrome_driver.quit()
