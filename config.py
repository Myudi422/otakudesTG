import os
from telethon import TelegramClient

#api_id = os.environ.get('API_ID')
#api_hash = os.environ.get('API_HASH')
#bot_token = os.environ.get('BOT_TOKEN')
api_id = 7120601
api_hash = aebd45c2c14b36c2c91dec3cf5e8ee9a
bot_token = 1920905087:AAGvlh_lBs44Z_s9l7IzNyxtlo040oVKNFY

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
