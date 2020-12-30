#
# Ally Bank (used to be called TradeKing) APIs
#
# ref docs:
# https://live.invest.ally.com/applications
#
# https://www.ally.com/api/invest/documentation/getting-started/
#
# part of the code is from 
# https://towardsdatascience.com/collect-stock-and-options-data-easily-using-python-and-ally-financial-api-3-example-queries-45d162e4f055
# I updated it for ally and I added a couple end points
#

import requests
from requests_oauthlib import OAuth1
import pandas as pd
import numpy as np
import datetime as dt

api_key = "put_you_key_here"
secret = "put_you_key_here"
oauth_token = "put_you_key_here"
oauth_secret = "put_you_key_here"

#authentication 
auth = OAuth1(api_key, secret, oauth_token, oauth_secret)

# url call to the api
url = 'https://devapi.invest.ally.com/v1/market/timesales.json?symbols=AAPL&startdate=2020-12-29&enddate=2020-12-30&interval=1min'

response = requests.get(url, auth = auth).json()

#send to data frame and format data types
df = pd.DataFrame(response["response"]["quotes"]["quote"])
df = df.sort_values(['datetime'], ascending = False)
df['date'] = pd.to_datetime(df['date'])
df['datetime'] = pd.to_datetime(df['datetime'],  utc=False).dt.tz_convert('US/Central')
df['hi'] = df["hi"].astype(float)
df['incr_vol'] = df["incr_vl"].astype(float)
df['last'] = df["last"].astype(float)
df['lo'] = df["lo"].astype(float)
df['opn'] = df["opn"].astype(float)
df['vl'] = df['vl'].astype(float)
df.head()

# url call to the api
url = 'https://devapi.invest.ally.com/v1/market/ext/quotes.xml?symbols=SPX&fids=ask,bid,cl'

response = requests.get(url, auth = auth)
for line in response.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        print(decoded_line)
        
# streaming quote
# url call to the api
url = 'https://devapi-stream.invest.ally.com/v1/market/quotes.xml?symbols=AAPL'

response = requests.get(url, auth = auth, stream=True)

for line in response.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print(decoded_line)