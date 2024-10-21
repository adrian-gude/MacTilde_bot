import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends your chat ID."""
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Your chat ID is: {chat_id}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Function that executes when the user sends /start."""
    await update.message.reply_text("Hello! I am the MacTilde bot.")


def main():
    application = ApplicationBuilder().token(os.environ["TELEGRAM_TOKEN_API"]).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("getid", get_id))
    application.run_polling()


if __name__ == "__main__":
    # init the bot
    main()
