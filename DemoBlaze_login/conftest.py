import pytest
from selenium import webdriver
import read_config

@pytest.fixture
def setup_tearDown(request):
    browser=read_config.get_config("basic info","browser")
    url=read_config.get_config("basic info","url")
    if browser=='chrome':
      d=webdriver.Chrome()
      d.maximize_window()
      d.implicitly_wait(10)
      d.get(url)
      request.cls.d=d
      yield
      d.quit()