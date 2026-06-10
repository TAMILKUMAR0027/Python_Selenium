from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    AddToCart=By.XPATH,"//button[@id='button-cart']"
    SuccessMessage=By.XPATH,"//div[@class='alert alert-success alert-dismissible']"