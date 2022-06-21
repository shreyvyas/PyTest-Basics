import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")            # setup method from conftest.py
class TestLogin:

    def test_title(self, setup):
        # we are returning driver in setup method. so here it need to pass
        title = setup.title      # no need of setup.driver (driver already in setup method)
        print(title)
        assert title == "Swag Labs"

    def test_login(self, setup):
        setup.find_element(By.ID, "user-name").send_keys("standard_user")
        setup.find_element(By.ID, "password").send_keys("secret_sauce")
        setup.find_element(By.ID, "login-button").click()

# but here one problem is we need to define teardown method as well so we can close the driver
# return and yield wont work together as return is part of function and yield is generator
# this concept we will cover in another python file test_login2.py
