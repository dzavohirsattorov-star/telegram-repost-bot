import asyncio
import sys
import types
sys.modules['imghdr'] = types.ModuleType('imghdr')

from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

API_ID = int(os.environ.get("API_ID", "39992891"))
API_HASH = os.environ.get("API_HASH", "f8379d46a5f921ad5040a548cfec0839")
SESSION_STRING = os.environ.get("SESSION_STRING", "")
SOURCE = os.environ.get("SOURCE", "fudboltveyey")
TARGET = os.environ.get("TARGET", "jaxon_chemp")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await client.send_message(TARGET, event.message)
    print("Xabar kochirildi!")

print("Bot ishga tushdi!")
client.start()
client.run_until_disconnected()
