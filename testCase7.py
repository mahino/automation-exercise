import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-extensions")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]').click()
time.sleep(2)
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/div/div[1]/div/h2'))
    WebDriverWait(driver, 5).until(element_present)
    print("Page loaded successfully!")
except Exception as err:

    print("Timed out waiting for page to load.", err)
time.sleep(2)
driver.close()