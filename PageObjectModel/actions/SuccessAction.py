from pages.succesPage import SuccessPage
from actions.baseAction import BaseAction


class SuccessAction(BaseAction):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.sp=SuccessPage(driver)
    
    def get_created_test(self):
        return self.driver.find_element(*self.sp.accountCreated).text
        