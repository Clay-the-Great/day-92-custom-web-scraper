from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

# This is a custom web scraper that scrapes data off Goodreads to create book lists in CSV format.

service = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.goodreads.com/list/show/4808.Banned_CHINA_Books")
file_name = "scraped_data/banned_china_books.csv"
# driver.get("https://www.goodreads.com/list/show/157723.Food_Books_for_Readers_to_Devour_nonfiction_")
# file_name = "scraped_data/Food Books for Readers to Devour (nonfiction).csv"

csv_rows = []
rows = driver.find_elements(By.CSS_SELECTOR, "tr")
# print(type(rows))
for row in rows:
    csv_row = [
        row.find_element(By.CSS_SELECTOR, "tr .number").text,
        row.find_element(By.CSS_SELECTOR, "tr .bookTitle").text,
        row.find_element(By.CSS_SELECTOR, "tr .authorName span").text,
        row.find_element(By.CSS_SELECTOR, "tr .minirating").text.split("—")[0].strip().split(" ")[0],
        row.find_element(By.CSS_SELECTOR, "tr .minirating").text.split("—")[1].strip().split(" ")[0],
    ]
    csv_rows.append(csv_row)

fields = ["Ranking", "Title", "Author", "Rating", "Rates_number"]

with open(file_name, "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(csv_rows)
