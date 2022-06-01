from tradingview_ta import TA_Handler, Interval, Exchange
from time import time, sleep
from lnm_client import lnm_client
import os
import yaml
import logging

logging.basicConfig(level=logging.INFO)

def load_yaml(file):
    with open(file) as file:
      load = yaml.load(file, Loader=yaml.FullLoader)
    return load

yaml_file = load_yaml(os.path.join(os.path.dirname(__file__), "configuration.yml"))

lnm_options = yaml_file['lnm_credentials']
config = yaml_file['ta_summary']

logging.basicConfig(level=logging.INFO)

symbol="XBTUSD"
screener="CRYPTO"
exchange="BITMEX"

lnm = lnm_client(lnm_options)

def get_ta(symbol, screener, exchange):
    return TA_Handler(
    symbol=symbol,
    screener=screener,
    exchange=exchange,
    interval=Interval.INTERVAL_1_MINUTE,
    ).get_analysis().summary

def main():
  while True:
    analysis = get_ta(symbol, screener, exchange)
    print(analysis)
 
    if 'BUY' in analysis['RECOMMENDATION']:
      print(f"Buying {symbol}")
      lnm.market_long(quantity = config['qty_per_order'], leverage = config['leverage'])
    elif 'SELL' in analysis['RECOMMENDATION']:
        print(f"Selling {symbol}")
        lnm.market_short(quantity = config['qty_per_order'], leverage = config['leverage'])
    sleep(config['interval'])

if __name__ == '__main__':
  main()

