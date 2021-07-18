from alpha import alpha
from pyrogram import filters
from pyrogram.types import Message
from alpha import config 

##### Config #####
USERNAME = config.OWNER_USERNAME
ALIVE_PIC = config.ALIVE_PIC if config.ALIVE_PIC else None 
ALIVE_TEXT = f"ʜᴇʟʟo {USERNAME} ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪs ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ😊"
##### Config Finished #####
## ALPHA-X 
### ALIVE PATTERN ### 
ALIVE = f"""
⎝⎝ALPHA-X ( ╹▽╹ ) ⎠⎠

❆ **ALPHA-X** ᴠɪsɪᴏɴ ➣ `0.0.1`
❆ **Python** ᴠɪsɪᴏɴ ➣ `3.9.5`
❆ **Your Security** ➠ __RUNNING PERFECTLY__
❆ **Plugins** ➠  __All Working well__
✗ sᴜᴅᴏ ᴜsᴇʀ ➾ {config.SUDO_USERS}
✗ ʀᴇᴘᴏsɪᴛᴏʀʏ ✨ ➾ [Alpha-X](https://github.com/TheAlphaX/Alpha-X) ✗

"""

@alpha.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, msg: Message):
  
      if ALIVE_PIC: 
        await msg.edit(ALIVE_PIC, ALIVE_TEXT, ALIVE),
        disable_web_page_preview=True
        
      else:
        await msg.edit(ALIVE_TEXT, ALIVE)
        disable_web_page_preview=True
