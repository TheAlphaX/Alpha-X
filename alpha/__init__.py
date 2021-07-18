import ast
import logging
import os
from configparser import ConfigParser
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from alpha.alpha import Alpha

# Created logs folder if it is not there. Needed for logging.
if not os.path.exists('logs'):
    os.makedirs('logs')

# Logging at the start to catch everything
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.WARNING,
    handlers=[
        TimedRotatingFileHandler(
            "logs/userbot.log",
            when="midnight",
            encoding=None,
            delay=False,
            backupCount=10,
        ),
        logging.StreamHandler(),
    ],
)
LOGS = logging.getLogger(__name__)

# Extra details
__version__ = "0.0.1"
__author__ = "Alpha"

Alpha = Alpha(__version__)

# Read from config file
config_file = 'alpha.ini'
config = ConfigParser()
config.read(config_file)

API_ID = config.get("API_ID")
API_HASH = config.get("API_HASH") 
LOG_CHANNEL = config.get("LOG_CHANNEL")
STRING_SESSION = config.get("STRING_SESSION")
CUSTOM_ALIVE = config.get("CUSTOM_ALIVE")
ALIVE_PIC = config.get("ALIVE_PIC")
CMD_HNDLR = config.get("CMD_HNDLR", r"\.")
HEROKU_API_KEY = config.get("HEROKU_API_KEY")
HEROKU_APP_NAME = config.get("HEROKU_APP_NAME")
OWNER_ID = set(int(x) for x in config.get("OWNER_ID","0").split())
OWNER_USERNAME = config.get("OWNER_USERNAME")
BOT_TOKEN = config.get("BOT_TOKEN")
SUDO_ENABLED = False 
SUDO_USERS: config.get("SUDO_USERS", None)
DOWN_PATH = config.get("DOWN_PATH")
ALIVE_TEXT = config.get("ALIVE_TEXT")

        

# Scheduler
scheduler = AsyncIOScheduler()

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()
