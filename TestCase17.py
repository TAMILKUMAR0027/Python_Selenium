from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def dismiss_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll(
                "iframe, .adsbygoogle, [id*='google_ads'], [id*='aswift']"
            ).forEach(el => el.remove());
        """)
        print("Ads removed")
    except Exception as e:
        print("No ads found:", e)
d=webdriver.Chrome()
d.maximize_window()
wait =WebDriverWait(d,10)
d.get("https://automationexercise.com/")
dismiss_ads(d)

product1 = wait.until(
    expected_conditions.element_to_be_clickable(
        (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    )
)
product1.click()
d.find_element(By.XPATH,"//u[normalize-space()='View Cart']").click()
dismiss_ads(d)
title=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Blue Top']")))
print(title.text)
d.find_element(By.XPATH,"//i[@class='fa fa-times']").click()
assert title.text==""
print("product removed")