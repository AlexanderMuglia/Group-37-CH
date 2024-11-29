from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_view_flights():
    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Step 1: Navigate to Google
        driver.get("http://127.0.0.1:5000")
        print("Opened site home page.")

        # Step 2: click the "View Flights" link
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "viewFlightsLink"))).click()
        print("Clicked link to get to Flight Viewing page")

        # Step 3: Wait for results
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "table"))
        )
        print("Table loaded in the View Flight page")

        # Step 4: Check if "Apple Watch" is mentioned on the page
        page_source = driver.page_source
        if "YYZ" in page_source:
            print("YYZ is in the page source")
        else:
            print("YYZ is not in the page source")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_view_flights()
