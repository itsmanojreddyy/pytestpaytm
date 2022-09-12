import time

import allure
import pytest

from tests.test_base import BaseTest


@allure.epic("Paytm Sign In")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.security
@pytest.mark.usefixtures("setup")
class TestPaytmSignIn(BaseTest):

    # def test_click_signin(self):
    #     self.pages['PaytmSignIn_Page'].click_signin()

    @allure.description("Click on Paytm Sign in button")
    @allure.title("Click on Paytm Sign in")
    def test_click_SignIn(self):
       # self.pages['PaytmSignIn_Page'].click_signin()

    #@allure.description("Click on Paytm Sign in button")
    #@allure.title("Click on Paytm Sign in")
    def test_click_SignIn(self):
       # self.pages['PaytmSignIn_Page'].click_signin()