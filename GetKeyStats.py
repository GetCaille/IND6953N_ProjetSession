import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
driver = webdriver.Chrome()


def description(market, ticker):
    url_prefix = 'https://www.tradingview.com/symbols/'
    url = url_prefix + market.upper() + "-" + ticker.upper()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    desc = (soup.find('div',class_='tv-widget-description__text')).get_text()  # find company description
    return desc