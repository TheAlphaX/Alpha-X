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

# Scheduler
scheduler = AsyncIOScheduler()

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()
