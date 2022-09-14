from datetime import datetime, date, time, timedelta, timezone
from time import sleep
from plot import candlePlot

import pytz
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestBarRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame

from HA import HAbars, HAbar
from decision import decide

apikey = 'PKKJZYB9P6Q36H84YMXF'
secretkey = 'hBnEAEiD1f67p6hM4DKkUBtixY01YulNWSuGHOyx'

# create utc start of day time
eastern = pytz.timezone('America/New_York')
utc = pytz.utc

today = date(2022,9,13)
nyc_start_time = eastern.localize(datetime.combine(today,time(9, 30)))
nyc_end_time = eastern.localize(datetime.combine(today,time(16, 00)))
utc_start_time = nyc_start_time.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S")
utc_end_time = nyc_end_time.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S")

stock_hist_client = StockHistoricalDataClient(apikey, secretkey)

habars = HAbars()

#get bars up to the current time
request_params = StockBarsRequest(
    symbol_or_symbols='SPY',
    timeframe=TimeFrame.Minute,
    start = utc_start_time,
    end = utc_end_time
)

bars = stock_hist_client.get_stock_bars(request_params)['SPY']

for bar in bars:
    b = habars.add(bar)
    decide(b)

from plot import candlePlot
candlePlot(habars.bars)