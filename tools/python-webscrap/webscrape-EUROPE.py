from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import csv
import time
import requests


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
n_pages = 124 

research = True
current_page = 91

titles = []
descriptions = []
objectives = []
links = []

pn = ((current_page-1)*50)

while current_page<125:
    url = "https://cordis.europa.eu/search?q=contenttype%3D%27project%27%20AND%20(%27preserv%27%20AND%20%27conserv%27%20AND%20%27document%27%20AND%20%27collect%27%20AND%20%27archiv%27%20AND%20%27restor%27%20AND%20%27react%27%20AND%20%27media%27%20AND%20%27time-based%27%20AND%20%27multimedia%27%20AND%20%27media-based%27%20AND%20%27performance%27%20AND%20%27audiovisual%27%20AND%20%27virtual%27%20AND%20%27born-digital%27%20AND%20%27digital%27%20AND%20%27computer-based%27%20AND%20%27contemporary%27%20AND%20%27modern%27)&p="+str(current_page)+"&num=50&srt=Relevance:decreasing&archived=true"
    # response = requests.get(url)
    driver.get(url)
    time.sleep(10)

    #Use XPATH to find the apx-root tag
    apx_root = driver.find_element(By.XPATH, '/html/body/app-root')
    page_inner_HTML = apx_root.get_attribute("innerHTML")
    soup = BeautifulSoup(page_inner_HTML, 'html.parser')
    search = soup.find_all('app-card-search')
    if (len(search)<1):
        print("ERR: page "+str(current_page))
    for h in search:
        print(pn)
        add = False
        project_url = "https://cordis.europa.eu"+h.a.get('href')
        driver.get(project_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # TITLE
        project_title_TEXT = soup.find_all("title")[0].getText()
        # DESCRIPTION
        project_description = soup.find_all("p", {"class": "c-project-description__text"})
        project_description_TEXT = ""
        if len(project_description)>0:
            project_description_TEXT = project_description[0].getText()
            if any(x in project_description_TEXT for x in keywords):
                add=True

        # OBJECTVE
        project_objective = soup.find_all("p", {"class": "c-article__text"})
        project_objective_TEXT = ""
        if len(project_objective)>0:
            project_objective_TEXT = project_objective[0].getText()
            if any(x in project_objective_TEXT for x in keywords):
                add=True

        # IF FOUND ANY KEYWORD ADD TO THE ARRAYS
        if add==True:
            titles.append(project_title_TEXT)
            objectives.append(project_objective_TEXT)
            descriptions.append(project_description_TEXT)
            links.append(project_url)

        pn+=1
    
    current_page += 1

with open('EUROPE-related-project_91-124.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["n", "title", "objective", "description", "link" ]

    for i in range(len(links)):
        ii = i
        writer.writerow([str(ii), titles[i], objectives[i], descriptions[i], links[i]])