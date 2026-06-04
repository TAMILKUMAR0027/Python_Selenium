from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
wait = WebDriverWait(d, 10)
d.maximize_window()
d.get("https://automationexercise.com/")
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item active']//button[@type='button'][normalize-space()='Test Cases']"))).click()
testCaseMessage=wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Test Cases']"))).text
print(testCaseMessage)