import os

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")
CUSTOM_ALIVE = os.environ.get("CUSTOM_ALIVE")
ALIVE_PIC = os.environ.get("ALIVE_PIC")
CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID","0").split())
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUDO_ENABLED = False
SUDO_USERS: Set[int] = set()
DOWN_PATH = os.environ.get("DOWN_PATH")
U_BRANCH = "main"
UPSTREAM_REPO = os.environ.get(

        "UPSTREAM_REPO", "https://github.com/TheAlphaX/Alpha-x"

    )


            

