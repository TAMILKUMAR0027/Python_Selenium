from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    email=By.XPATH,"//input[@id='input-email']"
    password=By.XPATH,"//input[@id='input-password']"
    LoginButton=By.XPATH,"//input[@value='Login']"