from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

# Open the desired webpage
driver.get('https://www.saucedemo.com/')

# Display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)

# Locate the username field, password field and login button
username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

# Enter the credentials and log in
username.send_keys('standard_user')
password.send_keys('secret_sauce')
login_button.click()

# Wait for the page to load completely
time.sleep(5)

# Display cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

# Perform logout
menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
menu_button.click()
time.sleep(2)
logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()

# Close the WebDriver
driver.quit()