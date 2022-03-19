from pyrogram import Client

Tgraph = Client(
    "PyrogramBot",
    api_hash="d9647913e97bf2f6a66d978290284028",
    api_id="17946666",
    bot_token="5133844869:AAGQZsJ1ZYwiY62s-om3ZXU7fB94LIwX2rY",
    plugins=dict(root="Tgraph")
  )

Tgraph.run()
