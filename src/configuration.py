# Loads config file
from json import load

def load_config():
    with open("config/config.json") as f:
        config = load(f)
    return config
