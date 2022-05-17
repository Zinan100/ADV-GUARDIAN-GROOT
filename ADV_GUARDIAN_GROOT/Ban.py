from pyrogram import filters, Client as Ban
from time import time

@Ban.on_message(filters.command("ban"))
async def Ban_users(bot, msg):
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    try:
        await bot.ban_chat_member(chat_id, user_id)
    except:
        pass
    await msg.reply_text("""Another one bites the dust...!
Banned {msg.reply_to_message.from_user.mention}.""")

@Ban.on_message(filters.command("ban"))
async def Ban_users(bot, msg):
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    try:
        await bot.unban_chat_member(chat_id, user_id)
    except:
        pass
    await msg.reply_text("⚙️ᴜꜱᴇʀ ʜᴀꜱ ʙᴇᴇɴ ʙᴀɴᴇᴅ⚙️")
