from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait


d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.demoblaze.com/")
wait=WebDriverWait(d,10)
d.find_element(By.XPATH,"//a[@id='login2']").click()
username=d.find_element(By.XPATH,"//input[@id='loginusername']")
username.send_keys("TamilKumar")
password=d.find_element(locate_with(By.TAG_NAME,"input").below(username))
password.send_keys("Kiot1234")
cancel=d.find_element(By.XPATH,"(//button[text()='Close'])[3]")
d.find_element(locate_with(By.TAG_NAME,"button").near(cancel)).click()
