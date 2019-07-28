# Handling the scraper database which is used to know what we have scraped before or not
from json import load, dumps
from os.path import exists
import configuration
from time import time

class DB():
    def __init__(self):
        config = configuration.load_config()
        self.dbName = config["database_name"]

    def readDB(self):
        # Reads the database content
        if exists(self.dbName):
            with open(self.dbName) as f:
                db = load(f)
        else:
            db = {"server": {"start_date": int(time())}, "latest_research": [], "trending_research": []}
        return db

    def writeDB(self, data, indent=4):
        # Writes content to the database
        with open(self.dbName, "w") as f:
            f.write(dumps(data, indent=indent))

    def remove_duplicates(self, old, new):
        # Removes duplicates; This essentially makes sure that the resulting list elements are not members of the old list
        return list(set(new) - set(old))
