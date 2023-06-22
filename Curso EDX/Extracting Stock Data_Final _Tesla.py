import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup as bts
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


#Question 1: Use yfinance to Extract Stock Data
tesla = yf.Ticker("TSLA")#function ticker extract data on to create a ticker object.
print(tesla)
tesla_data = tesla.history(period="max")#extract stock information and save it in a dataframe
print(tesla_data)
print()
tesla_data.reset_index(inplace=True)#function display the first five rows
#print(tesla_data.head())

#Question 2: Use Webscraping to Extract Tesla Revenue Data
html_data = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01"
data  = requests.get(html_data).text
soup = bts ( data, "html5lib")#Analysis of html data using beautiful_soup
read_html_tesla_data = pd.read_html(str(soup))
tesla_revenue = read_html_tesla_data[1]
tesla_revenue.columns = ['Date', 'Revenue']

#tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
print(tesla_revenue.tail())





