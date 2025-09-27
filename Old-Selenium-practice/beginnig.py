
from selenium import webdriver

# create a Chrome browser instance
driver = webdriver.Chrome()

# open a webpage
driver.get("https://www.google.com")

print(driver.title)

driver.quit()
