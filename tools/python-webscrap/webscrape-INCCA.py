from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome()

keywords = [
    "document", 
    "archiv",
    "preserv",
    "conserv",
    "restor",
    "reactivat",
    "collecti",
]

links = []
n_pages = 2 

research = True

for k in range(len(keywords)):
    current_page = 0
    research = True
    while research:
        url = "https://incca.org/search?search_api_fulltext="+keywords[k]+"&f[0]=content_type%3Apost&page="+str(current_page)
        driver.get(url)
        # get results number info
        text_results = driver.find_element(By.CLASS_NAME, "view-header").text
        info_results = [int(s) for s in re.findall(r'\b\d+\b', text_results)] # [first, last, tot]
        # print(info_results)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('article')
        print(search)
        if info_results[1]<info_results[2]:
            current_page += 1
            for h in search:
                new_link = "https://incca.org"+h.a.get('href')
                if new_link in links:
                    pass
                else:
                    links.append(new_link)
        else:
            research = False

print(len(links))

with open('INCCA-links-arts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["n", "link"]

    for i in range(len(links)):
        writer.writerow([str(i), links[i]])




