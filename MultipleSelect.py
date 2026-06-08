from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


d=webdriver.Chrome()
d.maximize_window()
d.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
drop=d.find_element(By.XPATH,"//select[@id='ide']")
sec=Select(drop)
sec.select_by_visible_text("Eclipse")
sec.select_by_index(3)
k=sec.all_selected_options
for i in k:
    print(i.text)
print(sec.first_selected_option.text)
sec.deselect_all()
