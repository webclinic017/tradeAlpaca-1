from datetime import datetime, date, time, timedelta, timezone
from time import sleep

from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestBarRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame

from HA import HAbars, HAbar

apikey = 'PKW1HQ47CUXALPRYOB3N'
secretkey = 'oGCX75TffItL75ydY4id0jRGZvg6ZVebvU5S5LgA'

# create utc start of day time
today = date(2022,9,9)
start_time = datetime.combine(today,time(13, 30))
end_time = datetime.combine(today,time(13, 45) )

print('start_time', start_time)
print('end_time', end_time)

stock_hist_client = StockHistoricalDataClient(apikey, secretkey)

#
# current_time = datetime.datetime.utcnow()
# current_time.hour = 14
# current_time.min = 30
# current_time.second = 0
#
# print(current_time)
# today = datetime.date.today()
# print(today)

# habars = HAbars()

#get bars up to the current time
request_params = StockBarsRequest(\
    symbol_or_symbols='SPY',
    timeframe=TimeFrame.Minute,
    start=start_time,
    end = end_time
)

bars = stock_hist_client.get_stock_bars(request_params)['SPY']
for x in bars:
    print(x)