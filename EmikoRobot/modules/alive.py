import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/0943b1675752ff8716d77.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Seth Robot.** \n\n"
  TEXT += "⚡️**I'm Working Properly** \n\n"
  TEXT += f"⚡️ **My Master : [ꜱᴇᴛʜ★](https://t.me/xyzseth)** \n\n"
  TEXT += f"⚡️ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚡️ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚡️ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/SethRobot?start=help"), Button.url("Support", "https://t.me/sethproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)


@register(pattern=("/repo"))
async def source(event):
   TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}).** \n\n"
   TEXT += "**Here is The source of Seth Robot** \n\n"
   TEXT += "**Owner repo : [ꜱᴇᴛʜ★](https://t.me/xyzseth)** \n\n"
   TEXT += f"**Python Version :** `{kontol()}`\n\n"
   TEXT += f"**Library Version :** `{telever}` \n\n"
   TEXT += f"**Telethon Version :** `{tlhver}` \n\n"
   TEXT += f"**Pyrogram Version :** `{pyrover}` \n\n"
   BUTTON = [[Button.url("Repo", "https://github.com/Dorimuhai/sethrobot"), Button.url("Support", "https://t.me/sethproject")]]
   await event.reply(TEXT,  buttons=BUTTON, disable_web_page_preview=True)

