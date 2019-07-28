# Handling the scraper database which is used to know what we have scraped before or not
from json import load, dumps
import configuration

class DB():
    def __init__(self):
        config = configuration.load_config()
        self.dbName = config["database name"]

    def readDB(self):
        # Reads the database content
        with open(self.dbName) as f:
            db = load(f)
        return db

    def writeDB(self, data, indent=4):
        # Writes content to the database
        with open(self.dbName, "w") as f:
            f.write(dumps(data, indent=indent))

    def remove_duplicates(self, old, new):
        # Removes duplicates; This essentially makes sure that the resulting list elements are not members of the old list
        return list(set(new) - set(old))
