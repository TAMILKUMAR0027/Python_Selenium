import pytest
from pytest_check import check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from Utilities import excelReader
from log import logCreator
log=logCreator.log_generator()
@pytest.mark.usefixtures("setup_tearDown")
class Testlogin:
    def test_valid_login(self):
        data=excelReader.get_data("D:\\Python_Selenium_Expleo\\tutorial_ninja_project\\ExcelFiles\\Book1.xlsx","Sheet1")
        username=data[0][0]
        password=data[0][1]
        log.info("Data is extracted")
        self.d.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
        self.d.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@id='input-email']")))
        self.d.find_element(By.XPATH,"//input[@id='input-email']").send_keys(username)
        self.d.find_element(By.XPATH,"//input[@id='input-password']").send_keys(password)
        self.d.find_element(By.XPATH,"//input[@value='Login']").click()    
        log.info("Login successfull")
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='My Account']")))
        assert self.d.find_element(By.XPATH,"//h2[normalize-space()='My Account']").text=="My Account"    
    def test_invalid_login(self):
        data=excelReader.get_data("D:\\Python_Selenium_Expleo\\tutorial_ninja_project\\ExcelFiles\\Book1.xlsx","Sheet1")
        username=data[1][0]
        password=data[1][1]
        log.info("Data is extracted")
        self.d.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
        self.d.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@id='input-email']")))
        self.d.find_element(By.XPATH,"//input[@id='input-email']").send_keys(username)
        self.d.find_element(By.XPATH,"//input[@id='input-password']").send_keys(password)
        self.d.find_element(By.XPATH,"//input[@value='Login']").click()   
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")))
        msg=self.d.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text
        print(msg)
        check.equal("Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.",msg)