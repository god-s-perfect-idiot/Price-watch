from bs4 import BeautifulSoup
import requests
import time

def checkprice(link,type):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    a = 1
    try:
        if(type=="Flipkart"):
            html_doc = requests.get(link, headers=headers).text
            soup = BeautifulSoup(html_doc,'html.parser')
            price_tag = soup.find("div", "_1vC4OE _3qQ9m1").text
            a = str(price_tag)[1:]
        else:
            html_doc = requests.get(link, headers=headers).text
            soup = BeautifulSoup(html_doc,'html.parser')
            price_tag = soup.find("span", "a-size-medium a-color-price priceBlockBuyingPriceString").text
            a = str(price_tag)[2:]
    except:
        pass

    return a
