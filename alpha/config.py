import os

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")
CUSTOM_ALIVE = os.environ.get("CUSTOM_ALIVE")
ALIVE_PIC = os.environ.get("ALIVE_PIC")
CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

