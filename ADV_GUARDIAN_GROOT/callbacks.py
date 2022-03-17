from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random

START_MESSAGE = """𝐇𝐢 {},𝐈 𝐀𝐌 <a href=https://t.me/GROOT_ANNAN_MS_BOT>𝐆𝐔𝐀𝐑𝐃𝐈𝐀𝐍 𝐆𝐑𝐎𝐎𝐓</a> 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋𝐋𝐘 𝐔𝐒𝐄𝐃 𝐅𝐎𝐑 𝐒𝐄𝐑𝐈𝐄𝐄𝐒 𝐉𝐔𝐒𝐓 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐒𝐄𝐄 𝐌𝐘 𝐏𝐎𝐖𝐄𝐑𝐒❤️
"""



@Client.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        await msg.message.edit(
            text=START_MESSAGE.format(msg.from_user.mention),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝐂𝐑𝐄𝐀𝐓𝐎𝐑 🔰", url="https://t.me/Zinan00100"),
                InlineKeyboardButton("💢 𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐆𝐑𝐎𝐔𝐏💢", url="https://t.me/moviespot001100")
                ],[
                InlineKeyboardButton("📚 𝐇𝐄𝐋𝐏 📚", callback_data="help"), 
                InlineKeyboardButton("🤠 𝐀𝐁𝐎𝐔𝐓 🤠", callback_data="about") 
               ]]
               )
        )
       
    elif msg.data == "info":
        await msg.message.edit(
            text="""Commands and Usage:
• /id - get id of a specifed""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝙱𝚊𝚌𝚔", callback_data="help")
               ]]
               )
        )

    elif msg.data == "help":
        await msg.message.edit(
            text= f"""HEY {msg.from_user.mention} HERE IS THE HELP FOR <a href=https://t.me/GROOT_ANNAN_MS_BOT>GUARDIAN GROOT</a>
""",
            reply_markup=InlineKeyboardMarkup
                InlineKeyboardButton("𝙸𝙳", callback_data="info")
                InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="start") 
               ]]
               ) 
        ) 

             
