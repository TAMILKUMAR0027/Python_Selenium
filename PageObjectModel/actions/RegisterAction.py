from utilities import excelReader
from pages.RegisterPage import RegisterPage
from actions.baseAction import BaseAction


class RegisterAction(BaseAction):
    data = excelReader.get_data(r"D:\Python_Selenium_Expleo\PageObjectModel\Excel_files\register_data.xlsx","Sheet1")
    fn=data[0][0]
    ln=data[0][1]
    email=data[0][2]
    ph=data[0][3]
    password=data[0][4]
    retypePassword=data[0][5]
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.Rp=RegisterPage(driver)
    
    def set_firstName(self):
        self.driver.find_element(*self.Rp.firstName).send_keys(self.fn)
    def set_lastName(self):
        self.driver.find_element(*self.Rp.lastName).send_keys(self.ln)
    def set_email(self):
        self.driver.find_element(*self.Rp.email).send_keys(self.email)
    def set_phone(self):
        self.driver.find_element(*self.Rp.phone).send_keys(self.ph)
    def set_password(self):
        self.driver.find_element(*self.Rp.password).send_keys(self.password)
    def set_repassword(self):
        self.driver.find_element(*self.Rp.Retype_Password).send_keys(self.retypePassword)
    def clickChechBox(self):
        self.driver.find_element(*self.Rp.policy_checkBox).click()
    def clickContinue(self):
        self.driver.find_element(*self.Rp.Registerbtn).click()
    