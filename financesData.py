import pandas as pd
import quandl 
import time

#Quandl access key
quandl.ApiConfig.api_key = 'dgHj2ix2qxWUKwEgWvR9'

stockTicker = 'AAPL'
data = quandl.get_table('ZACKS/FC', ticker='AAPL')
data.head()
