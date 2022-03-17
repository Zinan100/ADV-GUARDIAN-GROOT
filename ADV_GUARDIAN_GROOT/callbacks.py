from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random


@PyrogramBot.on_callback_query()
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
        
