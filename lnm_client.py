from lnmarkets import rest
import datetime
from time import sleep, time
import logging
import json

logging.basicConfig(level=logging.INFO)


class lnm_client():
    # Connection to LN Markets API
    def __init__(self, options):
        self.options = options
        self.lnm = rest.LNMarketsRest(**self.options)

        if len(json.loads(self.lnm.get_user())) != 28:
            logging.warning('There is probably an error with your LN Markets credentials')
        else:
            logging.info('Connection to LN Markets ok!')
        

    def get_user(self):
        print(self.lnm.get_user())


    def market_long(self, quantity, leverage):
        params = {
            'type': 'm',
            'side': 'b',
            'quantity': quantity,
            'leverage': leverage
        }
        logging.info(datetime.datetime.fromtimestamp(time()))
        logging.warning('New Market Buy Running')

        return self.lnm.futures_new_position(params)

    def market_short(self, quantity, leverage):
        params = {
            'type': 'm',
            'side': 's',
            'quantity': quantity,
            'leverage': leverage
        }
        logging.info(datetime.datetime.fromtimestamp(time()))
        logging.warning('New Market Sell Running')
    
        return self.lnm.futures_new_position(params)


# options = {
#      'key': 'lQ9lfBrLfPAfraROW71zn2PETFj+k5d76tYVKBV2bQo=',
#      'secret': 'zCXP7RcwZLJn4he9WLaOj/giwqL7GmnZM8jy46ff9D8SDp2NxjeEK8XihPAbmfBWZdsGNZeyKPSWlczCP/DNAg==',
#      'passphrase': 'cihedje54g3f',
#      'network': 'testnet'}

# qty_per_order = 1 #type=int, min=1
# leverage = 10 #type=int, min=1, max=100

# lnm = lnm_client(options)

# lnm.market_long(quantity = qty_per_order, leverage = leverage)

# #lnm_client(options)