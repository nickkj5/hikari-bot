import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Oi oi! Eu sou a Hikari 🌸")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hikari está online! ✨")

async def fixar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        try:
            await context.bot.pin_chat_message(
                chat_id=update.effective_chat.id,
                message_id=update.message.reply_to_message.message_id
            )
            await update.message.reply_text("Mensagem fixada! 📌")
        except:
            await update.message.reply_text("Não consegui fixar a mensagem 😢")
    else:
        await update.message.reply_text("Responda a uma mensagem com /fixar para fixá-la 📌")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("fixar", fixar))

print("Hikari iniciou!")

app.run_polling()
