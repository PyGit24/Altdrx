# Python Sign Up User Credentials
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome()
driver.get("https://altdrx.com/")
class signup_cred():
	username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Full Name"]')))
	username.send_keys('Narasimha')
	ResiStatus = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Residential Status"]')))
	ResiStatus.send_keys('admin123')
	password = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
	password.send_keys('admin123')
	login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
	login_button.click()
time.sleep(5)