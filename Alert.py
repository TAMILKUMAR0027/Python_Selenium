import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


d=webdriver.Chrome()
d.maximize_window()
d.get("https://leafground.com/alert.xhtml")
print("-"*20)
print("Simple Alert")
d.find_element(By.XPATH,"//button[@id='j_idt88:j_idt91']//span[@class='ui-button-text ui-c'][normalize-space()='Show']").click()
a1=Alert(d)
d.switch_to.alert
a1.accept()

print(d.find_element(By.XPATH,"//span[@id='simple_result']").text)
print("-"*20)
print("Confirmation alert")
d.find_element(By.XPATH,"//button[@id='j_idt88:j_idt93']//span[@class='ui-button-text ui-c'][normalize-space()='Show']").click()
a1.accept()
print(d.find_element(By.XPATH,"//span[@id='result']").text)
d.find_element(By.XPATH,"//button[@id='j_idt88:j_idt93']//span[@class='ui-button-text ui-c'][normalize-space()='Show']").click()
a1.dismiss()
print(d.find_element(By.XPATH,"//span[@id='result']").text)
print("-"*20)
print("Prompt alert")
d.find_element(By.XPATH,"//button[@id='j_idt88:j_idt104']//span[@class='ui-button-text ui-c'][normalize-space()='Show']").click()
a1.send_keys("Tamil")
a1.accept()
print(d.find_element(By.XPATH,"//span[@id='confirm_result']").text)