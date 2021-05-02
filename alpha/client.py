from alpha import Var
from pyrogram import Client

alpha = Client(
    session_name=Var.STRING_SESSION,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH
)