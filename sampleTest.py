import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
search=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
search.send_keys("Selenium")
if(search.is_displayed()):
    print("Yes")
search.send_keys(Keys.ENTER)

driver.quit()
