from selenium.webdriver.support import expected_conditions

from pages.MyAccountPage import MyAccountPage
from actions.baseAction import BaseAction


class MyAccountAction(BaseAction):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.ma=MyAccountPage(driver)
    
    def getAccountMessage(self):
       return self.wait.until(expected_conditions.visibility_of_element_located((self.ma.assertionMessage))).text