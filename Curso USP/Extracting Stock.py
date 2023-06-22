import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")
apple_info=apple.info

print(apple_info)

apple_info['55']

apple_share_price_data = apple.history(period="max")

apple_share_price_data.head()