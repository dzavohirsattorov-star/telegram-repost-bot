from telethon import TelegramClient, events
import os

API_ID = 39992891
API_HASH = "f8379d46a5f921ad5040a548cfec0839"
SOURCE = "futbol_fudbol_sport_tv_gollar"
TARGET = "jaxon_chemp"

client = TelegramClient('bot', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await client.forward_messages(TARGET, event.message)

client.start()
client.run_until_disconnected()
