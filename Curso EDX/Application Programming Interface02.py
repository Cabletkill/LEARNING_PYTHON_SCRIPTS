import pandas as pd
import numpy as np
import plotly.graph_objects as go

import datetime
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
type(bitcoin_data )

'''
The response we get is in the form of a JSON which includes the price, market caps, 
and total volumes along with timestamps for each observation. 
We are focused on the prices so we will select that data.
'''

bitcoin_price_data = bitcoin_data['prices']
bitcoin_price_data[5]

data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
'''
Now that we have the DataFrame we will convert the timestamp to datetime 
and save it as a column called Date. 
We will map our unix_to_datetime to each timestamp and convert it to a readable datetime.
'''
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})


fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()