from tradingview_ta import TA_Handler, Interval, Exchange
from lnm_client import lnm_client
from time import sleep

class TAS():

  # Connection to LNMarkets API
  def __init__(self, options):
        print(options)
        self.options = options
        self.lnm = lnm_client(self.options)

  # Get trading signal from trading view
  def get_ta(symbol="XBTUSD", screener="CRYPTO", exchange="BITMEX"):
    return TA_Handler(
    symbol=symbol,
    screener=screener,
    exchange=exchange,
    interval=Interval.INTERVAL_1_MINUTE,
    ).get_analysis().summary

  # Output can be a graph showing the evolution of your Balance during the strategy
  def ta_summary(self, qty_per_order, leverage, interval):
    while True: 
      symbol="XBTUSD"
      screener="CRYPTO"
      exchange="BITMEX"
      analysis = TAS.get_ta(symbol, screener, exchange)
      print(analysis)
  
      if 'BUY' in analysis['RECOMMENDATION']:
        print(f"Buying {symbol}")
        self.lnm.market_long(quantity = qty_per_order, leverage = leverage)
      elif 'SELL' in analysis['RECOMMENDATION']:
          print(f"Selling {symbol}")
          self.lnm.market_short(quantity = qty_per_order, leverage = leverage)
      sleep(interval)







