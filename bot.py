from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

PyrogramBot = Client(
    "ADV GUARDIAN GROOT",
    api_id=API_ID, 
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="ADV_GUARDIAN_GROOT")
)

print = "🤩BOT ON POWER🤩"


PyrogramBot.run()
