from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class HomePage(BasePage):

    Myaccount = (By.XPATH, "//span[normalize-space()='My Account']")
    Register = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']")
    hpProduct=By.XPATH,"//div[@class='image']//img[@title='MacBook']"
    Login=By.XPATH,"//a[normalize-space()='Login']"
    def __init__(self, driver):
        super().__init__(driver)