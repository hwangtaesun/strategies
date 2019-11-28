import os

# Base class for all API clients
class Client:

    def __init__(self, secret_key):
        self.secret_key = secret_key
