from math import exp
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities import LogCreator
from Utilities import excelReader

log = LogCreator.log_generator() 
@pytest.mark.parametrize("username,password",excelReader.get_data("ExcelFiles/Login_data.xlsx","login"))
class TestLogin:
    def test_login(self,username,password):
        self.d=webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("https://www.demoblaze.com/")
        log.info("Website is launched")
        self.d.find_element(By.XPATH,"//a[@id='login2']").click()
        self.d.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
        self.d.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
        self.d.find_element(By.XPATH,"//button[text()='Log in']").click()
        try:
          msg=self.d.find_element(By.XPATH,"//a[text()='Welcome TamilKumar']")
          print(msg.text)
          assert msg.text=='Welcome TamilKumar'
          
        except:
            time.sleep(10)
            self.d.switch_to.alert.accept
        self.d.quit()
            