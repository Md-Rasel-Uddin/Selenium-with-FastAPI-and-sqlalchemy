
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com//")

elem = driver.find_element(By.NAME, "q")
#elem.clear()
elem.send_keys("Python Selenium tutorial" ,Keys.RETURN)
#elem.click()

titles = driver.find_elements(By.TAG_NAME, "h3")
for i in titles:
    print(i.text)

time.sleep(16)
driver.quit()
