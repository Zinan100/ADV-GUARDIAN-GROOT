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
            text="▣▢▢"
        )
        await msg.message.edit(
            text="▣▣▢"
        )
        await msg.message.edit(
            text="▣▣▣"
        )
        await msg.message.edit(
            text=START_MESSAGE.format(msg.from_user.mention),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝐂𝐑𝐄𝐀𝐓𝐎𝐑 🔰", url="https://t.me/Zinan00100")
                ],[
                InlineKeyboardButton("💢 𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐆𝐑𝐎𝐔𝐏💢", url="https://t.me/moviespot001100")
                ],[
                InlineKeyboardButton("📚 𝐇𝐄𝐋𝐏 📚", callback_data="help"), 
                InlineKeyboardButton("🤠 𝐀𝐁𝐎𝐔𝐓 🤠", callback_data="about")
                ],[
                InlineKeyboardButton("ᴄʟᴏꜱᴇ❌️", callback_data="close_data")
               ]]
               )
        )
       
    elif msg.data == "info":
        await msg.message.edit(
            text="▣▢▢"
        )
        await msg.message.edit(
            text="▣▣▢"
        )
        await msg.message.edit(
            text="▣▣▣"
        )
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
            text="▣▢▢"
        )
        await msg.message.edit(
            text="▣▣▢"
        )
        await msg.message.edit(
            text="▣▣▣"
        )
        await msg.message.edit(
            text= f"""HEY {msg.from_user.mention} HERE IS THE HELP FOR <a href=https://t.me/GROOT_ANNAN_MS_BOT>GUARDIAN GROOT</a>""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("ɪᴅ & ɪɴꜰᴏ", callback_data="info"),
                InlineKeyboardButton("ᴛᴇʟᴇɢʀᴀᴩʜ", callback_data="tgra"),       
                InlineKeyboardButton("ᴄᴏᴠɪᴅ", callback_data="cov")
                ],[
                InlineKeyboardButton("yᴛ ᴛʜᴜᴍᴩ", callback_data="ytth"),
                InlineKeyboardButton("ꜱᴛɪᴄᴋᴇʀ ɪᴅ", callback_data="stid"),
                InlineKeyboardButton("ꜱᴏɴɢ", callback_data="song")
                ],[
                InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="start"),
                InlineKeyboardButton("ᴄʟᴏꜱᴇ❌️", callback_data="close_data")
               ]]
               ) 
        )

    elif msg.data == "tgra":
        await msg.message.edit(
            text="▣▢▢"
        )
        await msg.message.edit(
            text="▣▣▢"
        )
        await msg.message.edit(
            text="▣▣▣"
        )
        await msg.message.edit(
            text="""▫️HELP: Telegraph▪️

Do as you wish with telegra.ph module!

USAGE:

🤧 /telegraph - Send me Picture or Vide Under (5MB)

NOTE:

• This Command Is Available in goups and pms
• This Command Can be used by everyone
""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="help")
               ]]
               )
        )

    elif msg.data == "cov":
        await msg.message.edit(
            text="▣▢▢"
        )
        await msg.message.edit(
            text="▣▣▢"
        )
        await msg.message.edit(
            text="▣▣▣"
        )
        await msg.message.edit(
            text="""➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽

𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/covid 𝖨𝗇𝖽𝗂𝖺
""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="help")
               ]]
               )
        )
 
    elif msg.data == "about":
        await msg.answer("""𖣘𝐶𝑟𝑒𝑎𝑡𝑒𝑟 𝙕𝙄𝙉𝘼𝙉 𝙏𝙀𝘾𝙃 𝟚. 𝕆 [ᵒⁿˡⁱⁿᵉ]🇦🇹
✯𝐷𝑒𝑣 𝙏𝙂 𝙋𝙐𝙎𝙃𝙋𝘼 𝙍𝙀𝙅𝙐🇮🇳[OFFLINE]
✵𝐵𝑜𝑡 𝙸𝙽𝙳𝙸𝙰𝙽""", show_alert=True)

    elif msg.data == "ytth":
        await msg.message.edit(
            text="▣▢▢"
        )
        await msg.message.edit(
            text="▣▣▢"
        )
        await msg.message.edit(
            text="▣▣▣"
        )
        await msg.message.edit(
            text="""𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.be/UyzJ9KEoU0w</code>""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="help")
               ]]
               )
        )
    elif msg.data == "stid":
        await msg.message.edit(
            text="""𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="help")
               ]]
               )
        )

    elif msg.data == "close_data":
        await msg.message.edit(
            text="<b>𝙲𝙻𝙾𝚂𝙸𝙽𝙶</b>"
        )
        await msg.message.edit(
            text="<b>𝙲𝙻𝙾𝚂𝙸𝙽𝙶</b>⭗ ⭗ ⭗ ⭗ ⭗ ⭗"
        )
        await msg.message.edit(
            text="<b>𝙲𝙻𝙾𝚂𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙶𝚁𝙴𝚂𝚂</b>⦿ ⦿ ⦿ ⭗ ⭗ ⭗"
        )
        await msg.message.edit(
            text="<b>𝙲𝙻𝙾𝚂𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙶𝚁𝙴𝚂𝚂</b>⦿ ⦿ ⦿ ⦿ ⭗ ⭗"
        )
        await msg.message.edit(
            text="<b>𝙲𝙻𝙾𝚂𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙶𝚁𝙴𝚂𝚂</b>⦿ ⦿ ⦿ ⦿ ⦿ ⭗"
        )
        await msg.message.edit(
            text="<b>𝙲𝙻𝙾𝚂𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙶𝚁𝙴𝚂𝚂</b>⦿ ⦿ ⦿ ⦿ ⦿ ⦿"
        )
        await msg.message.delete()  


    elif msg.data == "secode":
        await msg.message.edit(
            text=random.choice(All_Message)
        )
        await msg.delete()

    elif msg.data == "song"
        await msg.message.edit(
            text="""🎼Song Download🎼
Song Download Module, For Those Who Love Music

🎈 Command 🎈

- /song [Song Name] - To Download Music 😁

🌀Usage🌀
- Can Be Used By Everyone
- Works in bot pm

Made By <a href=https://t.me/moviespot00100>ᴍꜱ ᴜᴩᴅᴀᴛᴇᴢ</a>""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help"
               ]]
               )
        )
