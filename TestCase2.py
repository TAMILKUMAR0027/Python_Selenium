from ast import Assert
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
d = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(d, 10)
d.get("http://automationexercise.com")
d.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Signup']"))
)
d.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(
    "tamilkumar9081@gmail.com"
)
d.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Kiot1234")
d.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
msg = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[10]//a[1]"))).text
print(msg)
assert msg == "Logged in as Tamil"
d.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()
print(d.find_element(By.XPATH, "//b[normalize-space()='Account Deleted!']").text)
