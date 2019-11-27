import os

# Base class for all API clients
class Client:

    def __init__(self):
        self.public_key = os.environ.get('IEX_PUBLIC_KEY')
        self.secret_key = os.environ.get('IEX_SECRET_KEY')
