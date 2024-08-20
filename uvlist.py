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

current_page = 1
while True:
    url = f'https://www.uvlist.net/gamesearch/?page={current_page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table-class-name'})

    next_page = soup.find('a', {'class': 'next-page-class'})  # Replace with actual class or id
    if not next_page:
        break
    current_page += 1

for row in data:
    print(row)
    
