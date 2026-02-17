import asyncio
from playwright.async_api import async_playwright
import requests
import time
import os

TOKEN = "BURAYA_TOKEN"
CHAT_ID = "BURAYA_CHATID"

LAST_FILE = "last_record.txt"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def load_last():
    if os.path.exists(LAST_FILE):
        with open(LAST_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_last(value):
    with open(LAST_FILE, "w") as f:
        f.write(value)

async def check_ttbs():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://ttbs.gtb.gov.tr/Home/BelgeSorgula")

        await page.select_option("#Il", "35")  # İzmir
        await page.click("text=Ara")

        await page.wait_for_timeout(6000)

        # tabloda ilk satırı al
        first_row = await page.locator("table tbody tr").first.inner_text()

        await browser.close()

        last_saved = load_last()

        if last_saved == "":
            save_last(first_row)
            print("İlk kayıt alındı")
            return

        if first_row != last_saved:
            save_last(first_row)
            send(f"🚨 YENİ EMLAKÇI BELGESİ!\n\n{first_row}")

while True:
    asyncio.run(check_ttbs())
    time.sleep(600)  # 10 dakika
