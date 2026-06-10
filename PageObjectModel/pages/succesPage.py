from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class SuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    accountCreated=By.XPATH,"//h1[normalize-space()='Your Account Has Been Created!']"