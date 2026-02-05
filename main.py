from telethon import TelegramClient, events
import requests
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

webhook_url = os.getenv("WEBHOOK_URL")

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=1971444702))
async def handler(event):
    message_text = event.message.message
    payload = {'message': message_text}

    try:
        response = requests.post(webhook_url, data=payload, verify=False)
        print(f"Sent: {message_text} | Status: {response.status_code}")
    except Exception as e:
        print(f"Failed: {e}")

async def main():
    await client.start(phone=phone_number)
    print("Listening for messages...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
