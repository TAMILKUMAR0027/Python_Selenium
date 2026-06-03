from ast import Assert
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
wait = WebDriverWait(d, 10)
d.get("http://automationexercise.com")
d.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Signup']"))
)
d.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Tamil")
d.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(
    "tamilkumar9081@gmail.com"
)
d.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Create Account']")
    )
)
d.find_element(By.XPATH, "//input[@id='password']").send_keys("Kiot1234")
d.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Tamil")
d.find_element(By.XPATH, "//input[@id='last_name']").send_keys("E")
d.find_element(By.XPATH, "//input[@id='address1']").send_keys("salem")
d.find_element(By.XPATH, "//input[@id='state']").send_keys("Tamilnadu")
d.find_element(By.XPATH, "//input[@id='city']").send_keys("Salem")
d.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("636365")
d.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("9008765432")
d.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
msg = d.find_element(By.XPATH, "//b[normalize-space()='Account Created!']").text
try:
    assert msg == "ACCOUNT CREATED!"
    print("Success fully created")
except:
    print("Not created")

d.quit()
