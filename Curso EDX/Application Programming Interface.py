import pandas as pd
#import numpy as np
#import plotly.graph_objects as go
#from plotly.offline import plot
#import matplotlib.pyplot as plt
#import datetime
#from pycoingecko import CoinGeckoAPI
#from mplfinance.original_flavor import candlestick2_ohlc

dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
type(df)

print(df)
print()
print(df.head())
print()
print(df.mean())#When you call mean,the API will calculate the mean and return the value.