import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.mark.parametrize('browser', ['chrome', 'edge'])
@pytest.mark.parametrize('url', [
    'https://www.google.com/',
    'https://omayo.blogspot.com/'
])
def test_browser_and_url(browser, url):

    if browser == 'chrome':
        opt = ChromeOptions()
        opt.add_argument("--headless=new")
        d = webdriver.Chrome(options=opt)

    elif browser == 'edge':
        opt = EdgeOptions()
        opt.add_argument("--headless=new")
        d = webdriver.Edge(options=opt)

    d.get(url)
    print(d.title)

    d.quit()