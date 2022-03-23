from pyrogram import Client, filters
import random

All_Message = [
    "18yg12",
    "182cd2",
    "18gffvj"
]



@Client.on_message(filters.command("ans"))
async def fil_mod(bot, msg):
      mode_on = ["18gffvj", "182cd2", "18yg12"]
      mode_of = ["vvgg", "shvdd", "ggffgy"]

      try:
         args = msg.text.split(None, 1)[1].lower()
      except:
         return await msg.reply("ɪɴɢʟᴜᴅᴇ yᴏᴜʀᴇ ᴀɴꜱᴡᴇʀ ᴡɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ ᴇxᴀᴍᴩʟᴇ:/ans 12g ᴛʜᴇ ᴀɴꜱᴡᴇʀ ᴏɴʟy ʜᴀꜱ 6 ᴄʜᴀʀᴇᴄᴛᴇʀꜱ")
      m = await msg.reply_text("ɪɴɢʟᴜᴅᴇ yᴏᴜʀᴇ ᴀɴꜱᴡᴇʀ ᴡɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ ᴇxᴀᴍᴩʟᴇ:/ans 12g ᴛʜᴇ ᴀɴꜱᴡᴇʀ ᴏɴʟy ʜᴀᴠᴇ 6 ᴄʜᴀʀᴇᴄᴛᴇʀꜱ")

      if args in mode_on:
          await m.edit("✅️You are correct")
      else:
          await m.edit("❎️Wrong answer")



@Client.on_message(filters.command("seccode"))
async def fil_mod(bot, msg):
    await msg.message.reply_text(
        text=random.choice(All_Message)
    )
    await msg.message.edit(
        text="ᴛyᴩᴇ ᴛʜᴀᴛ ꜱʜᴏᴡɴ ᴄᴏᴅᴇ ᴡɪᴛʜ /ᴀɴꜱ <ᴄᴏᴅᴇ>"
    )
