from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the website
    driver.get("https://altdrx.com/")

    # Inspect the page
    SignUp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/section[1]/div[1]/div[2]/button[1]')))
    SignUp.click()
    Login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/p/a')))
    Login.click()
    Ph_no = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div[1]/div/input')))
    Ph_no.send_keys("9791194756")
    checkbox = driver.find_element(By.CLASS_NAME, "orangeecheckbox")
    # Select the checkbox if it's not already selected
    if not checkbox.is_selected():
        checkbox.click()
    # Verify that the checkbox is now selected
    assert checkbox.is_selected() == True
    Otp_But = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/section/div[2]/div[4]/button')))
    Otp_But.click()
    Otp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div[2]/input')))
    Otp.send_keys("7654")

    # Ensure to enter the correct OTP
    verify_but = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'verifycheck')))
    verify_but.click()
    time.sleep(10)

finally:
    # Close the browser
    driver.quit()
