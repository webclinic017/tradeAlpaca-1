from datetime import datetime, date, time, timedelta, timezone
from time import sleep

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, OrderStatus, TimeInForce

from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestBarRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame

apikey = 'PKKJZYB9P6Q36H84YMXF'
secretkey = 'hBnEAEiD1f67p6hM4DKkUBtixY01YulNWSuGHOyx'

trading_client = TradingClient(apikey, secretkey, paper=True)


def buy():
    global trading_client
    market_order_data = MarketOrderRequest(
        symbol="SPY",
        qty=1,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY
    )

    market_order = trading_client.submit_order(
        order_data=market_order_data
    )

    request_params = GetOrdersRequest(
        status=OrderStatus.NEW,
        side=OrderSide.BUY
    )

    sleep(1)
    orders = trading_client.get_orders()
    print(orders)


def sell():
    global trading_client
    market_order_data = MarketOrderRequest(
        symbol="SPY",
        qty=1,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.DAY
    )

    market_order = trading_client.submit_order(
        order_data=market_order_data
    )

    request_params = GetOrdersRequest(
        status=OrderStatus.NEW,
        side=OrderSide.SELL
    )

    orders = trading_client.get_orders(filter=request_params)
    print(orders)


def close_all_positions():
    global trading_client
    trading_client.close_all_positions(cancel_orders=True)


def get_positions():
    global trading_client
    return trading_client.get_all_positions()


# buy()
# print(get_positions())

close_all_positions()