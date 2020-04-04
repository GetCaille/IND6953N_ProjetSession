# Web Scrapping Yahoo Finance

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import yfinance as yf
import matplotlib.pyplot as plt


def GetPrice(ticker, start_date, end_date):
    """
    :param ticker: company's ticker
    :return: adjusted price, volatility, other stats
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    adj_close = data['Adj Close']
    adj_daily_yield = adj_close.pct_change(1)
    average_daily_yield = adj_daily_yield.mean()
    adj_periodic_yield = adj_close.pct_change(252)
    average_periodic_yield = adj_periodic_yield.mean()
    daily_yield_stddev = adj_daily_yield.std()
    plt.plot(adj_close)
    plt.title('Adjusted Close Price')
    plt.show()
    return average_daily_yield, average_periodic_yield, daily_yield_stddev


def GetData(ticker):
    """
    :arg ticker from Yahoo Finance
    :return Dataframe of Income Statement, Balance Sheets and Cash Flow
    """

    Base_URL = 'https://ca.finance.yahoo.com/quote/'
    cashflow = '/cash-flow/'
    income = '/financials/'
    balancesheet = '/balance-sheet/'

    URL_Income = Base_URL + ticker + income
    URL_CashFlow = Base_URL + ticker + cashflow
    URL_BalanceSheet = Base_URL + ticker + balancesheet

    page_income = requests.get(URL_Income)
    page_cashflow = requests.get(URL_CashFlow)
    page_balancesheet = requests.get(URL_BalanceSheet)

    soup_bs = BeautifulSoup(page_balancesheet.content, 'html.parser')
    soup_cf = BeautifulSoup(page_cashflow.content, 'html.parser')
    soup_in = BeautifulSoup(page_income.content, 'html.parser')

    # INCOME STATEMENT
    features = soup_in.find_all('div', class_='D(tbr)')
    headers = []
    temp_list = []
    label_list = []
    final = []
    index = 0
    #create headers
    for item in features[0].find_all('div', class_='D(ib)'):
        headers.append(item.text)
    #statement contents
    while index <= len(features)-1:
        #filter for each line of the statement
        temp = features[index].find_all('div', class_='D(tbc)')
        for line in temp:
            #each item adding to a temporary list
            temp_list.append(line.text)
        #temp_list added to final list
        final.append(temp_list)
        #clear temp_list
        temp_list = []
        index+=1
    df_income = pd.DataFrame(final[1:])
    df_income.columns = headers


    # BALANCE SHEET
    features = soup_bs.find_all('div', class_='D(tbr)')
    headers = []
    temp_list = []
    label_list = []
    final = []
    index = 0
    #create headers
    for item in features[0].find_all('div', class_='D(ib)'):
        headers.append(item.text)
    #statement contents
    while index <= len(features)-1:
        #filter for each line of the statement
        temp = features[index].find_all('div', class_='D(tbc)')
        for line in temp:
            #each item adding to a temporary list
            temp_list.append(line.text)
        #temp_list added to final list
        final.append(temp_list)
        #clear temp_list
        temp_list = []
        index+=1
    df_balance = pd.DataFrame(final[1:])
    df_balance.columns = headers


    # CASH FLOW
    features = soup_cf.find_all('div', class_='D(tbr)')
    headers = []
    temp_list = []
    label_list = []
    final = []
    index = 0
    #create headers
    for item in features[0].find_all('div', class_='D(ib)'):
        headers.append(item.text)
    #statement contents
    while index <= len(features)-1:
        #filter for each line of the statement
        temp = features[index].find_all('div', class_='D(tbc)')
        for line in temp:
            #each item adding to a temporary list
            temp_list.append(line.text)
        #temp_list added to final list
        final.append(temp_list)
        #clear temp_list
        temp_list = []
        index+=1
    df_cs = pd.DataFrame(final[1:])
    df_cs.columns = headers

    return df_balance, df_cs, df_income


def GetStats(ticker):
    pass


print(GetPrice('NPI.TO', datetime.datetime(year=2015, month=1, day=1), datetime.datetime(year=2020, month=4, day=1)))