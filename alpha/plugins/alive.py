import re
import os
import asyncio
import wget

from typing import Tuple, Optional
from alpha import alpha, Message, Config
from pyrogram.errors import (
    ChatSendMediaForbidden, Forbidden, SlowmodeWait, PeerIdInvalid,
    FileIdInvalid, FileReferenceEmpty, BadRequest, ChannelInvalid, MediaEmpty
)

_IS_TELEGRAPH = False
_IS_STICKER = False

_DEFAULT_PIC = "https://telegra.ph/file/175ce47b80ddb44d87cb9.mp4"
_CHAT, _MSG_ID = None, None
_LOGO_ID = None

@alpha.on_cmd("alive", about={
    'header': "This is to check userbot"}, allow_channels=False)
async def alive(message: Message):
    if not (_CHAT and _MSG_ID):
        try:
            _set_data()
        except Exception as set_err:
            _LOG.exception("There was some problem while setting Media Data."
                           f"trying again... ERROR:: {set_err} ::")
            _set_data(True)

    alive_text, markup = _get_alive_text_and_markup(message)
    if _MSG_ID == "text_format":
        return await message.edit(alive_text, disable_web_page_preview=True, reply_markup=markup)
    await message.delete()
    try:
        await _send_alive(message, alive_text, markup)
    except (FileIdInvalid, FileReferenceEmpty, BadRequest):
        await _refresh_id(message)
        await _send_alive(message, alive_text, markup)


def _get_mode() -> str:
    if userge.dual_mode:
        return "Dual"
    if Config.BOT_TOKEN:
        return "Bot"
    return "User"


def _get_alive_text_and_markup(message: Message) -> Tuple[str, Optional[InlineKeyboardMarkup]]:
    markup = None
    output = f"""
    ʜᴇʟʟᴏ ᴍᴀsᴛᴇʀ. ᴛʜɪs ɪs ᴀʟᴘʜᴀ-x ɪɴ ʏᴏᴜʀ sᴇʀᴠɪᴄᴇ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ʏᴏu😗
    
 ❆ **ALPHA-X vision** ➛ `0.0.1`
 ❆ **Python vision** ➛  `3.8.9`
 ❆ **SUDO user** ➛  `{_parse_arg(Config.SUDO_ENABLED)}`
 ❆ **YOUR SECURITY** ➛ `running perfectly`
 ❆ **All functions working** ➛  EXCELLENT..!
  
  ⎝⎝ 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 ɮʏ [𝗔𝗟𝗣𝗛𝗔-𝗫](https://t.me/AlphaXupdates) ⎠⎠
 """
 
 def _parse_arg(arg: bool) -> str:
    return "enabled" if arg else "disabled"


async def _send_alive(message: Message,
                      text: str,
                      reply_markup:
                      recurs_count: int = 0) -> None:
    if not _LOGO_ID:
        await _refresh_id(message)
    should_mark = None if _IS_STICKER else reply_markup
    if _IS_TELEGRAPH:
        await _send_telegraph(message, text, reply_markup)
    else:
        try:
            await message.client.send_cached_media(chat_id=message.chat.id,
                                                   file_id=_LOGO_ID,
                                                   caption=text,
                                                   reply_markup=should_mark)
            if _IS_STICKER:
                raise ChatSendMediaForbidden
        except SlowmodeWait as s_m:
            await asyncio.sleep(s_m.x)
            text = f'<b>{str(s_m).replace(" is ", " was ")}</b>\n\n{text}'
            return await _send_alive(message, text, reply_markup)
        except MediaEmpty:
            if recurs_count >= 2:
                raise ChatSendMediaForbidden
            await _refresh_id(message)
            return await _send_alive(message, text, reply_markup, recurs_count + 1)
        except (ChatSendMediaForbidden, Forbidden):
            await message.client.send_message(chat_id=message.chat.id,
                                              text=text,
                                              disable_web_page_preview=True,
                                              reply_markup=should_mark)


async def _refresh_id(message: Message) -> None:
    global _LOGO_ID, _IS_STICKER  # pylint: disable=global-statement
    try:
        media = await message.client.get_messages(_CHAT, _MSG_ID)
    except (ChannelInvalid, PeerIdInvalid, ValueError):
        _set_data(True)
        return await _refresh_id(message)
    else:
        if media.sticker:
            _IS_STICKER = True
        _LOGO_ID = get_file_id_of_media(media)


def _set_data(errored: bool = False) -> None:
    global _CHAT, _MSG_ID, _IS_TELEGRAPH  # pylint: disable=global-statement

    pattern = r"^https://telegra\.ph/file/\w+\.\w+$"
    if Config.ALIVE_PIC and not errored:
        if Config.ALIVE_PIC.lower().strip() == "nothing":
            _CHAT = "text_format"
            _MSG_ID = "text_format"
            return
        media_link = Config.ALIVE_PIC
        match = re.search(pattern, media_link)
        elif match:
            _IS_TELEGRAPH = True
        elif "|" in Config.ALIVE_PIC:
            _CHAT, _MSG_ID = Config.ALIVE_PIC.split("|", maxsplit=1)
            _CHAT = _CHAT.strip()
            _MSG_ID = int(_MSG_ID.strip())
    else:
        match = re.search(pattern, _DEFAULT_PIC)
        _CHAT = match.group(6)
        _MSG_ID = int(match.group(7))


async def _send_telegraph(msg: Message, text: str, reply_markup:
    path = os.path.join(Config.DOWN_PATH, os.path.split(Config.ALIVE_PIC)[1])
    if not os.path.exists(path):
        await pool.run_in_thread(wget.download)(Config.ALIVE_PIC, path)
    if path.lower().endswith((".jpg", ".jpeg", ".png")):
        await msg.client.send_photo(
            chat_id=msg.chat.id,
            photo=path,
            caption=text,
            reply_markup=reply_markup
        )
    elif path.lower().endswith((".mkv", ".mp4")):
        await msg.client.send_video(
            chat_id=msg.chat.id,
            video=path,
            caption=text,
            reply_markup=reply_markup
        )
    else:
        await msg.client.send_document(
            chat_id=msg.chat.id,
            document=path,
            caption=text,
            reply_markup=reply_markup
        )
        
    # FOR ALPHA-X
    # .alive To check THE BOT STATUS😗
