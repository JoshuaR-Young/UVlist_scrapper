from bs4 import BeautifulSoup
import pandas
import requests
import time

#Get website data
def get_game_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Extract required info
    data = []
    rows = soup.find_all('tr', class_='row')
    for row in rows:
        title = row.find('td', class_='title').text.strip()
        year = row.find('td', class_='title').text.strip()
        genre = row.find('td', class_='title').text.strip()
        platform = row.find('td', class_='title').text.strip()
        data.append({'Title': title, 'Year': year, 'Genre': genre, 'Platform': platform}) 
