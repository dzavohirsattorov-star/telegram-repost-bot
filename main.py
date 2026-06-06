from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes
import asyncio

BOT_TOKEN = "8955269705:AAE-EG8l1be_6j587V1aTLiARkZWoaupsz0"
SOURCE = "@futbol_fudbol_sport_tv_gollar"
TARGET = "@jaxon_chemp"

async def check_and_forward(app):
    last_id = 0
    while True:
        try:
            updates = await app.bot.get_updates(offset=last_id)
            channel = await app.bot.get_chat(SOURCE)
            messages = await app.bot.get_chat(channel.id)
        except:
            pass
        await asyncio.sleep(60)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    asyncio.run(check_and_forward(app))
