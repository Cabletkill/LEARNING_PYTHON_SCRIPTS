import yfinance as yf
import pandas as pd

AMD = yf.Ticker("AMD")
print(AMD)
AMD_info=AMD.info
print(AMD_info, end=' ')

country= AMD_info['country']


print()
print(country)
AMD_share_price_data = AMD.history(volume="trading")
print(AMD_share_price_data)

price= AMD_share_price_data.head()

print(price)