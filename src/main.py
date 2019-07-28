# Main Scraper code
# Run this to start the bot

from bot import Telegram
from db import DB
import scraper
import configuration
import time

# Print MLpaperz Banner
print("""
███╗   ███╗██╗     ██████╗  █████╗ ██████╗ ███████╗██████╗ ███████╗
████╗ ████║██║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══███╔╝
██╔████╔██║██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝  ███╔╝
██║╚██╔╝██║██║     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗ ███╔╝
██║ ╚═╝ ██║███████╗██║     ██║  ██║██║     ███████╗██║  ██║███████╗
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝
""")

# Setup database handler and get database content
db_handler = DB()
db = db_handler.readDB()

# Setup telegram client
bot = Telegram()

update_interval = float(configuration.load_config()["update_interval"]) * 60 * 60

while True:
    # Get the latest and trending research
    latest_data = scraper.get_latest()
    trending_data = scraper.get_trending()

    # Remove duplicates so we don't send papers we have sent before
    latest_data = db_handler.remove_duplicates(db["latest_research"], latest_data)
    trending_data = db_handler.remove_duplicates(db["trending_research"], trending_data)

    # Get full paper info
    latest_papers = scraper.parse_papers(latest_data, "new")
    trending_papers = scraper.parse_papers(trending_data, "trending")

    # format paper info and send to Telegram
    for paper in latest_papers + trending_papers:
        abstract = paper["abstract"]
        abstract = " ".join(abstract.split())
        message = """{}

{}

URL - {}
{}
{}

Code Implementation - {}

#{} @MLpaperz""".format(paper["title"], abstract, paper["url"], paper["abstract link 1"], paper["abstract link 2"], paper["code"], paper["tag"])
        bot.sendMessage(message)

    # update database
    db["latest_research"] = db["latest_research"] + latest_data
    db["trending_research"] = db["trending_research"] + trending_data
    db_handler.writeDB(db)

    # Sleep till next interval
    time.sleep(update_interval)
