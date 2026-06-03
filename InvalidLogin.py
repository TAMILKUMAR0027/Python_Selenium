from ast import Assert
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
wait = WebDriverWait(d, 10)
d.get("https://automationexercise.com/")
d.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Signup']"))
)
d.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(
    "tamilkumar9081@gmail.com"
)
d.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Kiot1234")
d.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
msg = d.find_element(
    By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']"
).text

print(msg)
d.quit()
