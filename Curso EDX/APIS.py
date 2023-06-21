'''
import pandas as pd
dict={'a':[11,21,31],
      'b':[12,22,32]}
df =pd.DataFrame(dict)
help(df)
'''
'''
import pandas as pd
dict_={'a':[11,21,31], 'b':[12,22,32]}
df=pd.DataFrame(dict_)
print(type(df))
print(df)
'''


import pandas as pd

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
type(bitcoin_data )
bitcoin_price_data = bitcoin_data['prices']
bitcoin_price_data[0:5]
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])