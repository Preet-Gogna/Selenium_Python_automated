import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import time
from selenium.webdriver.common.by import By
from Utilities.base_utils import init_driver, take_screenshot

class TestContactUs(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver
        self.driver = init_driver()
        self.driver.get("https://www.demoblaze.com")
        time.sleep(2)

    def test_contact_us_form_submission(self):
        driver = self.driver

        # Step 1: Click on "Contact" to open the modal
        contact_button = driver.find_element(By.XPATH, "//a[text()='Contact']")
        contact_button.click()
        time.sleep(2)

        # Step 2: Fill in the contact form
        driver.find_element(By.ID, "recipient-email").send_keys("preetgogna12@gmail.com")
        driver.find_element(By.ID, "recipient-name").send_keys("Preet Gogna")
        driver.find_element(By.ID, "message-text").send_keys("i want to buy galaxy s8 when it will be in stock ?")
        time.sleep(1)

        # Step 3: Click on "Send message"
        send_btn = driver.find_element(By.XPATH, "//button[text()='Send message']")
        send_btn.click()
        time.sleep(2)

        # Step 4: Handle and verify the alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        self.assertIn("Thanks", alert_text or "successful", "Alert message is unexpected.")
        alert.accept()

        # Step 5: Take a screenshot of the homepage after submission
        take_screenshot(driver, "contact_us_submission.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
