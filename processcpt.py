import requests
from bs4 import BeautifulSoup
import urllib.request
import time

url = input("Enter Amazon link:")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

#stockprice

realprice = soup.findAll('span', class_="priceBlockStrikePriceString a-text-strike")[0].text.strip()
sellingprice = soup.findAll('span', id='priceblock_dealprice')[0].text.strip()

onestars = soup.findAll('a', class_="a-link-normal 1star")[0]['title']

reviews = soup.findAll('div', class_='a-section review-views celwidget')
print(reviews)

print(sellingprice)
