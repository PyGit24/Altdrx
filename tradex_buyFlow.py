from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.altdrx.com/login")

# Log In
driver.find_element(By.ID, "username").send_keys("newuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "loginButton").click()

# Navigate to Tradex Buy
driver.find_element(By.LINK_TEXT, "Tradex Buy").click()
driver.find_element(By.ID, "product").click()  # Adjust according to actual product selection method
driver.find_element(By.ID, "quantity").send_keys("10")
driver.find_element(By.ID, "buyButton").click()

# Verification
assert "Purchase successful" in driver.page_source
driver.quit()
