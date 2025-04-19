# Import necessary libraries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from Utilities.base_utils import init_driver, login, logout, take_screenshot
from selenium.webdriver.common.by import By
import time

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        """
        Set up the browser and login with valid credentials.
        """
        self.driver = init_driver()
        self.driver.get("https://www.demoblaze.com/")
        login(self.driver, "preetgogna12@gmail.com", "123456789")  # You can change the user if needed

    def test_add_product_to_cart(self):
        """
        Test: Add a laptop product to the cart and verify success.
        """
        driver = self.driver

        # Navigate to 'Laptops' category
        driver.find_element(By.LINK_TEXT, "Laptops").click()
        time.sleep(2)

        # Select 'Sony vaio i5' product
        driver.find_element(By.LINK_TEXT, "Sony vaio i5").click()
        time.sleep(2)

        # Click 'Add to cart' button
        driver.find_element(By.LINK_TEXT, "Add to cart").click()
        time.sleep(2)

        # Handle confirmation alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()

        # Capture screenshot for verification
        take_screenshot(driver, "add_to_cart_success.png")

        # Assert that the alert confirms addition to cart
        self.assertIn("Product", alert_text or "added", "Product not added to cart!")

    def tearDown(self):
        """
        Logout and close the browser session.
        """
        logout(self.driver)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
