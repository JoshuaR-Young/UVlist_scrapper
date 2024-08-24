import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table.hover', {'tr': 'td'}) 
    
    if not table:
        return None 
    
    data = []
    rows = table.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    return data

#Start scraping from the first page
base_url = 'https://www.uvlist.net/gamesearch/?page={}'
current_page = 1
all_data = []

while True:
    url = base_url.format(current_page)
    print(f"Scraping page {current_page}: {url}")
    
    #Scrape the page and get the data
    page_data = scrape_page(url)
    
    if not page_data:  
        break
    
    all_data.extend(page_data)
    
    # Find if there is a next page link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_page = soup.find('a', {'class': 'next-page-class'})  
    
    if not next_page:
        break
    
    current_page += 1

#Save the data to a CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(all_data)

for row in all_data:
    print(row)
    
