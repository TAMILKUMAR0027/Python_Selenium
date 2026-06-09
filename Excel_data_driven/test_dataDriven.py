import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import LogCreator
from Utilities import excelReader

log = LogCreator.log_generator()


@pytest.mark.parametrize(
    "username,password",
    excelReader.get_data(
        r"D:\Python_Selenium_Expleo\Excel_data_driven\ExcelFiles\Login_data.xlsx",
        "login"
    )
)
class TestLogin:

    def test_login(self, username, password):
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("https://www.demoblaze.com/")

        log.info("Website is launched")

        self.d.find_element(By.ID, "login2").click()
        self.d.find_element(By.ID, "loginusername").send_keys(username)
        self.d.find_element(By.ID, "loginpassword").send_keys(password)
        self.d.find_element(By.XPATH, "//button[text()='Log in']").click()

        try:
            wait = WebDriverWait(self.d, 10)

            msg = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(text(),'Welcome')]")
                )
            )

            print(msg.text)
            assert "Welcome" in msg.text

        except:
            try:
                alert = self.d.switch_to.alert
                alert.accept()
            except:
                log.info("No alert found")

        self.d.quit()