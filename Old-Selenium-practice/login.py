from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

un = driver.find_element(By.NAME, "username")
un.send_keys("student")
pasw = driver.find_element(By.NAME, "password")
pasw.send_keys("Password123")

sub = driver.find_element(By.CLASS_NAME, "btn")
sub.click()

time.sleep(6)

check = driver.find_element(By.TAG_NAME, 'h1')
txt = check.text

if "Logged In Successfully" in txt:
    print("Successful")
else:
    print("Not Successful")


driver.quit()



#Use next credentials to execute Login:
#Username: student
#Password: Password123
