from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.get("https://demoqa.com/browser-windows")
parent=d.current_window_handle
print("Current window: ",d.current_window_handle)
d.find_element(By.XPATH,"//button[@id='tabButton']").click()
d.switch_to.window(parent)
new_Window=d.find_element(By.XPATH,"//button[@id='windowButton']")
new_Window.click()
