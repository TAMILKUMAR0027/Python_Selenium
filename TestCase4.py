from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
wait = WebDriverWait(d, 10)
d.maximize_window()
d.get("https://automationexercise.com/")
d.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Signup']"))
)
d.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(
    "tamilkumar0027@gmail.com"
)
d.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Kiot1234")
d.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
msg = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[10]//a[1]"))).text
print(msg)
assert msg=="Logged in as TAMIL KUMAR"
d.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
logoutMessage=wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Login to your account']"))).text
print(logoutMessage)
assert logoutMessage=="Login to your account"