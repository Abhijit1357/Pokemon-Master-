import os

# Load from env or set directly here
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

# MongoDB URI (change this for production)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Default map size (rows x cols)
MAP_WIDTH = 5
MAP_HEIGHT = 5

# Starting location
START_X = 2
START_Y = 2
