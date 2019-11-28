from configs.clients.iex_client import IEXClient
from configs.clients.alpha_vantage_client import AlphaVantageClient

from settings import CONFIG

def run_script():

    iex_client = IEXClient(CONFIG['iex']['secret_key'], CONFIG['iex']['public_key'])
    alpha_vantage_client = AlphaVantageClient(CONFIG['alpha']['secret_key'])


if __name__=='__main__':
    run_script()
