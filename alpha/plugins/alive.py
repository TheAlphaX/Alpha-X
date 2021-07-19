import html
from alpha import alpha 
from pyrogram import filters
from pyrogram.types import Message
from alpha import config 
# config imports 

USERNAME = config.OWNER_USERNAME
ALIVE_PIC = config.ALIVE_PIC if config.ALIVE_PIC else None 


# here for later 
AL_TEXT = config.ALIVE_TEXT if config.ALIVE_TEXT else f"ʜᴇʟʟo {USERNAME} ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪs ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ"

ALIVE=f"""
❆ ᴀʟᴘʜᴀ ✗ ᴠɪsɪᴏɴ → `0.0.1`
❆ Pʏᴛʜᴏɴ Vɪsɪᴏɴ → `3.9.5`
❆ Sᴜᴅᴏ Usᴇr → {config.SUDO_ENABLED}
❆ Mʏ Mᴀsᴛᴇʀ → @{USERNAME}
||•|| Security by ALPHA-X ||•||
"""


@alpha.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, msg: Message):
      if ALIVE_PIC: 
        await msg.edit(ALIVE_PIC, AL_TEXT, ALIVE)
      else:
        await msg.edit(AL_TEXT, ALIVE)
        
# BY @Alone_loverboy 
# For Alpha-x
