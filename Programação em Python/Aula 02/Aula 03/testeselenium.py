import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://kahoot.it/")
time.sleep(1)
print(f"Página atual: {driver.current_url}")
print(f"Título da página: {driver.title}")