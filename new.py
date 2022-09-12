apikey = 'PKW1HQ47CUXALPRYOB3N'
secretkey = 'oGCX75TffItL75ydY4id0jRGZvg6ZVebvU5S5LgA'

from datetime import datetime
from time import sleep
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestBarRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from HA import HAbars

trading_client = TradingClient(apikey, secretkey, paper=True)
stock_hist_client = StockHistoricalDataClient(apikey, secretkey)

# spy_latest_request = StockLatestBarRequest(symbol_or_symbols='SPY')


# bar = stock_hist_client.get_stock_latest_bar(spy_latest_request)['SPY']
# print(bar.timestamp.strftime("%H:%M:%S"),bar.open, bar.high, bar.low, bar.close)
# print()
# print(HA(bar))

# lasttime = bar.timestamp
# for i in range(60):
#     bar = stock_client.get_stock_latest_bar(spy_latest_request)['SPY']
#     if bar.timestamp == lasttime:
#         lasttime = bar.timestamp
#         sleep(1)
#         print('-', end="")
#     else:
#         print()
#         print('now = ', datetime.now().strftime("%H:%M:%S"))
#         print(bar.timestamp.strftime("%H:%M:%S"),bar.open, bar.high, bar.low, bar.close)
#         break
#
request_params = StockBarsRequest(
    symbol_or_symbols='SPY',
    timeframe=TimeFrame.Minute,
    start="2022-09-09 13:30"
)
print(request_params)

# ha = HAbars()

bars = stock_hist_client.get_stock_bars(request_params)['SPY']
for x in bars:
    print(x.timestamp.strftime("%H:%M:%S"), x.open, x.high, x.low, x.close)
    lastHAbar = ha.add(x)
    print(ha.add(lastHAbar))
    diff = lastHAbar.close - lastHAbar.open
    if abs(diff) <= 0.02:
        print('SPINNING TOP')
    elif lastHAbar.open > lastHAbar.close:
        print('RED')
    else:
        print('GREEN')
