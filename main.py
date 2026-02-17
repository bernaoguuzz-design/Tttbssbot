import requests
import asyncio
from telegram import Bot

TOKEN = "8510481938:AAFNWm-ro49kiu6DFjVQ4v--hnHe012ZE-g"
CHAT_ID = "7863143280"

bot = Bot(token=TOKEN)

last_content = None  # önceki sonucu tutacağız


async def check_ttbs():
    global last_content

    try:
        url = "https://ttbs.gtb.gov.tr/Home/BelgeSorgula"

        # siteyi çek
        r = requests.get(url, timeout=20)

        if r.status_code != 200:
            print("Site cevap vermedi")
            return

        content = r.text

        # ilk çalışmada sadece kaydet (mesaj atma)
        if last_content is None:
            last_content = content
            print("İlk veri alındı")
            return

        # gerçekten değişmişse mesaj gönder
        if content != last_content:
            last_content = content

            await bot.send_message(
                chat_id=CHAT_ID,
                text="✅ TTBS'de yeni belge olabilir! Kontrol et."
            )

            print("Yeni değişiklik bulundu")

    except Exception as e:
        print("HATA:", e)


async def main():
    while True:
        await check_ttbs()
        await asyncio.sleep(600)  # 10 dakika


asyncio.run(main())
