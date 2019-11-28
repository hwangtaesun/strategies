import requests

from .base_client import Client

class AlphaVantageClient(Client):

    def __init__(self, secret_key):
        super().__init__(secret_key)
        self.query = "https://www.alphavantage.co/query?"

    def get_time_series_intraday(self, ticker, interval):
        request = self.query + "function={function}&symbol={symbol}&interval={interval}&apikey={apikey}"
        return requests.get(
            request.format(function="TIME_SERIES_INTRADAY", \
                symbol=ticker, \
                interval=interval, \
                apikey=self.secret_key
            )
        )
