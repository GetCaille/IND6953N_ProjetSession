import requests
from bs4 import BeautifulSoup
import pandas as pd


def statistics(ticker):
    url = 'https://ca.finance.yahoo.com/quote/' + str(ticker) + '/key-statistics?p=' + str(ticker)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    features = soup.find_all('tr', class_='Bxz(bb)')

    labels = []
    values = []
    for item in features:
        label = (item.find('td', class_='Pos(st)')).get_text()
        value = (item.find('td', class_='Fw(500)')).get_text()
        labels.append(label)
        values.append(value)
        data = list(zip(labels, values))
    df = pd.DataFrame(data, columns=['Name', 'Value'])
    df
    return df


df = statistics('NPI.TO')
forward_pe_ratio = float(df.loc[3, 'Value'])
price_to_sales = float(df.loc[5, 'Value'])
price_to_book = float(df.loc[6, 'Value'])

