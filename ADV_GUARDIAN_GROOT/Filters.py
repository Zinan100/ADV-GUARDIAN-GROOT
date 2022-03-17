from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.regex("Super shranya"))
async def regex(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/ab6d292895350fc995414.jpg",
        caption="""📟 Movie Name : Super Sharanya
🗒️ Release Date : 07 Jan 2022 (India)

📧 Votes : 418
⏰ RunTime : 161 Minutes
⭐ IMDB Rating : 6.9/10
🎞️ Genres : Comedy,  Romance, 
🎬 Director : Girish A.D.
📝 Writer : Girish A.D.
🔊 Languages : #Malayalam HD
💃🏻 Cast : Antony Varghese,  Arjun Asokan,  Mamitha Baiju,  Vineeth Vishwam,  Anaswara Rajan, 

›› Download ›""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("♀️ 𝘿𝙊𝙒𝙇𝙊𝘼𝘿 ♀️", url="https://t.me/Rexer0BOT_BOT?start=BATCH-BQADBQAD7AMAAj7cWFUaUL9p5lhGdRYE")
           ]]
           )
    )
