import pandas as pd
import quandl as ql


# quandl access key

my_API_Key = 'xabkmqmf7HNaU9rv3Mz9'


ql.ApiConfig.api_key = my_API_Key

stockTicker = 'AAPL'
data = ql.get_table('ZACKS/FC', ticker='AAPL')
data.head()


