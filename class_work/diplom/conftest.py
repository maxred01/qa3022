import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import pytest, requests, logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
from selenium.webdriver import DesiredCapabilities
# from api_test.app import Application
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import *


# @pytest.fixture(scope='function')
# def driver():
#     options = Options()
#     options.add_argument('log-level=3')
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options.add_argument('window-size=1920,1080')
#     my_driver = webdriver.Chrome(options=options)
#     my_driver.implicitly_wait(10)
#     yield my_driver
#     my_driver.quit()


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def change_pass_back():
    yield
    session = requests.Session()
    data = {
        "login": "79964410394",
        "password": "R911t689012345",
        "remember": False
    }
    url = "https://apteka.magnit.ru/api/personal/auth/"

    session.post(url, data=data)

    url = "https://apteka.magnit.ru/api/personal/password/change/"

    data = {
        'password': 'R911t68901234%',
        'passwordConfirm': 'R911t68901234%',
        'currentPassword': 'R911t689012345'}

    session.post(url, data=data)
