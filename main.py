import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

TOKEN = "8510481938:AAFNWm-ro49kiu6DFjVQ4v--hnHe012ZE-g"
CHAT_ID = "7863143280"

bot = Bot(token=TOKEN)
seen = set()

async def check_ttbs():
    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )

        page = await browser.new_page()

        await page.goto("https://ttbs.gtb.gov.tr/Home/BelgeSorgula")

        await page.wait_for_timeout(8000)

        content = await page.content()

        if "EMLAK" in content:
            if content not in seen:
                seen.add(content)
                await bot.send_message(
                    chat_id=CHAT_ID,
                    text="✅ TTBS'de yeni emlakçı göründü!"
                )

        await browser.close()


async def main():
    while True:
        try:
            await check_ttbs()
        except Exception as e:
            print("HATA:", e)

        await asyncio.sleep(60)


asyncio.run(main())
