from pyrogram import Client, filters
import os

# --- ENVIRONMENT VARIABLES ---
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

SOURCE_CHANNEL_ID = int(os.environ.get("SOURCE_CHANNEL_ID", 0))
TARGET_CHANNEL_ID = int(os.environ.get("TARGET_CHANNEL_ID", 0))

# --- POWERFUL CUSTOM CAPTION ---
NEW_CAPTION = """
✨ **New Update Released!** 🚀

🔥 **Quality:** HD & Unblurred
📢 **Channel:** Stay Tuned for More!
"""

app = Client(
    "powerful_auto_forward_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Media (Video, Photo, Document) varumbol work cheyyum
@app.on_message(filters.chat(SOURCE_CHANNEL_ID) & (filters.video | filters.photo | filters.document))
async def powerful_forwarder(client, message):
    try:
        print(f"⚡ Puthiya media vannu! Processing thudangunnu...")

        # Video aanel
        if message.video:
            await client.send_video(
                chat_id=TARGET_CHANNEL_ID,
                video=message.video.file_id,
                caption=NEW_CAPTION,
                supports_streaming=True
            )
        # Photo aanel
        elif message.photo:
            await client.send_photo(
                chat_id=TARGET_CHANNEL_ID,
                photo=message.photo.file_id,
                caption=NEW_CAPTION
            )
        # Document (File) aanel
        elif message.document:
            await client.send_document(
                chat_id=TARGET_CHANNEL_ID,
                document=message.document.file_id,
                caption=NEW_CAPTION
            )

        print("✅ Success: Media clean aayi post cheythu!")
        
    except Exception as e:
        print(f"❌ Error caught: {e}")

if __name__ == "__main__":
    print("🚀 Powerful Bot Successfully Started...")
    app.run()
