# Web Scrapping Yahoo Finance

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver



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

    print(URL_Income)
    print(URL_CashFlow)
    print(URL_BalanceSheet)

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


def KeyStats(ticker):
    """
    :arg ticker from Yahoo Finance
    :return Main stats from Yahoo Finance
    """
    url_stats = "https://ca.finance.yahoo.com/quote/{0}/key-statistics?p={0}".format(ticker)
    url_main = "https://ca.finance.yahoo.com/quote/{0}/".format(ticker)

    key_stats_main = ['Market Cap', 'PE Ratio (TTM)', 'EPS(TTM', 'Beta (5Y Monthly)', 'Forward Dividend & Yield']
    key_stats_stats = ['Enterprise Value', 'Trailing P/E', 'Forward P/E', 'Price/Book (mrq)', 'Enterprise Value/EBITDA'
                       , 'Profit Margin', 'Operating Margin (ttm)', 'Return on Assets (ttm)', 'Return on Equity (ttm)'
                       , 'Quarterly Revenue Growth (yoy)', 'Forward Annual Dividend Rate', 'Payout Ratio']

    driver = webdriver.Chrome(r"C:\Users\Alex\Downloads\chromedriver_win32")

    driver.get(url_main)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(innerHTML, 'html.parser')
    for stat in key_stats_main:
        page_stat1 = soup.find(text=stat)
        try:
            page_row1 = page_stat1.find_parent('tr')
            try:
                page_statnum1 = page_row1.find_all('span')[1].contents[1]
            except:
                page_statnum1 = page_row1.find_all('td')[1].contents[0]
        except:
            print('Invalid parent for this element')
            page_statnum1 = "N/A"
        stock_info.append(page_statnum1)

    driver.get(url_stats)
    innerHTML2 = driver.execute_script("return document.body.innerHTML")
    soup2 = BeautifulSoup(innerHTML2, 'html.parser')
    for stat in key_stats_stats:
        page_stat2 = soup2.find(text=stat)
        try:
            page_row2 = page_stat2.find_parent('tr')
            try:
                page_statnum2 = page_row2.find_all('span')[1].contents[0]
            except:
                page_statnum2 = page_row2.find_all('td')[1].contents[0]
        except:
            print('Invalid parent for this element')
            page_statnum2 = "N/A"
        stock_info.append(page_statnum2)
    return(stock_info)


KeyStats('AAPL')


