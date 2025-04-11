from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from config import BOT_TOKEN
from game.map import get_current_zone_description, move_player
from database.db import get_or_create_player

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Keyboard layout
keyboard = [["⬅️", "⬆️", "⬇️", "➡️"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Telegram command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    get_or_create_player(user_id)
    desc = get_current_zone_description(user_id)

    await update.message.reply_text(
        f"Welcome to Pokemon Master!\n\n{desc}",
        reply_markup=markup
    )

    # Inline channel button
    channel_button = InlineKeyboardMarkup([
        [InlineKeyboardButton("Our Channel", url="https://t.me/Pokemon_Master_x")]
    ])

    await update.message.reply_text(
        "Check out our channel for updates!",
        reply_markup=channel_button
    )

# Handle directional movement
async def handle_movement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    direction = update.message.text.strip()

    if direction in ["⬆️", "⬇️", "⬅️", "➡️"]:
        new_desc = move_player(user_id, direction)
        await update.message.reply_text(new_desc)
    else:
        await update.message.reply_text("Use the buttons to move around!")

# Dummy HTTP server for Koyeb health check
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is alive!')

def start_health_server():
    server = HTTPServer(('0.0.0.0', 8000), HealthHandler)
    server.serve_forever()

if __name__ == '__main__':
    # Start health check server in background
    threading.Thread(target=start_health_server, daemon=True).start()

    # Start Telegram bot
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_movement))

    print("Bot running...")
    app.run_polling()
