from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\zagr\\WebDriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
time.sleep(3)
driver.quit()