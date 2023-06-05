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
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--load-extension=/path/to/adblock_extension_directory')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]').click()
time.sleep(2)
print("Landed on cart page.")
try:
    driver.find_element(By.XPATH, '//*[@id="susbscribe_email"]').send_keys("mohan1@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="subscribe"]').click()
    if driver.find_element(By.XPATH, '//*[@id="success-subscribe"]/div').is_displayed():
        print("You have been successfully subscribed!")
    else:
        print("failed to subscribe")
except Exception as err:
    print("Timed out waiting for page to load.", err)
time.sleep(2)
driver.close()