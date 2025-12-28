import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler

# ====== تغییر بده ======
TELEGRAM_TOKEN = "توکن_تلگرام_تو"
OPENROUTER_API_KEY = "کلید_OpenRouter_تو"
# =======================

# 🔹 سوالات خاص و پاسخ‌ها
predefined_answers = {
    "سلام": "سلام! خوبی؟",
    "حالت چطوره؟": "من خوبم، ممنون که پرسیدی!",
    "اسم تو چیه؟": "من ربات هوشمند تو هستم."
}

def ask_ai(text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-r1",
        "messages": [
            {"role": "system", "content": "تو یک دستیار فارسی هستی"},
            {"role": "user", "content": text}
        ]
    }

    try:
        r = requests.post(url, headers=headers, json=data, timeout=15)
        print("Status Code:", r.status_code)
        print("Response:", r.text)
        if r.status_code != 200:
            return f"خطا در اتصال به API: {r.status_code}"
        else:
            return r.json()["choices"][0]["message"]["content"]

    except Exception as e:
        print("Exception:", e)
        return f"خطا در درخواست به API: {e}"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    
    # 🔹 اگر سوال در predefined_answers هست، جواب آماده بده
    if user_text in predefined_answers:
        reply = predefined_answers[user_text]
    else:
        reply = ask_ai(user_text)
    
    await update.message.reply_text(reply)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات هوشمند شما هستم. هر سوالی داری بپرس.")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# ====== هندلرها ======
app.add_handler(CommandHandler("start", start_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()
