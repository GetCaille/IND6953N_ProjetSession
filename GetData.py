# Web Scrapping Yahoo Finance

import requests
from bs4 import BeautifulSoup
import pandas_datareader as pdr
import pandas as pd


def StockData(ticker, start_date, end_date):
    """
    :param ticker: company's ticker
    :return: adjusted price, volatility, other stats
    """
    data_ticker = pdr.get_data_yahoo(ticker, start_date, end_date)
    df_price = pd.DataFrame (data_ticker)
    return df_price


def GetFinancials(ticker):
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

    # Data Cleaning
    income_statement = df_income.apply(lambda x: x.str.replace(',', ''))
    income_statement.rename(columns={list(income_statement)[1]: 'Value'}, inplace=True)
    balance_sheet = df_balance.apply(lambda x: x.str.replace(',', ''))
    balance_sheet.rename(columns={list(balance_sheet)[1]: 'Value'}, inplace=True)
    cash_flow = df_cs.apply(lambda x: x.str.replace(',', ''))
    cash_flow.rename(columns={list(cash_flow)[1]: 'Value'}, inplace=True)
    return income_statement, balance_sheet, cash_flow


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

    # Data cleaning

    clean_df = df.apply(lambda x: x.str.replace('%', ''))
    return clean_df

#  Test Case :
# date_format = 'YYYY-MM-DD'
# Data_NPI = StockData("NPI.TO", '2019-01-31', '2020-04-20')
# Financial_NPI = GetFinancials('NPI.TO')
Key_Statistics_NPI = statistics('NPI.TO')