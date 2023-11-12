from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)

driver.get('https://web.whatsapp.com')

time.sleep(5)
driver.quit()