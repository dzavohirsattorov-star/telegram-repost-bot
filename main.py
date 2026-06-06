import asyncio
from telethon import TelegramClient, events

API_ID = 39992891
API_HASH = "f8379d46a5f921ad5040a548cfec0839"
BOT_TOKEN = "8955269705:AAE-EG8l1be_6j587V1aTLiARkZWoaupsz0"
SOURCE = "futbol_fudbol_sport_tv_gollar"
TARGET = "jaxon_chemp"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await bot.forward_messages(TARGET, event.message)

bot.run_until_disconnected()
