import time
from seleniumwire import webdriver  # For request interception
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Chrome options
chrome_options = webdriver.ChromeOptions()


# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to click elements by XPath
def click_element(xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

# Function to type text into elements by XPath
def type_in_element(xpath, text):
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)

# Open the website
driver.get('https://m.snappfood.org/')
time.sleep(5)

# Click on select map
click_element('/html/body/div[2]/div[1]/div/div/div[2]/button')
time.sleep(2)

# Click on login button in the bottom menu
click_element('/html/body/div[1]/div[3]/div')
time.sleep(0.5)

# Click on register button
click_element('/html/body/div[1]/div[4]/div/div/div[3]/button')
time.sleep(0.5)

# Click on mobile input field
click_element('/html/body/div[1]/div[2]/section/div[1]/div[3]/div[1]/input')
time.sleep(0.5)

# Type mobile number into input field
type_in_element('/html/body/div[1]/div[2]/section/div[1]/div[3]/div[1]/input', '09000000')
time.sleep(10)

# Close the browser
driver.quit()
