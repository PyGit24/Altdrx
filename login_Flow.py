from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.altdrx.com/login")

# Log In
driver.find_element(By.ID, "Mobile Number").send_keys("9791194756")
driver.find_element(By.ID, "Enter OTP").send_keys("64794")
driver.find_element(By.ID, "SEND OTP").click()

# Verification
assert "Dashboard" in driver.page_source
driver.quit()
