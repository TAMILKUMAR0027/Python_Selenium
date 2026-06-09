from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_function():
    global d
    d=webdriver.Chrome()
    d.maximize_window()
    d.implicitly_wait(10)
    d.get("https://tutorialsninja.com/demo/")
def teardown_function():
    d.quit()

def test_validate():
    d.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("HP")
    d.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    assert d.find_element(By.XPATH,"//a[normalize-space()='HP LP3065']").is_displayed()
def test_invalid():
    d.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("kiot")
    d.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    kiot = d.find_elements(By.XPATH, "//a[normalize-space()='HP LP3065']")
    assert len(kiot)==0
