'''
posts = [
    [
        n,
        link,
        auth,
        date,
        type,
        rel
    ]
]
'''

import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import numpy as np
import datetime as dt

results = []
csv_file = "incca-links02.csv" 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()

posts = []

with open(csv_file) as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        if row[4] != "N":

            driver.get(row[1])
            
            # DATE form web
            date_text = driver.find_element(By.CLASS_NAME, "field--name-created").text
            date = dt.datetime(
                int(date_text [11]+date_text [12]+date_text [13]+date_text [14]), # year
                int(date_text[5]+date_text[6]),
                1
            )

            # AUTH form web
            try:
                auth_text = driver.find_element(By.CLASS_NAME, "profile__name").text
            except:
                auth_text = ""

            auth = auth_text

            # TYPE from CSV
            if len(row[2])>0:
                if row[2] == "PROJECT":
                    type = "ENTITY"
                if row[2] == "ORGANIZATION":
                    type = "ENTITY"
                if row[2] == "ARCHIVE":
                    type = "ENTITY"
                if row[2] == "MODEL":
                    type = "ENTITY"
                if row[2] == "CONFERENCE":
                    type = "EVENT"
                if row[2] == "SYMPOSIUM":
                    type = "EVENT"
                if row[2] == "SUMMIT":
                    type = "EVENT"
                if row[2] == "EXHIBITION":
                    type = "EVENT"
                if row[2] == "WORKSHOP":
                    type = "EVENT"
                if row[2] == "SEMINAR":
                    type = "EVENT"
                if row[2] == "ARTICLE":
                    type = "PUBLICATION"
                if row[2] == "BOOK":
                    type = "PUBLICATION"
                if row[2] == "THESIS":
                    type = "PUBLICATION"
                if row[2] == "PROGRAM":
                    type = row[2]
                if row[2] == "CALL":
                    type = row[2]
                if row[2] == "OTHER":
                    type = row[2]
            else: 
                type = ""

            posts.append([row[1], auth, date, type, row[3]])

with open('incca-postreview.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["n", "link", "auth", "date", "type", "rel"]
    
    for i in range(len(posts)):
        writer.writerow([str(i), posts[i][0], posts[i][1], posts[i][2], posts[i][3], posts[i][4]])