import time

from selenium.webdriver.support import expected_conditions

from actions.baseAction import BaseAction
from pages.homePage import HomePage


class HomePageAction(BaseAction):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.hp = HomePage(driver)

    def clickMyAccount(self):
        self.wait.until(expected_conditions.visibility_of_element_located((self.hp.Myaccount))).click()

    def clickRegister(self):
        self.wait.until(expected_conditions.visibility_of_element_located((self.hp.Register))).click()
    def clickProduct(self):
        self.driver.find_element(*self.hp.hpProduct).click()
    def clickLogin(self):
        self.driver.find_element(*self.hp.Login).click()