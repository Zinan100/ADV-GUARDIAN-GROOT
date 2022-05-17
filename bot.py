import os
import logging 
import logging.config
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

FORCE_SUB = os.environ.get("FORCE_SUB", None)

class TG(Client):

    def __init__(self):
        super().__init__(
            "ADV GUARDIAN GROOT",
            api_id=API_ID, 
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="ADV_GUARDIAN_GROOT")
        )

    async def start(self):
       await super().start()
       me = await self.get_me() 
       self.mention = me.mention
       self.username = me.username 
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)
            self.invitelink = link
         except Exception as e:
            logging.warning(e) 
            logging.warning("Make Sure Bot admin in force sub channel") 
            self.force_channel = None
       logging.info(f"{me.first_name} Started 🤩🤩")
        
    async def stop(self, *args):
      await super().stop()
      logging.info("Bot Stopped")
        
bot = TG()
bot.run()






