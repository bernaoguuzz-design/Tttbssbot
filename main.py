import requests
import time
from telegram import Bot

TOKEN = "8510481938:AAFNWm-ro49kiu6DFjVQ4v--hnHe012ZE-g"
CHAT_ID = "7863143280"

bot = Bot(token=TOKEN)

seen = set()

def check_ttbs():
    url = "https://ttbs.gtb.gov.tr/Home/BelgeSorgula"

    r = requests.get(url)
    text = r.text

    if "EMLAK" in text:
        if text not in seen:
            seen.add(text)
            bot.send_message(chat_id=CHAT_ID,
                             text="✅ TTBS'de yeni belge olabilir, kontrol et!")

while True:
    try:
        check_ttbs()
        time.sleep(600)  # 10 dk
    except Exception as e:
        print(e)
