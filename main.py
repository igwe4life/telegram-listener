from telethon import TelegramClient, events
import requests
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE")
webhook_url = os.getenv("WEBHOOK_URL")

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=1971444702))
async def handler(event):
    message_text = event.message.message

    try:
        requests.post(webhook_url, data={'message': message_text}, timeout=5)
    except Exception as e:
        print(e)

async def start_bot():
    await client.start(phone=phone_number)
    await client.run_until_disconnected()

def run_bot():
    client.loop.run_until_complete(start_bot())

# Run Telegram bot in background thread
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
