from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
 

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
 
