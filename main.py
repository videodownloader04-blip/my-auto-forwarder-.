from pyrogram import Client, filters
import os

# --- ENVIRONMENT VARIABLES (Railway-il ninnu data edukkuvਾਨu) ---
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

SOURCE_CHANNEL_ID = int(os.environ.get("SOURCE_CHANNEL_ID", 0))
TARGET_CHANNEL_ID = int(os.environ.get("TARGET_CHANNEL_ID", 0))

# --- PUTHIYA CAPTION (Ivide ningalude puthiya caption nalkuka) ---
NEW_CAPTION = """
🎬 **Puthiya Video Vannu!** 🚀

🔥 Enjoy the video without blur!
📢 Join our main channel for more!
"""

# Bot initialize cheyyunnu
app = Client(
    "auto_forward_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Source channelil puthiya message (video, photo, document) varumpol ee function work aakum
@app.on_message(filters.chat(SOURCE_CHANNEL_ID) & (filters.video | filters.photo | filters.document))
async def auto_forward_and_edit(client, message):
    try:
        print(f"Puthiya file vannu! Forward cheyyan thudangunnu...")

        # message.copy() use cheyyumbol puthiya post aayi pokum (Forwarded tag undavilla)
        await message.copy(
            chat_id=TARGET_CHANNEL_ID,
            caption=NEW_CAPTION,
            has_spoiler=False, # Ithu False aakkumpol Telegram-le aa thilangunna blur (spoiler) maari kittum!
            reply_markup=None  # Ithu None aakkumpol pazhaya postile buttons ozhivaayi kittum!
        )
        print("✅ Vijayakaramayi post cheythu!")
        
    except Exception as e:
        print(f"❌ Oru error vannu: {e}")

# Bot run cheyyunnu
if __name__ == "__main__":
    print("🚀 Bot start cheyyunnu...")
    app.run()
