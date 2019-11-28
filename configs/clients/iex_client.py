import requests, os

from iexfinance.account import get_metadata
from iexfinance.stocks import Stock
from .base_client import Client

class IEXClient(Client):

    def __init__(self, secret_key, public_key):
        super().__init__(secret_key)
        self.public_key = public_key

    @property
    def metadata():
        return get_metadata()


    def get_stock_by_ticker(self, ticker):
        return Stock(ticker, token=self.secret_key)
