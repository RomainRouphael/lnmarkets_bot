from tradingview_ta import TA_Handler, Interval, Exchange
from lnm_client import lnm_client
from time import sleep
import json

class TAS():

  # Connection to LNMarkets API
  def __init__(self, options):
        self.options = options
        self.lnm = lnm_client(self.options)

  # Get trading signal from trading view https://www.tradingview.com/symbols/XBTUSD/technicals/
  def get_ta(symbol="XBTUSD", screener="CRYPTO", exchange="BITMEX", interval="1m"):
    interval_list = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1d", "1W", "1M"]
    ta_interval_list = ['Interval.INTERVAL_1_MINUTE',
                        'Interval.INTERVAL_5_MINUTES',
                        'Interval.INTERVAL_15_MINUTES',
                        'Interval.INTERVAL_30_MINUTES',
                        'Interval.INTERVAL_1_HOUR',
                        'Interval.INTERVAL_2_HOURS',
                        'Interval.INTERVAL_4_HOURS',
                        'Interval.INTERVAL_1_DAY',
                        'Interval.INTERVAL_1_WEEK',
                        'Interval.INTERVAL_1_MONTH']
    
    ta_interval = ta_interval_list[interval_list.index(interval)]
    
    return TA_Handler(
    symbol=symbol,
    screener=screener,
    exchange=exchange,
    interval=ta_interval,
    ).get_analysis().summary

  # Output can be a graph showing the evolution of your Balance during the strategy
  def ta_summary(self, quantity, leverage, interval): 
    symbol="XBTUSD"
    screener="CRYPTO"
    exchange="BITMEX"

    interval_list = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1d", "1W", "1M"]
    t_interval_list = [60, 300, 900, 1800, 3600, 7200, 14400, 86400, 604800, 2592000]
    t_interval = t_interval_list[interval_list.index(interval)]

    analysis = TAS.get_ta(symbol, screener, exchange, interval)
    print(analysis)
    if 'BUY' in analysis['RECOMMENDATION']:
      pos = 'long'
      pid = json.loads(self.lnm.market_long(quantity = quantity, leverage = leverage))['position']['pid']
    elif 'SELL' in analysis['RECOMMENDATION']:
      pos = 'short'
      pid = json.loads(self.lnm.market_short(quantity = quantity, leverage = leverage))['position']['pid']
    elif 'NEUTRAL' in analysis['RECOMMENDATION']:
      pos = 'neutral'
      pid = ''

    sleep(t_interval)

    while True:
      if pos == 'long':
        if 'SELL' in analysis['RECOMMENDATION']:
          self.lnm.close_position(pid)
          pos = 'short'
          pid = json.loads(self.lnm.market_short(quantity = quantity, leverage = leverage))['position']['pid']
        elif 'NEUTRAL' in analysis['RECOMMENDATION']:
          self.lnm.close_position(pid)
          pos = 'neutral'
          pid = ''
      elif pos == 'short':
        if 'BUY' in analysis['RECOMMENDATION']:
          self.lnm.close_position(pid)
          pos = 'long'
          pid = json.loads(self.lnm.market_long(quantity = quantity, leverage = leverage))['position']['pid'] 
        elif 'NEUTRAL' in analysis['RECOMMENDATION']:
          self.lnm.close_position(pid)
          pos = 'neutral'
          pid = ''
      elif pos == 'neutral':
        if 'BUY' in analysis['RECOMMENDATION']:
          pos = 'long'
          pid = json.loads(self.lnm.market_long(quantity = quantity, leverage = leverage))['position']['pid']
        elif 'SELL' in analysis['RECOMMENDATION']:
          pos = 'short'
          pid = json.loads(self.lnm.market_short(quantity = quantity, leverage = leverage))['position']['pid']
        elif 'NEUTRAL' in analysis['RECOMMENDATION']:
          pos = 'neutral'
          pid = ''
      
      sleep(t_interval)







