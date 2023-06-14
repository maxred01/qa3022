'''Check checkboxes'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#open site
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://demoqa.com/elements")
chrome_driver.maximize_window()

#click button check_box
btn_chek_box = chrome_driver.find_element(By.XPATH, '//span[contains(text(), "Check Box")]')
btn_chek_box.is_displayed()
btn_chek_box.click()
time.sleep(1)

#open tree checkboxes
tree_checkboxes1 = chrome_driver.find_element(By.XPATH, '//*[@id="tree-node"]'
                                                        '/ol/li/span/button')
tree_checkboxes1.click()
tree_checkboxes2 = chrome_driver.find_element(By.XPATH, '//*[@id="tree-node"]'
                                                        '/ol/li/ol/li[1]/span/button')
tree_checkboxes2.click()
tree_checkboxes3 = chrome_driver.find_element(By.XPATH, '//*[@id="tree-node"]'
                                                        '/ol/li/ol/li[2]/span/button')
tree_checkboxes3.click()
tree_checkboxes4 = chrome_driver.find_element(By.XPATH, '//*[@id="tree-node"]'
                                                        '/ol/li/ol/li[3]/span/button')
tree_checkboxes4.click()
tree_checkboxes5 = chrome_driver.find_element(By.XPATH, '//*[@id="tree-node"]'
                                                        '/ol/li/ol/li[2]/ol/li[1]/span/button')
tree_checkboxes5.click()
tree_checkboxes6 = chrome_driver.find_element(By.XPATH, '//*[@id="tree-node"]'
                                                        '/ol/li/ol/li[2]/ol/li[2]/span/button')
tree_checkboxes6.click()
time.sleep(1)

#page down
chrome_driver.execute_script("window.scrollBy(0, 250);")

#find all checkboxes
checkboxes = chrome_driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# click on all checkboxes
NUM = 1
for checkbox in checkboxes:
    checkbox.find_element(By.XPATH, f"(// span[@class ='rct-checkbox'])[{NUM}]").click()
    NUM += 1
    time.sleep(1)

#wait and close chrome
time.sleep(1)
chrome_driver.quit()
