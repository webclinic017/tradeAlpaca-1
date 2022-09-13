position = 0
from HA import HAbars, HAbar

def decide(bar:HAbar):
    global position
    if position < 0:
        process_short(bar)
    elif position == 0:
        process_open(bar)
    else:
        process_long(bar)

def det_color(bar:HAbar) -> str:
    if bar.open < bar.close:
        return 'GREEN'
    if bar.open > bar.close:
        return 'RED'
    return 'YELLOW'

def process_short(bar:HAbar):
    c = det_color(bar)
    match c:
        case 'GREEN':
            print(c, bar.timestamp)
        case 'RED':
            print(c, bar.timestamp)
        case 'YELLOW':
            print(c, bar.timestamp)
        case other:
            raise Exception('short no color')

def process_open(bar:HAbar):
    c = det_color(bar)
    match c:
        case 'GREEN':
            print(c, bar)
        case 'RED':
            print(c, bar)
        case 'YELLOW':
            print(c, bar)
        case other:
            raise Exception('open no color')

def process_long(bar:HAbar):
    c = det_color(bar)
    match c:
        case 'GREEN':
            print(c, bar.timestamp)
        case 'RED':
            print(c, bar.timestamp)
        case 'YELLOW':
            print(c, bar.timestamp)
        case other:
            raise Exception('long no color')