from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# Function to wait for the visibility of an element
def wait_for_visibility(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

# Function to click on an element
def click_element(driver, locator, timeout=10):
    element = wait_for_visibility(driver, locator, timeout)
    element.click()

# Configuring the Chrome service and options
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")  # Disable notifications
options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

# Creating an instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Opening Google
    driver.get("https://google.com")

    # Waiting for the search field to be visible
    search = wait_for_visibility(driver, (By.NAME, 'q'))

    # Entering the search text
    search.send_keys("Universidad Carlos III de Madrid")

    # Performing the search by pressing Enter
    search.submit()

    # Waiting for the Wikipedia link to be visible
    wikipedia_link = wait_for_visibility(driver, (By.XPATH, "//a[contains(@href, 'wikipedia.org')]"))

    # Clicking on the Wikipedia link
    wikipedia_link.click()

    # Waiting for the search field on Wikipedia to be visible
    search_bar_wiki = wait_for_visibility(driver, (By.ID, 'searchInput'))

    # Entering the search text on Wikipedia
    search_bar_wiki.send_keys("Universidad Carlos III de Madrid")

    # Locating and clicking on the second search result directly
    click_element(driver, (By.XPATH, "//a[contains(@href, '/w/index.php?title=Special%3ASearch&fulltext=1&search=Universidad+Carlos+III+de+Madrid')]"))


    # Find the number of references to “Universidad Carlos III de Madrid” in Wikipedia
    numb = driver.find_element(By.XPATH, '//*[@id="mw-search-top-table"]/div[2]/strong[2]')
    # Print in terminal the number of references to “Universidad Carlos III de Madrid”
    print(f'1) There are {numb.text} results on the Wikipedia for the term "Universidad Carlos III de Madrid"')
    sleep(2)

    # ----- PART 2 ----

    # Navigating back to the Wikipedia homepage
    driver.back()

    # Waiting for the Wikipedia homepage to be fully loaded
    wait_for_visibility(driver, (By.ID, 'content'))

    # Find the number of students in Universidad Carlos III de Madrid in Wikipedia
    students = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[16]/td')

    # Print in terminal the number of students in “Universidad Carlos III de Madrid”
    print(f'2) The Universidad Carlos III de Madrid had aproximately {students.text} students in 2020/2021')
    sleep(2)

    # Waiting for some time to view the page
    #input("Press Enter to close the browser...")


finally:
    # Closing the browser
    driver.quit()
