import requests

from iexfinance.account import get_metadata

from base_client import Client

class IEXClient(Client):

    def __init__(self):
        super()

    @property
    def metadata():
        return get_metadata()
