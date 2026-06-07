import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d=webdriver.Chrome()
d.maximize_window()
wait=WebDriverWait(d,10)
d.get("https://thinking-tester-contact-list.herokuapp.com/")
d.find_element(By.XPATH,"//input[@id='email']").send_keys("tamilkumar@gmail.com")
d.find_element(By.XPATH,"//input[@id='password']").send_keys("Kiot1234")
d.find_element(By.XPATH,"//button[@id='submit']").click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//table/thead/tr/th[1]")))
list=d.find_elements(By.XPATH,"//table/thead/tr/th")
for i in range(1,len(list)+1):
    val=d.find_element(By.XPATH,f"//table/thead/tr/th[{i}]").text
    print(val,end="|")
print('\n')
rows = len(d.find_elements(By.XPATH, "//table/tr"))
for i in range(1,rows+1):
    cols = len(d.find_elements(By.XPATH, f"//table/tr[{i}]/td"))
    for j in range(2,cols+1):
        val=d.find_element(By.XPATH,f"//table/tr[{i}]/td[{j}]").text
        print(val,end="|")
    print('\n')

d.quit()

