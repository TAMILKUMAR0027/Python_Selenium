import pytest
from selenium import webdriver


@pytest.fixture(params=[('chrome'),('edge')])
def setUp_TearDown(request):
    if request.param=='chrome':
        d=webdriver.Chrome()
    elif request.param=='edge':
        d=webdriver.Edge()
    
    d.maximize_window()
    d.implicitly_wait(10)
    d.get("https://tutorialsninja.com/demo/")
    request.cls.d=d 
    yield
    d.quit()
