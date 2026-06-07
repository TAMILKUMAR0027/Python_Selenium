from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.get("https://omayo.blogspot.com/")
frame=d.find_element(By.XPATH,"//iframe[@id='iframe1']")
d.switch_to.frame(frame)
print(d.find_element(By.XPATH,"//a[normalize-space()='What is Selenium?']").text)
d.switch_to.default_content()
d.quit()