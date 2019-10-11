![paperswithcode.com logo](img/pwc.png)
# MLpaperz

Get the latest and trending in machine learning research from [paperswithcode.com](https://paperswithcode.com) right on telegram 🙂

Currently hosted at [MLpaperz](https://t.me/MLpaperz) on telegram.

This is a telegram bot which scrapes the latest and trending research work from [paperswithcode.com](https://paperswithcode.com) then uploads it to a telegram channel. The project was inspired from a conversation with a friend, I was talking to him about the latest paper release in NLP (at the time of writing) which is **roBERTa** and was surprised he hasn't heard about it. Then I asked him if he reads research papers and he said no because there's no way he could be checking research paper sites everyday for new releases and if there was a way he could be getting the updates on his phone it would be nice then I decided to create this to solve that problem.

**Star the repo if you like what you see 😉**

## Requirements
* Python 3
* An Operating System that supports Python (e.g Linux, Windows, MAC)
* A text editor (e.g Atom, VSCode)
* A Telegram account

## Setting Up
1. Install the project requirements. Instructions located in `requirements.txt`
2. Configure your project
   1. Rename `config-sample.json` file to `config.json` located in the config folder.
   2. Create your telegram bot from [`@botfather`](https://t.me/botfather) and create the channel or group you wish to receive updates on.
   3. Fill in your bot API token into the `bot_token` value in your config file.
   4. Fill in your telegram channel public name (for public channels) or channel || group chat_id (for private channels and groups) into the `channel_token` value in your config file.
   5. Set your `update_interval`, It is how many hours your bot will periodically check paperswithcode.com for updates. Setting a value of 1 means papers will be updated every hour.
   6. Set your `admin_id`, This is used to let the bot alert the admin each time it has completed scraping; However it is not compulsory and you can comment out the line that sends the alert from `main.py`
   7. Set your database name. This is the file containing previously viewed papers and it is in JSON format. The value can be `db.json` or `db/db.json` or whatever you please, Note the file does not need to exist when setting this up.
3. Run the `main.py` file. Or you can import it into another script and run it in cron mode; Make sure the bot is a member of the group or administrator on the channel; **Cron mode disables admin alerting, although you can reconfigure it to.**
```python
from main import main
# Do some other thing in your script
main(cron_mode=True)
```

## Current Progress
* [x] Scraping and Parsing Latest Research Papers
* [x] Scraping and Parsing Trending Research Papers
* [x] Setup telegram bot to send messages
* [x] Setup main.py
* [x] Setup hosting server

## TODO
* [ ] Design some dope logo instead of using paperswithcode logo
* [ ] Slack, Discord Bot Support

## Author(s)
* **LordGhostX** And a friend 

## Licence
[**MIT**](https://opensource.org/licenses/MIT)

