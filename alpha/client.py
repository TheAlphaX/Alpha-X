from alpha import config
from pyrogram import Client

pm = Client(
    "PM-BoT",
    bot_token=config.TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    )



