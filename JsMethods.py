
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


d=webdriver.Chrome()
d.maximize_window()
d.get("https://leafground.com/dashboard.xhtml")
submit=d.find_element(By.XPATH,"//span[normalize-space()='Send']")
d.execute_script("window.scrollBy(0,500);")
d.execute_script("arguments[0].scrollIntoView();",submit)


email=d.find_element(By.XPATH,"//input[@id='email']")
msg=d.find_element(By.XPATH,"//textarea[@id='message']")
d.execute_script("arguments[0].value='tamil@gmail.com';", email)
d.execute_script("arguments[0].value='Hello bye how are you';", msg)
d.execute_script("arguments[0].click();", submit)
d.execute_script("arguments[0].style.border='3px solid red';",submit)
d.execute_script("arguments[0].style.backgroundColor='green';", submit)
title = d.execute_script("return document.title;")
print(title)