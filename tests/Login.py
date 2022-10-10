import time

import pytest
from tests.test_base import BaseTest


@pytest.mark.usefixtures("setup")
class TestExampleOne(BaseTest):
    # def test_content_text(self):
    #     print("Verify content on the page")
    #     self.driver.get("https://brewdat-lh-appservice-dev.azurewebsites.net/")

    def test_search_product(self):
        self.pages['Home_Page'].click_search()
