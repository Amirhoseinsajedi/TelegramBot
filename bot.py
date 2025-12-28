from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler

# ====== تغییر بده ======
TELEGRAM_TOKEN = "8078280538:AAEHAzSGTSGOZk9oC_Kefc6l5zSERtSVLQw"
# =======================

# 🔹 سوالات خاص و پاسخ‌ها
predefined_answers = {
    "سلام": "سلام! خوبی؟",
    "حالت چطوره؟": "من خوبم، ممنون که پرسیدی!",
    "اسم تو چیه؟": "من ربات هوشمند تو هستم.",
        "اسمت چیه": "من ربات هوشمند تو هستم.",
                "اسم مامانم چیه؟": " پرستو همزه ارباب میخوای راجبش ااطلاعات بهت بدم",
                                "بله بده": " اون با آیدی @Parastoooo  در ویراستی فعال سیاسی هستش",
                                                " بیشتر اطلاعات بده": " متاسفانه نمیتونم وارد حریم خصوصی شم",
                                                                "هدف من از ساخت تو چیه": "من برای پروژه بازی سازی استاد جواهریان پیاده سازی شدم",
                                                                                " چطوری": "ممنون تو خوبی؟",
                                                                                                " ممنون": "خواهش میکنم میخوای باهم حرف بزنیم راجب ai",
                                                                                                                "بله": "بیا راجب هوش مصنوعی های توسعه یافته در سال جدید باهم گپ بزنیم",
                                                                                                                                "اسم من له عنوان سازندت چیه؟": "شما امیرحسین ساجدی هستی",
                                                                                                                                                "نام سازندت": "امیرحسین ساجدی",
                                                                                                                                                                "خداحافظ": " به امید دیدار مجدد",   
                                                                                                                                                                "بای": " به امید دیدار مجدد",

    
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    
    # 🔹 اگر سوال در predefined_answers هست، جواب آماده بده
    if user_text in predefined_answers:
        reply = predefined_answers[user_text]
    else:
        reply = "متاسفم، من جواب این سوال را بلد نیستم."

    await update.message.reply_text(reply)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات هوشمند شما هستم. هر سوالی داری بپرس.")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# ====== هندلرها ======
app.add_handler(CommandHandler("start", start_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()

