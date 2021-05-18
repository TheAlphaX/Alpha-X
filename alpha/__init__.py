from pyrogram import filters
from .client import alpha

def _filter(_, __, m):
    return m.from_user and m.from_user.is_self

Ownerfilter = filters.create(_filter)
