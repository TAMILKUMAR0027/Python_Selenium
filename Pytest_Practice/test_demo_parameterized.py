import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('search',[('selenium'),('Tamil'),('Kiot')])
def test_search(search):
    d=webdriver.Chrome()
    d.maximize_window()
    d.get("https://www.google.com/")
    s1=d.find_element(By.XPATH,"//textarea[@id='APjFqb']")
    s1.send_keys(search)
    time.sleep(5)
    d.quit()