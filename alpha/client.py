from alpha import config
from pyrogram import Client

alpha = Client(

    session_name=config.STRING_SESSION,

    api_id=config.API_ID,

    api_hash=config.API_HASH,

    plugins={'root': 'alpha.plugins'}

)



