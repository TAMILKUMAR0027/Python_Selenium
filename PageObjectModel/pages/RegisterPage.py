from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class RegisterPage(BasePage):
    firstName=By.XPATH,"//input[@id='input-firstname']"
    lastName=By.XPATH,"//input[@id='input-lastname']"
    email=By.XPATH,"//input[@id='input-email']"
    phone=By.XPATH,"//input[@id='input-telephone']"
    password=By.XPATH,"//input[@id='input-password']"
    Retype_Password=By.XPATH,"//input[@id='input-confirm']"
    policy_checkBox=By.XPATH,"//input[@name='agree']"
    Registerbtn=By.XPATH,"//input[@value='Continue']"

    def __init__(self, driver):
        super().__init__(driver)
    