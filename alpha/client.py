from alpha import config
from pyrogram import Client

alpha = Client(
    "Simple-Pyrogram-Bot",
    bot_token=config.TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    )



