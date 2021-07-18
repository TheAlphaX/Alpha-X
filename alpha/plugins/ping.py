import time

from alpha import alpha
from pyrogram import filters
from pyrogram.types import Message
from alpha.config import config 

OWNER_USERNAME=config.OWNER_USERNAME

@alpha.on_message(filters.command("ping", ".") & filters.me)
async def ping(_, msg: Message):

    text = f"""
┏━━━┓━━━━━━━━━┓

┃┏━┓┃━━━━━━━━━┃

┃┗━┛┃━━┓━┓━━━┓┃

┃┏━━┛┏┓┃┏┓┓┏┓┃┛

┃┃━━━┗┛┃┃┃┃┗┛┃┓

┗┛━━━━━┛┛┗┛━┓┃┛

━━━━━━━━━━━━┛┃━

━━━━━━━━━━━━━┛━
__ALPHA-X__ is **ON!**ツ
•My Master→ {OWNER_USERNAME}
•Ms↓
"""
    st = time.time()

    await msg.edit(text)

    et = time.time()
    text += f"\n`{round((et - st), 3)} ms`"

    await msg.edit(text)
