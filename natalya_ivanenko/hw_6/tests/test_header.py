from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from hw_6.pages.locators import header_locators

def test_header(driver):
    wait.until(EC.presence_of_element_located(header_locators.header))

    buttons = driver.find_elements(header_locators.header_btn)
    for item in buttons:
        ActionChains(driver).move_to_element(item).perform()
        assert(item.is_displayed())

    # Нахождение элементов на странице
    logo = driver.find_element(header_locators.header_logo)
    ActionChains(driver).move_to_element(logo).perform()
    assert(logo.is_displayed())
