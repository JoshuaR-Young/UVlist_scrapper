from bs4 import BeautifulSoup
import requests

url = 'https://www.uvlist.not/gamesearch/'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(#table, {class: table-class-name})
