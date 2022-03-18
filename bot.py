from pyrogram import Client
from info import DATABASE_URI, DATABASE_NAME


PyrogramBot = Client(
    "ADV GUARDIAN GROOT",
    api_hash="5023c40ea655bc2834e48888b17ccee8", 
    api_id="13160306", 
    bot_token="5221793107:AAGzaFdLJoZIBmKB1MeOLJCJRfK0rFfYkVg",
    database_uri="mongodb+srv://P7:P7@cluster0.gqnoo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    database_name="CLUSTER0",
    plugins=dict(root="ADV_GUARDIAN_GROOT")
)






PyrogramBot.run()
