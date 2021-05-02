from .client import alpha
from .config import Var
from pyrogram import filters

def _filter(_, __, m):
    return m.from_user and m.from_user.is_self

Owner_filter = filters.create(_filter)