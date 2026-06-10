import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utilities import read_config


browser=read_config.get_data("basic info","browser")
url=read_config.get_data("basic info","url")
@pytest.fixture
def setup_and_teardown(request):
    if browser=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        wait=WebDriverWait(driver,15)
        request.cls.driver=driver
        request.cls.wait=wait
        yield
        driver.quit()