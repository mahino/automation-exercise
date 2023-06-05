import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-extensions")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
userEmail = random.choice(["mohan4@gmail.com"])#, "mohan2@gmail.com","mohan3@gmail.com","mohan4@gmail.com"])
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys("mohan")
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys(userEmail)
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
if len(driver.find_elements(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/p')) == 0:
    if driver.find_element(By.XPATH, '//*[@id="id_gender1"]').is_displayed():
        driver.find_element(By.XPATH, '//*[@id="id_gender1"]').click()
    else:
        driver.close()
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Mohan")
    driver.find_element(By.XPATH, '//*[@id="days"]/option[6]').click()
    driver.find_element(By.XPATH, '//*[@id="months"]/option[6]').click()
    driver.find_element(By.XPATH, '//*[@id="years"]/option[25]').click()
    driver.find_element(By.XPATH, '//*[@id="first_name"]').send_keys("Mohan")
    driver.find_element(By.XPATH, '//*[@id="last_name"]').send_keys("Mohan")
    driver.find_element(By.XPATH, '//*[@id="address1"]').send_keys("Mohan")
    driver.find_element(By.XPATH, '//*[@id="state"]').send_keys("andhrapradesh")
    driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("Guntur")
    driver.find_element(By.XPATH, '//*[@id="zipcode"]').send_keys("560029")
    driver.find_element(By.XPATH, '//*[@id="mobile_number"]').send_keys("8374541653")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/form/button').click()
    time.sleep(2)
    print("Succefully created account")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
    time.sleep(2)
    print("Succefully entered user home page account")
else:
    print("User already created, Logging in..")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys("mohan@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys("Mohan")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()
    print("Succefully deleted user")
time.sleep(2)
driver.close()