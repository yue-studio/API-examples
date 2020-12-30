#
# Using the investpy module to get stock quotes
#
# investpy is a Python package to retrieve data from Investing.com
#
# ref doc:
# https://pypi.org/project/investpy/
#
# Install the module if it is not the:
#    pip install investpy
#

import investpy
from datetime import datetime
from time import mktime

#
# Retrieves historical data of S&P 500 index
#
# *_date format is dd/mm/yyyy
#
df = investpy.get_index_historical_data(index='S&P 500', country='united states',
        from_date='01/12/2020', to_date=datetime.now().strftime("%d/%m/%Y"))

#
# Retrieves the historical data of AAPL
# *_date format is dd/mm/yyyy
#
df2 = investpy.get_stock_historical_data(stock='aapl', country='united states', 
        from_date='01/06/2020', to_date=datetime.now().strftime("%d/%m/%Y"))
