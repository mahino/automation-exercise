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
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]').click()

time.sleep(2)
try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/section[2]/div/div/div[2]/div/h2'))
    WebDriverWait(driver, 5).until(element_present)
    print("All Products Page loaded Successfully!")
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a'))
    s = WebDriverWait(driver, 10).until(element_present)
    if s:
        print(s)
        driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a/i').click()
        print("Product Selected")
        for i in ['/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2', '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]', '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span', '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]', '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]', '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]']:
            print(i)
            if driver.find_elements(By.XPATH, i):
                s = driver.find_element(By.XPATH, i)
                print(s)
            else:
                print("Failed to load fetch element", i)
    else:
        print("first Product not found")
except Exception as err:
    print("Timed out waiting for page to load.", err)
time.sleep(2)
driver.close()