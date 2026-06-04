from telethon import TelegramClient, events

API_ID = 12345678
API_HASH = "your_api_hash"
SOURCE = -1001234567890
TARGET = -1001234567891

client = TelegramClient('bot', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    await client.forward_messages(TARGET, event.message)

client.start()
client.run_until_disconnected()
