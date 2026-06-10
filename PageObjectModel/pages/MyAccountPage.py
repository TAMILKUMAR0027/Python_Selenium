from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    assertionMessage=By.XPATH,"//h2[normalize-space()='My Account']"