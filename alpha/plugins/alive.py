import time

from datetime import datetime

import os

import re

import asyncio 

import requests

from io import BytesIO

from pyrogram import filters, Message

from alpha import alpha, Config

CUSTOM_ALIVE = (

Config.CUSTOM_ALIVE

    if Config.CUSTOM_ALIVE

    else "ʜᴇʟʟᴏ ᴍᴀsᴛᴇʀ. ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜ"

)

ALV_PIC = ( 

  

    Config.ALIVE_PIC 

    if Config.ALIVE_PIC 

    else "https://telegra.ph/file/175ce47b80ddb44d87cb9.mp4"

    

)

if Config.SUDO_USERS:

    sudo = "Enabled"

else:

    sudo = "Disabled"

    

@alpha.on_cmd("alive", "." & filters.me)

async def alive(Message): 

    start = datetime.now()

    end = datetime.now()

    (end - start).microseconds / 1000

    uptime = get_readable_time((time.time()))

    

    if ALV_PIC:

       ALIVE_TEXT = f"""

      `{CUSTOM_ALIVE}`

 ❆ **ALPHA-X vision** ➛ `0.0.1`

 ❆ **Python vision** ➛  `3.8.9`

 ❆ **SUDO user** ➛ `{Config.SUDO_USERS}`

 ❆ **YOUR SECURITY** ➛ `running perfectly`

 ❆ **All functions working** ➛  EXCELLENT..!

  

  ⎝⎝𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 ɮʏ [𝗔𝗟𝗣𝗛𝗔-𝗫](https://t.me/Alphaxupdates) ⎠⎠

  """

    await alive.get_chat()

    await alive.delete()

    await borg.send_file(alive.chat_id, ALV_PIC, ALIVE_TEXT, link_preview=False)

        

    await alive.delete()

    return

    req = requests.get("https://telegra.ph/file/175ce47b80ddb44d87cb9.mp4")

    req.raise_for_status()

    file = BytesIO(req.content)

    file.seek(0)

    img = Image.open(file)

    await borg.send_message(

            alive.chat_id,

            

            f"""

       `{CUSTOM_ALIVE}`

 ❆ **ALPHA-X vision** ➛ `0.0.1`

 ❆ **Python vision** ➛  `3.8.9`

 ❆ **SUDO user** ➛ `{Config.SUDO_ENABLED}`

 ❆ **YOUR SECURITY** ➛ `running perfectly`

 ❆ **All functions working** ➛  EXCELLENT..!

  

  ⎝⎝𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 ɮʏ [𝗔𝗟𝗣𝗛𝗔-𝗫](https://t.me/Alphaxupdates) ⎠⎠

  """

  )

  

    await borg.send_file(alive.chat_id, file="https://telegra.ph/file/175ce47b80ddb44d87cb9.mp4")

    await alive.delete()
