from alpaca.data.models.bars import Bar
from datetime import datetime

class HAbar:
    def __init__(self, t:datetime, o:float, h:float, l, c ):
        self.timestamp = t
        self.open = o
        self.high = h
        self.low = l
        self.close = c

    def __str__(self):
        s = "{}, {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(
            self.timestamp.strftime("%H:%M:%S"), self.open, self.high, self.low, self.close
        )
        return s

class HAbars:
    def __init__(self) -> None:
        self.bars = []

    def add(self, bar:Bar) -> HAbar:
        t = bar.timestamp
        o = bar.open
        h = bar.high
        l = bar.low
        c = bar.close

        if len(self.bars) == 0:
            thisbar = HAbar(t,o,h,l,c)
        else:
            prevbar = self.bars[-1]
            ht = t
            ho = (prevbar.open + prevbar.close) / 2
            hc = (o + h + l + c) / 4
            hh = max(h, ho, hc)
            hl = min(l, ho, hc)
            thisbar = HAbar(ht, ho, hh, hl, hc)
        self.bars.append(thisbar)
        return thisbar
