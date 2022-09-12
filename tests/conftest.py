from pathlib import Path

import pytest
from _pytest.fixtures import fixture
from selenium import webdriver
from pages.HomePage import HomePage
from pages.PaytmSignInPage import PaytmSignInPage
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def setup(request):
    global Web_driver
    print("initiating chrome driver")
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # optional
    chrome_options.add_argument('--no-sandbox')
    # optional
    chrome_options.add_argument('--disable-dev-shm-usage')

    Web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # if not added in PATH
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
