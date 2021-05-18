import time

from alpha import alpha
from pyrogram import filters
from pyrogram.types import Message


@alpha.on_message(filters.command("ping", ".") & filters.me)
async def ping(_, msg: Message):

    text = "**Pong!**"
    st = time.time()

    await msg.edit(text)

    et = time.time()
    text += f"\n`{et - st} ms`"

    await msg.edit(text)
