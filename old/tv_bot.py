#https://github.com/brian-the-dev/python-tradingview-ta
#https://www.cryptomaton.org/2022/03/20/creating-a-ta-technical-analysis-crypto-trading-bot-for-binance-using-tradingview/
#https://python-tradingview-ta.readthedocs.io/en/latest/
#https://tvdb.brianthe.dev/
#https://tradingview.brianthe.dev/
#https://www.tradingview.com/symbols/XBTUSD/technicals/


from tradingview_ta import TA_Handler, Interval, Exchange
from lnmarkets import rest
import datetime
from time import sleep, time
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

options = {
    'key': 'lQ9lfBrLfPAfraROW71zn2PETFj+k5d76tYVKBV2bQo=',
    'secret': 'zCXP7RcwZLJn4he9WLaOj/giwqL7GmnZM8jy46ff9D8SDp2NxjeEK8XihPAbmfBWZdsGNZeyKPSWlczCP/DNAg==',
    'passphrase': 'cihedje54g3f',
    'network': 'testnet'}

lnm = rest.LNMarketsRest(**options)

print(lnm.futures_get_ticker())

symbol="XBTUSD"
screener="CRYPTO"
exchange="BITMEX"


def get_ta(symbol, screener, exchange):
    return TA_Handler(
    symbol=symbol,
    screener=screener,
    exchange=exchange,
    interval=Interval.INTERVAL_1_MINUTE,
    ).get_analysis().summary


#print(get_ta(symbol, screener, exchange))

frequency = 1 #type=int, seconds
qty_per_order = 1 #type=int, min=1
leverage = 10 #type=int, min=1, max=100

def market_long(quantity, leverage):
        params = {
            'type': 'm',
            'side': 'b',
            'quantity': quantity,
            'leverage': leverage
        }
        logging.info(datetime.datetime.fromtimestamp(time()))
        logging.warning('New Market Buy Running')
        return lnm.futures_new_position(params)

def market_short(quantity, leverage):
        params = {
            'type': 'm',
            'side': 's',
            'quantity': quantity,
            'leverage': leverage
        }
        logging.info(datetime.datetime.fromtimestamp(time()))
        logging.warning('New Market Sell Running')
        return lnm.futures_new_position(params)
        
#market_long(quantity = qty_per_order, leverage = leverage)

def main():
  while True:
    analysis = get_ta(symbol, screener, exchange)
    print(analysis)
 
    if 'BUY' in analysis['RECOMMENDATION']:
      print(f"Buying {symbol}")
      market_long(quantity = qty_per_order, leverage = leverage)
    elif 'SELL' in analysis['RECOMMENDATION']:
        print(f"Selling {symbol}")
        market_short(quantity = qty_per_order, leverage = leverage)
    sleep(frequency*60)

if __name__ == '__main__':
  main()