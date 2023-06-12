from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check


def navigation_to_section(driver, index):
    btn = driver.find_element(By.XPATH, f"(//div[@class='card mt-4 top-card'])[{index}]")
    check.is_true(btn.is_displayed())
    btn.click()
    driver.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']").click()


chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demoqa.com/')
chrome_driver.maximize_window()

navigation_to_section(chrome_driver, 1)
navigation_to_section(chrome_driver, 2)
navigation_to_section(chrome_driver, 3)
navigation_to_section(chrome_driver, 4)
navigation_to_section(chrome_driver, 5)
chrome_driver.execute_script("window.scrollBy(0, 500);")
navigation_to_section(chrome_driver, 6)

chrome_driver.quit()
