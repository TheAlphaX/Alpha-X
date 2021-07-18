from alpha import Config
from pyrogram import Client

alpha = Client(
    session_name = Config.STRING_SESSION,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH,
    plugins={'root': 'alpha.plugins'}
)
