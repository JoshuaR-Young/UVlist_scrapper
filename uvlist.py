from bs4 import BeautifulSoup
import requests

url = 'https://www.uvlist.not/gamesearch/'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(#table, {class: table-class-name})

data = []
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

#display the data
for row in data:
    print(row)
    
