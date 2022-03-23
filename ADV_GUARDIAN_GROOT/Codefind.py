from pyrogram import Client, filters



@Client.on_message(filters.command("ans"))
async def fil_mod(bot, msg):
      mode_on = ["18gffvj", "182cdgbbr2", "18ygfvtyv12"]
      mode_of = ["vvgg", "shvdd", "ggffgy"]

      try:
         args = msg.text.split(None, 1)[1].lower()
      except:
         return await message.reply("checking answer")
      m = await msg.reply_text("checking answer in progress")

      if args in mode_on:
          await m.edit("✅️You are correct")
      elif args in mode_of:
          await m.edit("❎️Wrong answer")
      else:
          await m.edit("❎️Wrong answer")
