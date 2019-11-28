import configparser
import os

def get_config():

    config_directory = os.path.join(os.path.dirname(__file__), 'configs')

    if os.path.isfile(os.path.join(config_directory, 'strategies.cfg')):
        return os.path.join(config_directory, 'strategies.cfg')
    else:
        return os.path.join(config_directory, 'default_strategies.cfg')

CONFIG = configparser.ConfigParser()
config_file = get_config()
CONFIG.read(config_file)
