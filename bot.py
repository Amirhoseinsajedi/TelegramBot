import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ====== تغییر بده ======
TELEGRAM_TOKEN = "8078280538:AAEHAzSGTSGOZk9oC_Kefc6l5zSERtSVLQw"
OPENROUTER_API_KEY = "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"
# =======================

def ask_ai(text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-r1",  # مدل رایگان
        "messages": [
            {"role": "system", "content": "تو یک دستیار فارسی هستی"},
            {"role": "user", "content": text}
        ]
    }

    try:
        r = requests.post(url, headers=headers, json=data, timeout=15)
        print("Status Code:", r.status_code)
        print("Response:", r.text)  # چاپ جواب کامل برای دیباگ

        if r.status_code != 200:
            return f"خطا در اتصال به API: {r.status_code}"
        else:
            return r.json()["choices"][0]["message"]["content"]

    except Exception as e:
        print("Exception:", e)
        return f"خطا در درخواست به API: {e}"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = ask_ai(user_text)
    await update.message.reply_text(reply)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات هوشمند شما هستم. هر سوالی داری بپرس.")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# ====== هندلرها ======
from telegram.ext import CommandHandler
app.add_handler(CommandHandler("start", start_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()


