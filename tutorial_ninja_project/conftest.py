import pytest
from selenium import webdriver

from Utilities import read_config
from log import logCreator

log=logCreator.log_generator()
@pytest.fixture
def setup_tearDown(request):
    
    browser=read_config.get_config("basic info","browser")
    url=read_config.get_config("basic info","url")
    if browser=='chrome':
      d=webdriver.Chrome()
      d.maximize_window()
      d.implicitly_wait(10)
      d.get(url)
      log.info("Website launched")
      request.cls.d=d
      yield
      d.quit()