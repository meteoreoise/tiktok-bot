import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# التوكن تاع البوت (عوضو بتاعك)
TELEGRAM_BOT_TOKEN = "7164621331:AAGAKbR-dIn8L_FsBape2VSbMcKpFqPPBwQ"

# الدالة لي تجيب اليوزر من ID
def get_username_from_id(user_id: int) -> str:
    headers = {
        "User-Agent": "Instagram 155.0.0.37.107 Android",
    }
    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data["user"]["username"]
    else:
        return None

# لما المستخدم يبعث الأمر
async def username_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🔢 بعت ID تاع المستخدم هكذا:\n`/username 1903424587`", parse_mode='Markdown')
        return

    try:
        user_id = int(context.args[0])
        username = get_username_from_id(user_id)
        if username:
            await update.message.reply_text(f"✅ اليوزر هو: @{username}")
        else:
            await update.message.reply_text("❌ معرف خاطئ أو الحساب خاص.")
    except Exception as e:
        await update.message.reply_text(f"⚠️ خطأ: {e}")

# إطلاق البوت
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("username", username_command))

print("🚀 البوت راهو يخدم...")
app.run_polling()
