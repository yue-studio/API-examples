#
# Yahoo Finance APIs
#
#  They are still functional after Yahoo is gone but they are not being supported.
#  You can still find a lot of info by googling
#

import pandas as pd
import numpy as np
import requests
from datetime import datetime
from time import mktime

t = datetime.now()
unix_secs = mktime(t.timetuple())

# Get the historical quotes from Yahoo
url = 'https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=-1325635200&period2=' + str(int(unix_secs)) + '&interval=1d&events=history'

# spx = pd.read_csv("GSPC.csv",index_col=0, names = ['date', 'open', 'high', 'low', 'close', 'adj', 'volume'])
spx = pd.read_csv(url,index_col=0, names = ['date', 'open', 'high', 'low', 'close', 'adj', 'volume'])
spx = spx.iloc[1:]
spx['open'] = pd.to_numeric(spx['open'],errors='coerce')
spx['close'] = pd.to_numeric(spx['close'],errors='coerce')
spx['high'] = pd.to_numeric(spx['high'],errors='coerce')
spx['low'] = pd.to_numeric(spx['low'],errors='coerce')