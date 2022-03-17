from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
 

@Ms.on_message(filters.command("start"))
async def start_msg(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/cfcb2df74d7ac1e022084.jpg"
        caption= f"""𝐇𝐢 {msg.from_user.mention},𝐈 𝐀𝐌 <a href=https://t.me/GROOT_ANNAN_MS_BOT>𝐆𝐔𝐀𝐑𝐃𝐈𝐀𝐍 𝐆𝐑𝐎𝐎𝐓</a> 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋𝐋𝐘 𝐔𝐒𝐄𝐃 𝐅𝐎𝐑 𝐒𝐄𝐑𝐈𝐄𝐄𝐒 𝐉𝐔𝐒𝐓 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐒𝐄𝐄 𝐌𝐘 𝐏𝐎𝐖𝐄𝐑𝐒❤️"""
