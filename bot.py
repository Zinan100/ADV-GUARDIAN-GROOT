from pyrogram import Client


PyrogramBot = Client(
    "ADV GUARDIAN GROOT",
    api_hash="API_HASH", 
    api_id="API_ID", 
    bot_token="BOT_TOKEN",
    plugins=dict(root="ADV_GUARDIAN_GROOT")
)






PyrogramBot.run()
