from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com")
#assert "Python" in driver.title

text = driver.find_elements(By.CLASS_NAME, "text")
author = driver.find_elements(By.CLASS_NAME, "author")

data = []

for t, a in zip(text, author):
    data.append({"Text":t.text, "Author":a.text})

df = pd.DataFrame(data)
df.to_csv("quotes.csv")

#elem = driver.find_element(By.CLASS_NAME, "q")
#elem.clear()
#elem.send_keys(Keys.RETURN)
#assert "No results found" not in driver.page_source


time.sleep(6)
driver.close()
