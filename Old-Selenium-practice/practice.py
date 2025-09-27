# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import pandas as pd
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")

# elem = driver.find_element(By.NAME, 'q')
# elem.send_keys("Selenium Tutorial", Keys.RETURN)

# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME,"h3"))
# )
# result = driver.find_elements(By.TAG_NAME, "h3")

# d = []
# for e in result:
#     d.append(e.text)
# #print(d)
# df= pd.DataFrame(d)
# df.to_csv("test.csv")

# time.sleep(16)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.NAME, "username").send_keys("student")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(16)

m = driver.find_element(By.TAG_NAME, 'h1')

if m.text=="Logged In Successfully":
    print("Successful")
else:
    print("failed")



