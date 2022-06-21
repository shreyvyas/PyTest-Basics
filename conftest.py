import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(scope="class")
def setup1(request):
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
