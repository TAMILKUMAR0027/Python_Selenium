from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.get('http://automationexercise.com')
d.find_element(By.XPATH,"")