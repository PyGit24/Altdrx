from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.altdrx.com/signup")

# Sign Up
driver.find_element(By.ID, "Full Name").send_keys("narasimha")
driver.find_element(By.ID, "Residential Status").send_keys("Resident Indian")
driver.find_element(By.ID, "Mobile Number").send_keys("9791194756")
driver.find_element(By.ID, "Mobile Number OTP").send_keys("44578")
driver.find_element(By.ID, "Email ID").send_keys("rasimpersi@gmail.com")
driver.find_element(By.ID, "REGISTER").click()

# Verification
assert "Confirmation" in driver.page_source
driver.quit()
