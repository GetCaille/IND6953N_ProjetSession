import requests
from bs4 import BeautifulSoup
import pandas as pd


def description(market, ticker):
    url_prefix = 'https://www.tradingview.com/symbols/'
    url = url_prefix + market.upper() + "-" + ticker.upper()
    print(url)
    page_stats = requests.get(url)
    soup = BeautifulSoup(page_stats.content, 'html.parser')
    desc = (soup.find('div',class_='tv-widget-description__text')).get_text()  # find company description
    return desc


print(description('tsx', 'NPI'))






# features = soup.find_all('div', class_='tv-widget-fundamentals__item') # finds valuation, price history, etc...