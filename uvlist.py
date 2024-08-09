from bs4 import BeautifulSoup
import pandas
import requests
import time
import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections

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
