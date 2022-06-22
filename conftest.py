import pytest
from selenium import webdriver

from TestData.test_data import login_data


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="Chrome"
    )


@pytest.fixture(scope="class")
def setup1(request):
    browser_Name = request.config.getoption("browser_Name")
    if browser_Name == "Chrome":
        driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")

    elif browser_Name == "Firefox":
        driver = webdriver.Firefox(executable_path="C:/geckodriver.exe")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(params=login_data.loginData)
def getData(request):
    return request.param
