from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


d = webdriver.Chrome()
d.maximize_window()
wait=WebDriverWait(d,10)
d.get("https://automationexercise.com")
products=d.find_element(By.XPATH, "//a[@href='/products']")
products.click()
dismiss_ads(d)
d.find_element(By.XPATH,"//input[@id='search_product']").send_keys("Shirt")
d.find_element(By.XPATH,"//button[@id='submit_search']").click()
dismiss_ads(d)
search=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='overlay-content']//p[contains(text(),'Men Tshirt')]"))).text
print(search)