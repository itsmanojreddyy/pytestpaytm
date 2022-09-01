import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PaytmSignInPage(BasePage):
    Search_Box = (By.XPATH, '//span[text()="Sign In"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Clicking on Search box in Paytm")
    def click_signin(self):
        self.click(self.Search_Box)
        with allure.step("In Step for for Click for Sign In"):
            pass
        allure.attach(
            self._driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
