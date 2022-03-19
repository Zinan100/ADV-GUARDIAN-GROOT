from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

@Client.on_message(filters.private & filters.command("id"))
async def id_msg(bot, msg):
    await msg.reply_text(
        caption= f"""
First Name : <code>{msg.from_user.first_name}</code>
Last Name : <code>{msg.from_user.last_name}</code>
Username : @{msg.from_user.username}
User ID : <code>{msg.from_user.id}</code>
        """
        )

@Client.on_message(filters.group & filters.command("id"))
async def idd_msg(bot, msg):
    await msg.reply_text(
        text= f"""
Group Name : {msg.chat.title}
Group Username : @{msg.chat.username}
Group ID : {msg.chat.id}"""
    )
 
