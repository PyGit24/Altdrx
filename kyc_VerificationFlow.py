from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.altdrx.com/login")

# Log In
driver.find_element(By.ID, "username").send_keys("newuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "loginButton").click()

# Navigate to KYC
driver.find_element(By.LINK_TEXT, "KYC Verification").click()
driver.find_element(By.ID, "uploadDocument").send_keys("/path/to/document.jpg")
driver.find_element(By.ID, "submitButton").click()

# Wait for processing
time.sleep(5)  # Adjust based on actual processing time

# Verification
assert "Verification successful" in driver.page_source
driver.quit()
