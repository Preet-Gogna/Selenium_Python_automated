# Utilities/base_utils.py
""" This file contains common reusable functions that are used across multiple test scripts. 
Instead of repeating the same Selenium code (like logging in, launching browser, taking screenshots) in every .py file,
 we Write once in base_utils.py and Import and reuse in every test script"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

def init_driver(headless=False):
    """Initialize and return a Selenium Chrome WebDriver."""
    options = Options()
    if headless:
        options.add_argument("--headless")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def take_screenshot(driver, filename):
     """
    Takes a screenshot of the current page and saves it in the 'Screenshots' folder.
    The filename is provided as an argument."""
     folder_path = os.path.join(os.getcwd(), 'Screenshots')# path to save screenshots
     os.makedirs(folder_path, exist_ok=True) #ensuring screenshot folder exixts , if not create new
     filepath = os.path.join(folder_path, filename)
     driver.save_screenshot(filepath) 

def login(driver, username, password):
    """Reusable login function."""
    """
    Logs into the Demoblaze website with the provided username and password.
    The login form is found by ID and the user credentials are input into the form.
    Then the login button is clicked to submit the form.
    """
    driver.get("https://www.demoblaze.com")
    time.sleep(2)
    driver.find_element(By.ID, "login2").click()
    time.sleep(2) #to wait for login form to load 
    driver.find_element(By.ID, "loginusername").send_keys(username) #username input into form
    driver.find_element(By.ID, "loginpassword").send_keys(password) #password input into form
    driver.find_element(By.XPATH, "//button[text()='Log in']").click() # clicking login buttn to submit form
    time.sleep(3)

def logout(driver):
    """Reusable logout function."""
    """
    Logs out from the Demoblaze website.
    This function will check for the 'logout' button and click it to perform a logout.
    """
    try:
        driver.find_element(By.ID, "logout2").click()# finding and clicking logout button if user is logged in 
        time.sleep(2)
    except:
         #If the logout button is not found, it means the user is already logged out
        pass 
