from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SOURCE_CHANNEL_ID = int(os.environ.get("SOURCE_CHANNEL_ID", 0))
TARGET_CHANNEL_ID = int(os.environ.get("TARGET_CHANNEL_ID", 0))

NEW_CAPTION = "✨ **New Video!** 🚀\n\nEnjoy the content!"

app = Client("powerful_auto_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNEL_ID) & (filters.video | filters.photo | filters.document))
async def powerful_forwarder(client, message):
    try:
        # ചാനലിലേക്ക് ഒന്ന് കണക്ട് ചെയ്യാൻ ശ്രമിക്കുന്നു
        await client.get_chat(TARGET_CHANNEL_ID)
        
        if message.video:
            await client.send_video(TARGET_CHANNEL_ID, message.video.file_id, caption=NEW_CAPTION, supports_streaming=True)
        elif message.photo:
            await client.send_photo(TARGET_CHANNEL_ID, message.photo.file_id, caption=NEW_CAPTION)
        elif message.document:
            await client.send_document(TARGET_CHANNEL_ID, message.document.file_id, caption=NEW_CAPTION)
        
        print("✅ Success!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    app.run()
