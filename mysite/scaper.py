from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

url = 'https://foxi.ro/articol/citate-celebre'
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
html =  urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

quotes = []

for ol in soup.find_all('ol'):
    for li in ol.find_all('li'):
        try:
            autor = li.find('strong').extract().text
            quote = li.text
        except AttributeError:
            autor = 'Autor necunoscut'
        if autor != 'Autor necunoscut':
            quote = quote[:-3]
        quotes.append({'autor':autor,'text':quote})
with open('citate.json','w') as json_file:
    json.dump(quotes,json_file)
