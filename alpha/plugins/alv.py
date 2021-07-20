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

ALIVEE = (f"""
[✨]({config.BOT_PIC})
ʜᴇʟʟo {USERNAME} ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪs ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ 
<b>• ALPHA-X</b> vision→ <code> {ALPHA} </code>
<b>• Python</b> Vision→ <code> {PY} </code>
<b>• Sudo User</b>→ {config.SUDO_ENABLED} 
<b>•❤️My Master</b>❤️→ @{USERNAME}\n\n
||•|| Security by ALPHA-X ||•||
""",
disable_web_page_preview=False
)
ALIVE = f"""
ʜᴇʟʟo {USERNAME} ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪs ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ 
<b>• ALPHA-X</b> vision→ <code> {ALPHA} </code>
<b>• Python</b> Vision→ <code> {PY} </code>
<b>• Sudo User</b>→ {config.SUDO_ENABLED} 
<b>•❤️My Master</b>❤️→ @{USERNAME}\n\n
||•|| Security by ALPHA-X ||•||
"""

@alpha.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, msgg: Message):
      if BOT_PIC is True:
          await msgg.edit(ALIVEE)
      else:
          await msgg.edit(ALIVE)