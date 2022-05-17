from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from database import *


START_MESSAGE = """𝐇𝐢 {},𝐈 𝐀𝐌 <a href=https://t.me/GROOT_ANNAN_MS_BOT>𝐆𝐔𝐀𝐑𝐃𝐈𝐀𝐍 𝐆𝐑𝐎𝐎𝐓</a> 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋𝐋𝐘 𝐔𝐒𝐄𝐃 𝐅𝐎𝐑 𝐒𝐄𝐑𝐈𝐄𝐄𝐒 𝐉𝐔𝐒𝐓 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐒𝐄𝐄 𝐌𝐘 𝐏𝐎𝐖𝐄𝐑𝐒❤️
"""

@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    insert(int(message.chat.id))
    await msg.reply_photo(
        photo="https://telegra.ph/file/cfcb2df74d7ac1e022084.jpg",
        caption=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🔰 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 🔰", url="https://t.me/Zinan00100") 
            ],[
            InlineKeyboardButton("💢 𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐆𝐑𝐎𝐔𝐏💢", url="https://t.me/moviespot001100")
            ],[
            InlineKeyboardButton("📚 𝐇𝐄𝐋𝐏 📚", callback_data="help"), 
            InlineKeyboardButton("🤠 𝐀𝐁𝐎𝐔𝐓 🤠", callback_data="about")
            ],[
            InlineKeyboardButton("ʙʀᴀɪɴ ᴄʜᴇᴄᴋ🧠", callback_data="brain"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ❌️", callback_data="close_data")
           ]]
           )
    )



@Client.on_message(filters.private & filters.command("id"))
async def iid_msg(bot, msg):
    await msg.reply_text(
        text = f"""<b>𝚈𝙾𝚄𝚁 𝙸𝙳 𝙸𝚂 :</b> <code>{msg.from_user.id}</code>
<b>𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴 :</b> <code>{msg.from_user.first_name}</code>
<b>𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴 :</b> <code>{msg.from_user.last_name}</code>
<b>𝚄𝚁𝙻 :</b> <code>https://t.me/{msg.from_user.username}</code>
""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴄʟᴏꜱᴇ メ", callback_data="close_data")
           ]]
           )
    )
