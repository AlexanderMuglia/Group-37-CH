from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_flight_search():
    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Step 1: Navigate to the locally hosted webpage
        driver.get("http://127.0.0.1:5000")
        print("Opened site home page.")

        # Step 2: click the "Flight Search" link
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchFlightsLink"))).click()
        print("Clicked link to get to Flight Search page")

        # Step 3: Wait for the departure and arrival dropdowns to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "departure"))
        )
        print("Departure dropdown is loaded in the Flight Search page.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "arrival"))
        )
        print("Arrival dropdown is loaded in the Flight Search page.")


        # Step 4: Check if arrival codes and departure codes are in the page
        page_source = driver.page_source
        if "Select Departure Airport Code" in page_source:
            print("Select Departure Airport Code is in the page source")
        else:
            print("Select Departure Airport Code is not in the page source")

        if "Select Arrival Airport Code" in page_source:
            print("Select Arrival Airport Code is in the page source")
        else:
            print("Select Arrival Airport Code is not in the page source")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_flight_search()
