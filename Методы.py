import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAccordian(unittest.TestCase):
    def setUp(self):
        #инициализация браузера
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoga.com/accordian")
    def test_accordian(self):
        accordians = self.driver.find_element(By.CSS_SELECTOR,".accordian > div")
        self.assertEqual(len(accordians), 3)
        for accordian in accordians:
            accordian_header = accordian.find_element(By.CSS_SELECTOR, ".accordian-header")
            accordian_header.click()
            

