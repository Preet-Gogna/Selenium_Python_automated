# TestScripts/test_login.py

"""
Test Case: Valid Login Test
Feature: User Authentication (Login)
Scenario: Verify login functionality with valid credentials
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utilities.base_utils import init_driver, login, logout, take_screenshot
from selenium.webdriver.common.by import By

def test_valid_login():
    # Step 1: Initialize driver
    driver = init_driver()
    test_result = "Fail"  # Default result

    try:
        # Step 2: Perform login using valid credentials
        login(driver, "preetgogna12@gmail.com", "123456789")  

        # Step 3: Check for successful login by checking Logout button visibility
        logout_button = driver.find_element(By.ID, "logout2")
        if logout_button.is_displayed():
            test_result = "Pass"
            print("Login Test Passed")
        else:
            print(" Login Test Failed")

        # Step 4: Capture screenshot for reference
        take_screenshot(driver, "login_success.png")

    except Exception as e:
        print(f" Exception during login test: {e}")
        take_screenshot(driver, "login_error.png")

    finally:
        # Step 5: Logout and close the browser
        logout(driver)
        driver.quit()
        return test_result

if __name__ == "__main__":
    result = test_valid_login()
    print(f"Test Result: {result}")
