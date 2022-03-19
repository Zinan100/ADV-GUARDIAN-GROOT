import os
import pyrogram
from telegraph import upload_file
from pyrogram import filters, Client
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
import logging




@Client.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ")
  userid = str(message.chat.id)
  img_path = (f"./Download....!/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʙy @crimebhavani4")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʙy @crimebhavani4") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Client.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʙy @crimebhavani4")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("Loading ▣▣▢`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ join @crimebhavani4") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb join @septemberfilms")

@Client.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʙy @crimebhavani4")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("yours text")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʙy @crimebhavani4") 
  else:
    await message.reply_text("ᴜᴩʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʙy @crimebhavani4")
