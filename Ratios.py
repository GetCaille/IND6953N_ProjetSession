# Get Ratios

from GetData import StockData
from GetData import GetFinancials
import datetime
import pandas as pd


data_Financials = GetFinancials('CAS.TO')
data_stock = StockData('CAS.TO', datetime.datetime(year=2017, month=1, day=1), datetime.datetime(year=2020, month=4, day=1))
income_statement = data_Financials[0]   # Income statement of the company
balance_sheet = data_Financials[1]  # Balance Sheet of the Company
cash_flow = data_Financials[2]  # Cash Flow of the Company

# Data Cleaning
income_statement = income_statement.apply(lambda x: x.str.replace(',', ''))
income_statement.rename(columns = {list(income_statement)[1]: 'Value'}, inplace = True)
balance_sheet = balance_sheet.apply(lambda x: x.str.replace(',', ''))
balance_sheet.rename(columns = {list(balance_sheet)[1]: 'Value'}, inplace = True)
cash_flow = cash_flow.apply(lambda x: x.str.replace(',', ''))
cash_flow.rename(columns = {list(cash_flow)[1]: 'Value'}, inplace = True)


# Liquidity Ratio & Leverage Ratio

current_ratio = int(balance_sheet.loc[8, 'Value'])/int(balance_sheet.loc[26, 'Value'])
debt_ratio = int(balance_sheet.loc[32, 'Value'])/int(balance_sheet.loc[19, 'Value'])
debt_to_equity_ratio = int(balance_sheet.loc[32, 'Value'])/int(balance_sheet.loc[37, 'Value'])


# Efficiency Ratio

asset_turnover_ratio = int(income_statement.loc[0, 'Value'])/int(balance_sheet.loc[19, 'Value'])
inventory_turnover_ratio = int(income_statement.loc[0, 'Value'])/int(balance_sheet.loc[19, 'Value'])

# Profitability

operating_margin_ratio = int(income_statement.loc[6, 'Value'])/int(income_statement.loc[0, 'Value'])
gross_margin_ratio = int(income_statement.loc[2, 'Value'])/int(income_statement.loc[0, 'Value'])
net_profit_margin = int(income_statement.loc[12, 'Value'])/int(income_statement.loc[0, 'Value'])
return_on_asset = int(income_statement.loc[12, 'Value'])/int(balance_sheet.loc[19, 'Value'])
return_on_equity = int(income_statement.loc[12, 'Value'])/int(balance_sheet.loc[37, 'Value'])

# Market Value Ratio
