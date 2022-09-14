position = 0
from HA import HAbars, HAbar
from buysell import go_long, go_short, close_long, close_short, close_long_go_short, close_short_go_long

def det_color(bar:HAbar) -> str:
    if bar.open < bar.close:
        return 'GREEN'
    if bar.open > bar.close:
        return 'RED'
    return 'YELLOW'

def decide(bar:HAbar):
    c = det_color(bar)
    match c:
        case 'GREEN':
            process_green(bar)
        case 'RED':
            process_red(bar)
        case 'YELLOW':
            process_yellow(bar)
        case other:
            raise Exception('Color Problem', 'c =', c)

def process_green(bar: HAbar):
    if position < 0:
        # close short and go long
        close_short_go_long()
    elif position == 0:
        # go long
        go_long()
    elif position > 0:
        # do nothing, stay long
        pass
    else:
        raise Exception("Position value problem")


def process_red(bar: HAbar):
    if position < 0:
        # do nothing, stay short
        pass
    elif position == 0:
        # go short
        go_short()
    elif position > 0:
        # close long and go short
        close_long_go_short()
    else:
        raise Exception("Position value problem")


def process_yellow(bar: HAbar):
    if position < 0:
        # close short
        close_short()
    elif position == 0:
        # stay zero position
        pass
    elif position > 0:
        # close long
        close_long()
    else:
        raise Exception("Position value problem")

