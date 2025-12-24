import os
import time
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot Token Environment Variable থেকে নিবে
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
START_TIME = time.time()

def uptime():
    seconds = int(time.time() - START_TIME)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{days} দিন {hours} ঘন্টা {minutes} মিনিট {seconds} সেকেন্ড"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uptime_str = uptime()
    await update.message.reply_text(
        f"🤖 Bot চালু আছে!\n"
        f"⏰ Uptime: {uptime_str}\n"
        f"📅 শুরু হয়েছে: {datetime.fromtimestamp(START_TIME).strftime('%Y-%m-%d %I:%M:%S %p')}"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✅ Bot সক্রিয়! Uptime: {uptime()}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    
    print("Bot running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
