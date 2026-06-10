from selenium.webdriver.support import expected_conditions

from utilities import csvReader
from pages.LoginPage import LoginPage
from actions.baseAction import BaseAction


class LoginPageAction(BaseAction):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.lp=LoginPage(driver)
    data=csvReader.read_csv()[0]
    
    def set_email(self):
        self.wait.until(expected_conditions.visibility_of_element_located((self.lp.email))).send_keys(self.data['username'])
    def set_password(self):
        self.driver.find_element(*self.lp.password).send_keys(self.data['password'])
    def clickLogin(self):
        self.driver.find_element(*self.lp.LoginButton).click()
    