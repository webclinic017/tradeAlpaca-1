
import plotly.graph_objects as go
import pandas as pd

def candlePlot(bars):
    df = pd.DataFrame()
    df['Date'] = [b.timestamp for b in bars]
    df['open'] = [b.open for b in bars]
    df['high'] = [b.high for b in bars]
    df['low'] = [b.low for b in bars]
    df['close'] = [b.close for b in bars]

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])

    fig.show()