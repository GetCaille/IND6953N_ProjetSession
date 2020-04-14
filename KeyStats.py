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

        df = pd.DataFrame(values)
    return df


statistics('NPI.TO')

