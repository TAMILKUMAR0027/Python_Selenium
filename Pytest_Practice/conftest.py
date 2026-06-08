import pytest
from selenium import webdriver


@pytest.fixture()
def test_setup_and_teardown(request):
    d = webdriver.Chrome()
    d.maximize_window()
    d.implicitly_wait(10)
    d.get("https://tutorialsninja.com/demo/")
    request.cls.d = d   
    yield
    d.quit()