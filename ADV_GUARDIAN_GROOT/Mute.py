from pyrogram import filters, Client as Ms_officials
from pyrogram.types import ChatPermissions

@Ms_officials.on_message(filters.command("mute"))
async def mute_users(bot, msg):
    user_id = msg.reply_to_message.from_user.id
    chat_id = msg.chat.id
    try:
        await bot.Chat.restrict_member(user_id, ChatPermissions())
    except:
        pass
    await msg.reply_text("Another one bites the dust...!")
