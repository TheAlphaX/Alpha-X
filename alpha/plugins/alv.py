import re
import os
import asyncio
from pyrogram import filters

from pyrogram.types import Message
from typing import Tuple, Optional
from alpha import alpha 
from alpha import config
from alpha.plugins import ALPHA, PY


USERNAME = config.OWNER_USERNAME
BOT_PIC = config.BOT_PIC

ALIVEE = f"""
✨
ʜᴇʟʟo {USERNAME} ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪs ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ\n\n
<b>• ALPHA-X</b> vision→ <code> {ALPHA} </code>
<b>• Python</b> Vision→ <code> {PY} </code>
<b>• Sudo User</b>→ {config.SUDO_ENABLED} 
<b>•❤️My Master</b>❤️→ @{USERNAME}\n\n
||•|| Security by ALPHA-X ||•||
"""


ALIVE = f"""
ʜᴇʟʟo {USERNAME} ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪs ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ\n\n
<b>• ALPHA-X</b> vision→ <code> {ALPHA} </code>
<b>• Python</b> Vision→ <code> {PY} </code>
<b>• Sudo User</b>→ {config.SUDO_ENABLED} 
<b>•❤️My Master</b>❤️→ @{USERNAME}\n\n
||•|| Security by ALPHA-X ||•||
"""

@alpha.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, msgg: Message):
      if BOT_PIC:
          await msgg.edit_media(BOT_PIC, ALIVEE)
      else:
          await msgg.edit(ALIVE)
