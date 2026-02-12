import requests
import time

TOKEN = "8510481938:AAFNWm-ro49kiu6DFjVQ4v--hnHe012ZE-g"
CHAT_ID = "7863143280"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    send("TTBS takip sistemi aktif ✅")

while True:
    check()
    time.sleep(600)
