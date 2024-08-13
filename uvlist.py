from bs4 import BeautifulSoup
import pandas
import requests
import sqlite3

page_to_scrape = requests.get('https://www.uvlist.net/gamesearch/')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
uv_row = soup.find_all('tr')

for row in uv_row:
    cells = uv_row.find_all('td')
    cell_text = [cell.get_text(strip=True) for cell in cells]
