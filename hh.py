import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

d = webdriver.Chrome()
d.maximize_window()

d.get("https://leafground.com/drag.xhtml")

act = ActionChains(d)

start = d.find_element(By.XPATH, "//span[normalize-space()='Start']")

origin = ScrollOrigin.from_element(start)
act.scroll_from_origin(origin, 0, -300).perform()
act.scroll_by_amount(0, 300).perform()
drag = d.find_element(By.XPATH, "//div[@id='form:conpnl_header']")
act.drag_and_drop_by_offset(drag, 200, 300).perform()
time.sleep(10)
d.quit()
