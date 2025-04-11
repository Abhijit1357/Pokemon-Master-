import os

# Load from env or set directly here
BOT_TOKEN = os.getenv("BOT_TOKEN", "7966519826:AAFzU7F_l7jNVk3fybpt8hl5Yj4zg4q3VOY")

# MongoDB URI (change this for production)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://AOMusic:AOMusic@cluster0.sibxiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Default map size (rows x cols)
MAP_WIDTH = 5
MAP_HEIGHT = 5

# Starting location
START_X = 2
START_Y = 2
