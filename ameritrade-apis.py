#
# TD Amertrade APIs
#
# ref doc: https://developer.tdameritrade.com/apis
#


import requests
import json
import datetime
import pytz

#key for the APIs
td_consumer_key = 'Put_your_API_key_here'

#
# function to get current stock quote
#
def getStockQuote(s):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'

    full_url = endpoint.format(stock_ticker=s)
    page = requests.get(url=full_url,
                    params={'apikey' : td_consumer_key})
    content = json.loads(page.content)

    return(content)
    
#
# get one month worth of daily quotes    
# 
def getHistQuote(s):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?&periodType={periodType}&period={period}&frequency={frequency}&frequencyType={frequencyType}'

    full_url = endpoint.format(stock_ticker=s,
        periodType = "month",
        period = 1,
        frequency = 1,
        frequencyType = "daily"
        )
    page = requests.get(url=full_url,
                    params={'apikey' : td_consumer_key})
    content = json.loads(page.content)

    return(content)
    
#
# test
#
list_of_stocks = ['AAPL', 'AMZN', 'FB', 'GOOG', 'GOOGL', 'MSFT','NFLX', 'NVDA']

for symbol in list_of_stocks: 
  content = getStockQuote(symbol)
  print(symbol, " ", content[symbol]['lastPrice'])