import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup1")
class TestLogin:

    def test_title(self):
        title = self.driver.title
        print(title)
        assert title == "Swag Labs"

    def test_login(self, setup):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

