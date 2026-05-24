import asyncio
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ========== НАСТРОЙКИ (ЗАМЕНИ ТОЛЬКО ТОКЕН) ==========
# Сюда вставь НОВЫЙ токен, который получишь от @BotFather после /revoke
BOT_TOKEN = "1336324350:AAE3BYhL8v_4zfKm0iOK75odc5_YqRI3NzQ"

# ССЫЛКА НА ТВОЙ MINI APP (уже правильная)
WEBAPP_URL = "https://hilarious-chebakia-aa675d.netlify.app"


# =====================================================

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Кнопка для открытия Mini App
    keyboard = [[
        KeyboardButton(
            "🚀 Открыть рейтинг",
            web_app=WebAppInfo(WEBAPP_URL)
        )
    ]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        f"🤖 Привет, {user.first_name}!\n\n"
        f"Добро пожаловать в систему рейтинга робототехников!\n\n"
        f"📊 Нажми на кнопку ниже, чтобы:\n"
        f"• Зарегистрироваться (ФИО и дата рождения)\n"
        f"• Увидеть свой рейтинг\n"
        f"• Посмотреть результаты олимпиад\n\n"
        f"🏆 Участвуй в олимпиадах и зарабатывай баллы!",
        reply_markup=reply_markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 **Как пользоваться:**\n"
        "1. Нажми 'Открыть рейтинг'\n"
        "2. Если ты тут впервые — заполни имя и дату рождения\n"
        "3. Увидишь свой рейтинг и общую таблицу\n\n"
        "🏅 Баллы начисляются за:\n"
        "• 1 место — 100 баллов\n"
        "• 2 место — 75 баллов\n"
        "• 3 место — 50 баллов\n"
        "• Участие — 25 баллов\n\n"
        "❓ Вопросы организаторам",
        parse_mode="Markdown"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Бот работает, Mini App доступен!")


def main():
    print("🤖 Бот запускается...")
    print(f"✅ Mini App URL: {WEBAPP_URL}")
    print("📱 Напишите /start в Telegram и проверьте кнопку")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))

    print("✅ Бот успешно запущен! Иди в Telegram.")
    app.run_polling()


if __name__ == "__main__":
    main()