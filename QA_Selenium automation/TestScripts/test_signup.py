# Import necessary libraries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

# Function to check for alert presence
def is_alert_present(driver):
    try:
        driver.switch_to.alert
        return True
    except:
        return False

# Function to generate a random username
def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def setUp():
    # Set up the WebDriver using Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Simplified driver setup
    driver.maximize_window()  # Maximize the window
    return driver

def signUp(driver, username, password):
    # Navigate to the signup page
    driver.get("https://www.demoblaze.com/")

    # Click on the "Sign Up" button (Modify based on actual HTML structure)
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)

    # Fill in the registration form
    driver.find_element(By.ID, "sign-username").send_keys(username)
    driver.find_element(By.ID, "sign-password").send_keys(password)
    time.sleep(1)

    # Click the "Sign Up" button
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
    time.sleep(2)
    
    # Check if an alert is present
    if is_alert_present(driver):
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert text:", alert_text)
        
        # Accept the alert to continue
        alert.accept()
    else:
        print("No alert present.")

def test_signup():
    # Set up the driver
    driver = setUp()
    
    # Generate a random username and password for testing
    username = generate_random_username()  # This will create a new unique username each time
    password = "Test@1234"  # Use a predefined password or generate it as needed
    
    try:
        signUp(driver, username, password)
    finally:
        time.sleep(2)  # Wait to see the result
        driver.quit()  # Close the browser after the test

if __name__ == "__main__":
    test_signup()
