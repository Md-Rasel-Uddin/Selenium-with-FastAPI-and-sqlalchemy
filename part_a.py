from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
#import pandas as pd
import json

import argparse

from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin

#sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


# --- Argparse setup ---
parser = argparse.ArgumentParser(description="Quotes-Scrapping")
parser.add_argument("--pages", type=int, default=3, help="Number of pages to scrape")
parser.add_argument("--db", type=str, default="mydatabase.db", help="Database file name")
args = parser.parse_args()



user_agent = "MyScraperBot/1.0"  


chrome_options = Options()
chrome_options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(options=chrome_options)
base_url = "http://quotes.toscrape.com"
driver.get(base_url)

#robot.txt

# Set up robots.txt parser
robots_url = urljoin(base_url, "/robots.txt")
rp = RobotFileParser()
rp.set_url(robots_url)
rp.read()



results = []
#pages = 3

for i in range(1, args.pages + 1):
    url = f"{base_url}/page/{i}/"

    # Before visiting a page:
    page_url = f"{base_url}/page/{i}/"
    if not rp.can_fetch(user_agent, page_url):
        print(f"Skipping {page_url} due to robots.txt")
        continue   

    driver.get(url)
    time.sleep(1)  # allow page to load

    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for q in quotes:
        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text
        tags = [t.text for t in q.find_elements(By.CLASS_NAME, "tag")]
        results.append({
            "title": text,         # using quote text as title
            "url": driver.current_url,
            "category": ", ".join(tags) if tags else None,
            "author": author
        })

driver.quit()



engine = create_engine(f"sqlite:///{args.db}", echo=True)

Base = declarative_base()

class Quote(Base):
    __tablename__ = "scrapedresources"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    category = Column(String)
    author = Column(String)

    def __repr__(self):
        return f"Quote(id={self.id}, title={self.title}, url = {self.url}, category = {self.category}, author = {self.author})"

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session

with Session(engine) as session:
    for r in results:
        quote = Quote(
            title=r["title"],
            url=r["url"],
            category=r["category"],
            author=r["author"]
        )
        session.add(quote)
    session.commit()


#json file

with open("out.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

print(f"Scraped {len(results)} quotes into {args.db} and saved to out.json")


