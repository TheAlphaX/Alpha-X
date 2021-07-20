import html
from alpha import alpha 
from pyrogram import filters
from pyrogram.types import Message
from alpha import config 
from alpha.plugins import ALPHA, PY

# config imports 

USERNAME = config.OWNER_USERNAME
BOT_PIC = config.BOT_PIC if config.BOT_PIC else None 


# here for later 
AL_TEXT = config.ALIVE_TEXT if config.ALIVE_TEXT else f"ʜᴇʟʟo {USERNAME} ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪs ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ"

ALIVE=f"""
<b>• ALPHA-X</b> vision→ <code> {ALPHA} </code>
<b>• Python</b> Vision→ <code> {PY} </code>
<b>• Sudo User</b>→ {config.SUDO_ENABLED} 
<b>•❤️My Master</b>❤️→ @{USERNAME} 

||•|| Security by ALPHA-X ||•||
"""



@alpha.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, msg: Message):
      if ALIVE_PIC: 
        await msg.edit(BOT_PIC, AL_TEXT, ALIVE)
      else:
        await msg.edit(AL_TEXT, ALIVE)
        
# BY @Alone_loverboy 
# For Alpha-x
