from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dismiss_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll('iframe').forEach(frame => {
                let src = frame.src || '';
                let id = frame.id || '';

                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads') ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift') ||
                    id.includes('google_ads')
                ) {
                    frame.remove();
                }
            });
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")

d = webdriver.Chrome()
d.maximize_window()
wait=WebDriverWait(d,10)
d.get("https://automationexercise.com")
products=d.find_element(By.XPATH, "//a[@href='/products']")
products.click()
dismiss_ads(d)