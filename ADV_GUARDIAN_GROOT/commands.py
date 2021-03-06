from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from database import insert, getid
from utils import not_subscribed
from config import ADMIN


START_MESSAGE = """ππ’ {},π ππ <a href=https://t.me/GROOT_ANNAN_MS_BOT>ππππππππ πππππ</a> π ππ πππππππ ππππππ πππ π ππ πππππππππ ππππ πππ πππππππ ππππ πππ ππ ππ ππππ πππππ πππ πππ ππ ππππππβ€οΈ
"""

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**β οΈSorry bro,You didn't Joined Our Updates Channel Join now and start againπ**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=client.invitelink)]
           ])
       )

@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    insert(int(msg.chat.id))
    await msg.reply_photo(
        photo="https://telegra.ph/file/cfcb2df74d7ac1e022084.jpg",
        caption=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("π° πππππππ π°", url="https://t.me/Zinan00100") 
            ],[
            InlineKeyboardButton("π’ πππππ πππππππ ππππππ’", url="https://t.me/moviespot001100")
            ],[
            InlineKeyboardButton("π ππππ π", callback_data="help"), 
            InlineKeyboardButton("π€  πππππ π€ ", callback_data="about")
            ],[
            InlineKeyboardButton("ΚΚα΄ΙͺΙ΄ α΄Κα΄α΄α΄π§ ", callback_data="brain"),
            InlineKeyboardButton("α΄Κα΄κ±α΄βοΈ", callback_data="close_data")
           ]]
           )
    )



@Client.on_message(filters.private & filters.command("id"))
async def iid_msg(bot, msg):
    await msg.reply_text(
        text = f"""<b>ππΎππ πΈπ³ πΈπ :</b> <code>{msg.from_user.id}</code>
<b>π΅πΈπππ π½π°πΌπ΄ :</b> <code>{msg.from_user.first_name}</code>
<b>π»π°ππ π½π°πΌπ΄ :</b> <code>{msg.from_user.last_name}</code>
<b>πππ» :</b> <code>https://t.me/{msg.from_user.username}</code>
""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("α΄Κα΄κ±α΄ γ‘", callback_data="close_data")
           ]]
           )
    )

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):    
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")
