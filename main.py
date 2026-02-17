import requests
import time
from telegram import Bot
import asyncio

TOKEN = "8510481938:AAFNWm-ro49kiu6DFjVQ4v--hnHe012ZE-g"
CHAT_ID = "7863143280"

bot = Bot(token=TOKEN)

seen = set()

async def check_ttbs():
    url = "https://ttbs.gtb.gov.tr/Home/BelgeSorgula"

    r = requests.get(url)
    text = r.text

    if "EMLAK" in text:
        if text not in seen:
            seen.add(text)
            await bot.send_message(
                chat_id=CHAT_ID,
                text="✅ TTBS'de yeni emlakçı göründü!"
            )

async def main():
    while True:
        try:
            await check_ttbs()
        except Exception as e:
            print(e)
        await asyncio.sleep(60)

asyncio.run(main())
