import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-extensions")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
driver.get("https://automationexercise.com/")
userEmail = random.choice(["mohan1@gmail.com", "mohan2@gmail.com","mohan3@gmail.com","mohan4@gmail.com"])
userEmail = "mohan5@gmail.com"
print(userEmail)
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys(userEmail)
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys("Mohan")
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button').click()
if driver.find_elements(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p'):
    print("Your email or password is incorrect!")
else:
    print("Succefully logged in with EMAIL: " + userEmail)
time.sleep(2)
driver.close()