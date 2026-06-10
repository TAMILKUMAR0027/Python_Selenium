from selenium.webdriver.support import expected_conditions

from pages.ProductPage import ProductPage
from actions.baseAction import BaseAction


class ProductPageAction(BaseAction):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.pp=ProductPage(driver)
    
    def clickAddtoCart(self):
        self.wait.until(expected_conditions.element_to_be_clickable((self.pp.AddToCart))).click()
    
    def getSuccessMessage(self):
        return self.wait.until(expected_conditions.visibility_of_element_located((self.pp.SuccessMessage))).text