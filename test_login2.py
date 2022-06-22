import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import getData


@pytest.mark.usefixtures("setup1")
class TestLogin:

    def test_title(self):
        title = self.driver.title
        print(title)
        if title == "Swag Labs":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_title.png")
            assert False

    def test_login(self, getData):
        self.driver.find_element(By.ID, "user-name").send_keys(getData["email"])
        self.driver.find_element(By.ID, "password").send_keys(getData["password"])
        self.driver.find_element(By.ID, "login-button").click()

