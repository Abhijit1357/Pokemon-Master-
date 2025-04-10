from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from config import BOT_TOKEN
from game.map import get_current_zone_description, move_player
from database.db import get_or_create_player

# Keyboard layout
keyboard = [["⬅️", "⬆️", "⬇️", "➡️"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    get_or_create_player(user_id)
    desc = get_current_zone_description(user_id)
    await update.message.reply_text(
        f"Welcome to Pokemon Master!\n\n{desc}",
        reply_markup=markup
    )

async def handle_movement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    direction = update.message.text.strip()

    if direction in ["⬆️", "⬇️", "⬅️", "➡️"]:
        new_desc = move_player(user_id, direction)
        await update.message.reply_text(new_desc)
    else:
        await update.message.reply_text("Use the buttons to move around!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_movement))

    print("Bot running...")
    app.run_polling()
