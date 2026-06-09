import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setUp_TearDown")
class TestSearch:

    def test_validate(self):
        self.d.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP")
        self.d.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.d.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']").is_displayed()

    def test_invalid(self):
        self.d.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("kiot")
        self.d.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        kiot = self.d.find_elements(By.XPATH, "//a[normalize-space()='HP LP3065']")
        assert len(kiot) == 0