from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Update this path to the location of your ChromeDriver
CHROMEDRIVER_PATH = '/Users/karnank/Downloads/chromedriver-mac-arm64/chromedriver'

test_report = []

def log(message, passed):
    test_report.append(f"{'PASSED: ' if passed else 'FAILED: '}{message}")

def generate_report():
    with open("test_report.txt", "w") as file:
        for entry in test_report:
            file.write(entry + "\n")
    print("Test report generated successfully.")
    for entry in test_report:
        print(entry)

def main():
    options = Options()
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Open the website
        driver.get("https://theclubfactory.in/")
        time.sleep(3)
        log("Opened website", True)

        # 2. Click the login link
        driver.find_element(By.XPATH, "//a[@class='header__action-item-link hidden-pocket hidden-lap']").click()
        time.sleep(3)
        log("Clicked login link", True)

        # 3. Enter login credentials
        username_field = driver.find_element(By.ID, "customer[email]")
        password_field = driver.find_element(By.ID, "customer[password]")
        username_field.send_keys("karnank919@gmail.com")
        time.sleep(2)
        password_field.send_keys("9042737202")
        time.sleep(2)
        log("Entered login credentials", True)

        # 4. Click the login button
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        log("Clicked login button", True)

        # 5. Search for a product
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search...']")
        search_box.send_keys("watch")
        time.sleep(2)
        search_box.submit()
        time.sleep(3)
        log("Searched for 'watch'", True)

        # 6. Select a product from the search results
        product_link = driver.find_element(By.XPATH, "//a[contains(text(),'Smart Watch Series 7 | Logo Smart Watch | Infinity')]")
        if not product_link:
            log("Product not found", False)
            return
        product_link.click()
        time.sleep(3)
        log("Selected product", True)

        # 7. Increase the quantity of the selected product
        driver.find_element(By.XPATH, "//button[@title='Increase quantity by 1']").click()
        time.sleep(3)
        log("Increased quantity", True)

        # 8. Add the product to the cart
        driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()
        time.sleep(3)
        log("Added to cart", True)

        # 9. Proceed to the cart
        driver.find_element(By.XPATH, "//a[@class='button button--secondary']").click()
        time.sleep(3)
        log("Proceeded to cart", True)

        # 10. Click the checkout button
        driver.find_element(By.XPATH, "//button[@name='checkout']").click()
        time.sleep(3)
        log("Clicked checkout", True)

        # 11. Navigate to the home page
        home = driver.find_element(By.XPATH, "//a[@class='nav-bar__link link'][normalize-space()='Home']")
        home.click()
        time.sleep(3)
        log("Navigated to home", True)

        # 12. Navigate to the "All collections" page
        all_collection = driver.find_element(By.XPATH, "//a[@class='nav-bar__link link'][normalize-space()='All collections']")
        all_collection.click()
        time.sleep(3)
        log("Navigated to All collections", True)

        # 13. Navigate to a specific product category (e.g., Smart Watches)
        smart_watch = driver.find_element(By.XPATH, "//p[normalize-space()='Best Ever Smart Watches']")
        smart_watch.click()
        time.sleep(3)
        log("Navigated to Smart Watches category", True)

        # 14. Verify the presence of pagination
        pagination = driver.find_element(By.XPATH, "//a[@title='Navigate to page 2']")
        if pagination:
            log("Pagination is present", True)
        else:
            log("Pagination is not present", False)
        
        # 15. Navigate to the second page of the product list
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(3)
        page_two_link = driver.find_element(By.XPATH, "//a[@title='Navigate to page 2']")
        page_two_link.click()
        time.sleep(3)
        log("Navigated to page 2", True)

        # 16. Verify the presence of a specific product on the second page
        specific_product = driver.find_element(By.XPATH, "//a[contains(text(),'Smart Watch Series 7 | Logo Smart Watch | Infinity')]")
        if specific_product:
            log("Specific product is present on page 2", True)
        else:
            log("Specific product is not present on page 2", False)

        # 17. Click on a product image to view details
        product_image = driver.find_element(By.XPATH, "//a[@class='product-item__image']")
        product_image.click()
        time.sleep(3)
        log("Clicked on product image", True)

        # 18. Add the product to the cart from the product details page
        driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()
        time.sleep(3)
        log("Added product to cart from details page", True)

        # 19. Verify the cart total after adding a product
        cart_total = driver.find_element(By.XPATH, "//span[@class='cart-total']")
        if cart_total:
            log("Cart total verified", True)
        else:
            log("Cart total verification failed", False)

        # 20. Log out of the website
        logout_link = driver.find_element(By.XPATH, "//a[@class='header__action-item-link'][normalize-space()='Logout']")
        logout_link.click()
        time.sleep(3)
        log("Logged out", True)

    except Exception as e:
        log(f"Test failed: {e}", False)
        print(f"Test failed: {e}")

    finally:
        driver.quit()
        generate_report()

if __name__ == "__main__":
    main()
