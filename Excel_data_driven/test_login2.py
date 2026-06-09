import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import logger

from Utilities import excelReader


class TestLogin:
    def test_login(self):
        data = excelReader.get_data(r"D:\Python_Selenium_Expleo\Excel_data_driven\ExcelFiles\Login_data.xlsx","login")
        username=data[0][0]
        password=data[0][1]
        self.d=webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("https://www.demoblaze.com/")
        logger.info("Website is launched")
        self.d.find_element(By.XPATH,"//a[@id='login2']").click()
        self.d.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
        self.d.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
        self.d.find_element(By.XPATH,"//button[text()='Log in']").click()
        msg=self.d.find_element(By.XPATH,"//a[text()='Welcome TamilKumar']")
        print(msg.text)
        assert msg.text=='Welcome TamilKumar'
        self.d.quit()
    def test_invalid_login(self):
        data = excelReader.get_data(r"D:\Python_Selenium_Expleo\Excel_data_driven\ExcelFiles\Login_data.xlsx","login")
        username=data[1][0]
        password=data[1][1]
        self.d=webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("https://www.demoblaze.com/")
        self.d.find_element(By.XPATH,"//a[@id='login2']").click()
        self.d.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
        self.d.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
        self.d.find_element(By.XPATH,"//button[text()='Log in']").click()
        self.d.quit()