import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import time
from selenium.webdriver.common.by import By
from Utilities.base_utils import init_driver, login, take_screenshot

class TestPlaceOrder(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver
        self.driver = init_driver()
        self.driver.get("https://www.demoblaze.com")
        login(self.driver, "preetgogna12@gmail.com", "123456789")  # Replace with your test credentials
        time.sleep(2)

    def test_place_order(self):
        driver = self.driver

        # Step 1: Click on a product
        driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(2)

        # Step 2: Add product to cart
        driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
        time.sleep(2)

        # Handle alert after adding to cart
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)

        # Step 3: Go to cart
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)

        # Step 4: Click on Place Order
        driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        time.sleep(1)

        # Step 5: Fill order form
        driver.find_element(By.ID, "name").send_keys("Preet Gogna")
        driver.find_element(By.ID, "country").send_keys("India")
        driver.find_element(By.ID, "city").send_keys("Phagwara")
        driver.find_element(By.ID, "card").send_keys("1234567812345678")
        driver.find_element(By.ID, "month").send_keys("04")
        driver.find_element(By.ID, "year").send_keys("2025")

        # Step 6: Submit the order
        driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
        time.sleep(2)

        # Step 7: Confirm the order success message
        confirmation = driver.find_element(By.CLASS_NAME, "sweet-alert").text
        self.assertIn("Thank you", confirmation)

        take_screenshot(driver, "place_order_success.png")

    def tearDown(self):
        # Close the browser after test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
