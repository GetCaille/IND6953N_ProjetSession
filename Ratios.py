# Get Ratios

from GetData import StockData
from GetData import GetFinancials
import datetime
import pandas as pd


data_Financials = GetFinancials('NPI.TO')
data_stock = StockData('NPI.TO', datetime.datetime(year=2017, month=1, day=1), datetime.datetime(year=2020, month=4, day=1))
income_statement = data_Financials[0]   # Income statement of the company
balance_sheet = data_Financials[1]  # Balance Sheet of the Company
cash_flow = data_Financials[2]  # Cash Flow of the Company

# Data Cleaning
income_statement = income_statement.apply(lambda x: x.str.replace(',', ''))
balance_sheet = balance_sheet.apply(lambda x: x.str.replace(',', ''))
cash_flow = cash_flow.apply(lambda x: x.str.replace(',', ''))


# Liquidity Ratio

current_ratio = int(balance_sheet.loc[8, '2019-12-31'])/int(balance_sheet.loc[26,'2019-12-31'])
debt_ratio = int(balance_sheet.loc[32, '2019-12-31'])/int(balance_sheet.loc[19,'2019-12-31'])
debt_to_equity_ratio = int(balance_sheet.loc[32, '2019-12-31'])/int(balance_sheet.loc[37,'2019-12-31'])








