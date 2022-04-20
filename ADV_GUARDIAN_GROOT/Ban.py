from pyrogram import filters, Client as Ban
from time import time

@Ban.on_message(filters.command("ban"))
async def Ban_users(bot, msg):
    await msg.reply_text("⚙️ᴜꜱᴇʀ ʜᴀꜱ ʙᴇᴇɴ ʙᴀɴᴇᴅ⚙️")
    await msg.ban_chat_member(chat_id, user_id)

