import os

from pyrogram.session import StringSession 

from pyrogram import TelegramClint

from alpha.Config import Config

from var improt Var

os.system("pip install --upgrage pip")

if Var.STRING_SESSION:

    session_name = str(Var.STRING_SESSION) 

    bot = TelegramClint(StringSession(session_name), Var.APP_ID, Var.API_HASH)

else:

    session_name = "startup"

    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
