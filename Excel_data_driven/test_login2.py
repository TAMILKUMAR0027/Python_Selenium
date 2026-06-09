import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import excelReader


class TestLogin:

    def setup_method(self):
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("https://www.demoblaze.com/")

    def teardown_method(self):
        self.d.quit()

    def test_login(self):
        data = excelReader.get_data(
            r"D:\Python_Selenium_Expleo\Excel_data_driven\ExcelFiles\Login_data.xlsx",
            "login"
        )

        username = data[0][0]
        password = data[0][1]

        self.d.find_element(By.ID, "login2").click()
        self.d.find_element(By.ID, "loginusername").send_keys(username)
        self.d.find_element(By.ID, "loginpassword").send_keys(password)
        self.d.find_element(By.XPATH, "//button[text()='Log in']").click()

        wait = WebDriverWait(self.d, 15)

        msg = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(text(),'Welcome')]")
            )
        )

        print(msg.text)
        assert "Welcome" in msg.text

    def test_invalid_login(self):
        data = excelReader.get_data(
            r"D:\Python_Selenium_Expleo\Excel_data_driven\ExcelFiles\Login_data.xlsx",
            "login"
        )

        username = data[1][0]
        password = data[1][1]

        self.d.find_element(By.ID, "login2").click()
        self.d.find_element(By.ID, "loginusername").send_keys(username)
        self.d.find_element(By.ID, "loginpassword").send_keys(password)
        self.d.find_element(By.XPATH, "//button[text()='Log in']").click()

        # Invalid login → alert expected OR error message
        wait = WebDriverWait(self.d, 5)

        try:
            alert = wait.until(EC.alert_is_present())
            alert.accept()
            assert True
        except:
            # fallback: check no welcome message
            assert "Welcome" not in self.d.page_source