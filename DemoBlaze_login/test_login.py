import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import read_config
@pytest.mark.usefixtures("setup_tearDown")
class TestLogin:
    def test_login(self):
      self.d.find_element(By.XPATH,"//a[@id='login2']").click()
      username=read_config.get_config("Login Credential","username")
      password=read_config.get_config("Login Credential","pass")
      self.d.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
      self.d.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
      self.d.find_element(By.XPATH,"//button[text()='Log in']").click()
      msg=self.d.find_element(By.XPATH,"//a[text()='Welcome TamilKumar']")
      print(msg.text)
      assert msg.text=='Welcome TamilKumar'
   
    def test_invalid(self):
         self.d.find_element(By.XPATH,"//a[@id='login2']").click()
         username=read_config.get_config("Login Credential","invalidusername")
         password=read_config.get_config("Login Credential","inpass")
         self.d.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
         self.d.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
         self.d.find_element(By.XPATH,"//button[text()='Log in']").click()
         
         
         
         
         