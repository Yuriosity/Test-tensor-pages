from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def start_driver():
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    
    service = Service(executable_path=r'chromedriver-win64\chromedriver-win64\chromedriver.exe')
    return webdriver.Chrome(service=service, options=chrome_options)