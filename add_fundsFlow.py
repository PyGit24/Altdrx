from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.altdrx.com/login")

# Log In
driver.find_element(By.ID, "username").send_keys("newuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "loginButton").click()

# Navigate to Add Funds
driver.find_element(By.LINK_TEXT, "Add Funds").click()
driver.find_element(By.ID, "amount").send_keys("1000")
driver.find_element(By.ID, "addFundsButton").click()

# Verification
assert "Funds added successfully" in driver.page_source
driver.quit()
