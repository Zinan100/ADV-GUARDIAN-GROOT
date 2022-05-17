from pyrogram import filters, Client as Ms_officials 
from time import time

from ADV_GUARDIAN_GROOT.helper_functions.admin_check import admin_check
from ADV_GUARDIAN_GROOT.helper_functions.extract_user import extract_user
from ADV_GUARDIAN_GROOT.helper_functions.string_handling import extract_time

@Ms_officials.on_message(filters.command("ban"))
async def ban_users(bot, msg):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    try:
        await bot.ban_chat_member(chat_id, user_id)
    except:
        pass
    await msg.reply_text("Another one bites the dust...!")

@Ms_officials.on_message(filters.command("unban"))
async def unban_users(bot, msg):
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    try:
        await bot.unban_chat_member(chat_id, user_id)
    except:
        pass
    await msg.reply_text("ഒരു തവണ ഷമിച്ചു ഇനി മേലാ ഇത് ആവർത്തിക്കരുത്")

