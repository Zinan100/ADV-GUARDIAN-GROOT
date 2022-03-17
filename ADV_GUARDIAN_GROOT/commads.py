from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_MESSAGE = """𝐇𝐢 {},𝐈 𝐀𝐌 <a href=https://t.me/GROOT_ANNAN_MS_BOT>𝐆𝐔𝐀𝐑𝐃𝐈𝐀𝐍 𝐆𝐑𝐎𝐎𝐓</a> 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 𝐈 𝐀𝐌 𝐒𝐏𝐄𝐂𝐈𝐀𝐋𝐋𝐘 𝐔𝐒𝐄𝐃 𝐅𝐎𝐑 𝐒𝐄𝐑𝐈𝐄𝐄𝐒 𝐉𝐔𝐒𝐓 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐒𝐄𝐄 𝐌𝐘 𝐏𝐎𝐖𝐄𝐑𝐒❤️
"""
 

@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/cfcb2df74d7ac1e022084.jpg",
        caption=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🔰 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 🔰", url="https://t.me/Zinan00100"),
            InlineKeyboardButton("💢 𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐆𝐑𝐎𝐔𝐏💢", url="https://t.me/moviespot001100")
            ],[
            InlineKeyboardButton("📚 𝐇𝐄𝐋𝐏 📚", callback_data="help"), 
            InlineKeyboardButton("🤠 𝐀𝐁𝐎𝐔𝐓 🤠", callback_data="about") 
           ]]
           )
    )

@Client.on_message(filters.private & filters.command("id"))
async def id_msg(bot, msg):
    await msg.reply_photo(
        photo=random.choice(All_Pic),
        caption= f"""
First Name : <code>{msg.from_user.first_name}</code>
Last Name : <code>{msg.from_user.last_name}</code>
Username : @{msg.from_user.username}
User ID : <code>{msg.from_user.id}</code>
        """
        )

@Client.on_message(filters.group & filters.command("id"))
async def id_msg(bot, msg):
    await msg.reply_text(
        text= f"""
Group Name : {msg.chat.title}
Group Username : @{msg.chat.username}
Group ID : {msg.chat.id}"""
    )
 
