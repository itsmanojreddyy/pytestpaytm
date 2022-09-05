from pathlib import Path

import pytest
from _pytest.fixtures import fixture
from selenium import webdriver

from globals.dir_global import DRIVERS_PATH
from pages.HomePage import HomePage
from pages.PaytmSignInPage import PaytmSignInPage


@pytest.fixture(scope='class')
def setup(request):
    global Web_driver
    print("initiating chrome driver")
    Web_driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    Web_driver.maximize_window()
    Web_driver.get("https://paytm.com/");
    request.cls.driver = Web_driver
    yield
    Web_driver.close()


@pytest.fixture(scope='function')
def beforeTest():
    print("Before Test")
    yield
    print("After test")


@fixture
# Instantiates Page Objects
def pages():
    Home_Page = HomePage(Web_driver)
    PaytmSignIn_Page = PaytmSignInPage(Web_driver)
    return locals()
