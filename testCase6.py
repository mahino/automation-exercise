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
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a').click()
if driver.find_element(By.XPATH, '//*[@id="contact-page"]/div[2]/div[1]/div/h2').is_displayed():
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[1]/input').send_keys("MOHAN") #Name
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[2]/input').send_keys("MOHAN@gmail.com") #MAIL
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[3]/input').send_keys("MOHAN") #SUBJECT
    driver.find_element(By.XPATH, '//*[@id="message"]').send_keys("MOHAN") #Message
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[5]/input').send_keys("/Users/mohanas/Desktop/killer.sql") #file
    driver.find_element(By.XPATH, '//*[@id="contact-us-form"]/div[6]/input').click() #submit
    alert = driver.switch_to.alert
    alert.accept()
    print("Submitted succefully")
    if driver.find_elements(By.XPATH, '//*[@id="contact-page"]/div[2]/div[1]/div/div[2]'):
        driver.find_element(By.XPATH, '//*[@id="form-section"]/a/span').click()
    print("Returned Home.")
else:
    print("Not found")
time.sleep(2)
driver.close()