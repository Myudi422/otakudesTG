import os
from telethon import TelegramClient

api_id = os.environ.get('7120601')
api_hash = os.environ.get('aebd45c2c14b36c2c91dec3cf5e8ee9a')
bot_token = os.environ.get('1924465560:AAEgJ88UX60pNePNIEMY3f-izdp3mVwfp-I')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
