import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
        a = ActionChains(driver)
        m = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]')
        a.move_to_element(m).perform()
        print("Hoverd to first product")
        driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a').click()
        print("Product added to cart successfully!")
        pop_up_present = EC.presence_of_element_located((By.XPATH, '//*[@id="cartModal"]/div/div'))
        if WebDriverWait(driver, 10).until(pop_up_present):
            print(driver.window_handles)
            ele = driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a')
            time.sleep(5)
            a.move_to_element(ele).perform()
            ele.click()
            if driver.find_elements(By.XPATH, '//*[@id="cart_items"]/div/div[1]/ol/li[2]'):
                print("Landed Successfully on cart page!")
            else:
                print("Failed to loan cart page")
        else:
            print("unable to switch to popup!")
    else:
        print("first Product not found")
except Exception as err:
    print("Timed out waiting for page to load.", err)
time.sleep(2)
driver.close()