# Get Ratios

from GetData import GetFinancials
from GetData import statistics
import pandas as pd


def calculate_ratio(data_Financials, key_stats):

    income_statement = data_Financials[0]  # Income statement of the company
    balance_sheet = data_Financials[1]  # Balance Sheet of the Company
    current_ratio = int(balance_sheet.loc[balance_sheet['Breakdown'] == 'Total Current Assets', 'Value']) \
                    / int(balance_sheet.loc[balance_sheet['Breakdown'] == 'Total Current Liabilities', 'Value'])
    debt_ratio = int(balance_sheet.loc[balance_sheet['Breakdown'] == 'Total Liabilities', 'Value'])\
                 / int(balance_sheet.loc[balance_sheet['Breakdown'] == 'Total Assets', 'Value'])
    debt_to_equity_ratio = float(key_stats.loc[key_stats['Name'] == 'Total Debt/Equity (mrq)', 'Value'])
    forward_pe_ratio = float(key_stats.loc[key_stats['Name'] == 'Forward P/E 1', 'Value'])
    price_to_sales = float(key_stats.loc[key_stats['Name'] == 'Price/Sales (ttm)', 'Value'])
    price_to_book = float(key_stats.loc[key_stats['Name'] == 'Price/Book (mrq)', 'Value'])
    operating_margin_ratio = (float(key_stats.loc[key_stats['Name'] == 'Operating Margin (ttm)', 'Value'])/100)
    net_profit_margin = int(income_statement.loc[income_statement['Breakdown'] == 'Net Income', 'Value']) \
                    / int(income_statement.loc[income_statement['Breakdown'] == 'Total Revenue', 'Value'])
    return_on_asset = (float(key_stats.loc[key_stats['Name'] == 'Return on Assets (ttm)', 'Value'])/100)
    return_on_equity = (float(key_stats.loc[key_stats['Name'] == 'Return on Equity (ttm)', 'Value'])/100)
    beta = float(key_stats.loc[9, 'Value'])

    # Creating a DataFrame with all values
    ratios_df = pd.DataFrame(
        [current_ratio, debt_ratio, debt_to_equity_ratio, operating_margin_ratio, net_profit_margin,
         return_on_asset, return_on_equity, forward_pe_ratio, price_to_sales, price_to_book, beta],
        index=['Current Ratio', 'Debt Ratio', 'Debt to Equity Ratio', 'Operating Margin', 'Net Profit Margin',
               'Return on Asset', 'Return on Equity', 'PE Ratio', 'Price to Sales', 'PB Ratio', 'Beta 5Y'],
        columns=["Ratio"]
    )
    return ratios_df


# Test Case
data_Financials = GetFinancials('NPI.TO')
key_stats = statistics('NPI.TO')
df = calculate_ratio(data_Financials, key_stats)
