import pytest
from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Utilities import excelReader
from log import logCreator

log = logCreator.log_generator()


@pytest.mark.usefixtures("setup_tearDown")
class Testlogin:

    def test_valid_login(self):

        data = excelReader.get_data(
            "D:\\Python_Selenium_Expleo\\tutorial_ninja_project\\ExcelFiles\\Book1.xlsx",
            "Sheet1"
        )

        username = data[0][0]
        password = data[0][1]

        log.info("Data is extracted")

        # Open My Account dropdown
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='My Account']"))
        ).click()

        # Click Login
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']"))
        ).click()

        # Enter credentials
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-email"))
        ).send_keys(username)

        self.d.find_element(By.ID, "input-password").send_keys(password)

        # Click login button
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))
        ).click()

        log.info("Login successful")

        # Assertion
        my_account_text = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='My Account']"))
        ).text

        assert my_account_text == "My Account"


    def test_invalid_login(self):

        data = excelReader.get_data(
            "D:\\Python_Selenium_Expleo\\tutorial_ninja_project\\ExcelFiles\\Book1.xlsx",
            "Sheet1"
        )

        username = data[1][0]
        password = data[1][1]

        log.info("Data is extracted")

        # Open My Account dropdown
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='My Account']"))
        ).click()

        # Click Login
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']"))
        ).click()

        # Enter credentials
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "input-email"))
        ).send_keys(username)

        self.d.find_element(By.ID, "input-password").send_keys(password)

        # Click login
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))
        ).click()

        # Error message
        msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
            )
        ).text

        print(msg)

        # Validation
        check.equal(
            "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.",
            msg
        )
