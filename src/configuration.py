# Loads config file
from json import load

def load_config():
    with open("config/config.py") as f:
        config = load(f)
    return config
