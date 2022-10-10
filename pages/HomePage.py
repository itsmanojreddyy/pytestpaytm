from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    Search_Box = (By.CSS_SELECTOR, '#twotabsearchtextbox')

    def __init__(self, driver):
        super().__init__(driver)

    def click_search(self):
        self.click(self.Search_Box)
        self.send_keys(self.Search_Box,'Mobile')
