from pyrogram import Client


PyrogramBot = Client(
    "ADV GUARDIAN GROOT",
    api_hash="5023c40ea655bc2834e48888b17ccee8", 
    api_id="13160306", 
    bot_token="5221793107:AAGzaFdLJoZIBmKB1MeOLJCJRfK0rFfYkVg",
    database_uri="mongodb+srv://P7:P7@cluster0.gqnoo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    plugins=dict(root="ADV_GUARDIAN_GROOT")
)






PyrogramBot.run()
