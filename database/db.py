from pymongo import MongoClient
from config import MONGO_URI, START_X, START_Y

client = MongoClient(MONGO_URI)
db = client["pokemon_master"]
players = db["players"]

def get_or_create_player(user_id):
    player = players.find_one({"user_id": user_id})
    if not player:
        player = {
            "user_id": user_id,
            "x": START_X,
            "y": START_Y,
            "pokemons": [],
            "region": None,
            "starter_pokemon": None,
            "wins": 0,
            "losses": 0
        }
        players.insert_one(player)
    return player

def get_player(user_id):
    return players.find_one({"user_id": user_id}) or get_or_create_player(user_id)

def update_player_location(user_id, x, y):
    players.update_one(
        {"user_id": user_id},
        {"$set": {"x": x, "y": y}}
    )

def update_battle_result(user_id, won):
    field = "wins" if won else "losses"
    players.update_one(
        {"user_id": user_id},
        {"$inc": {field: 1}}
    )

def set_player_region(user_id, region):
    players.update_one(
        {"user_id": user_id},
        {"$set": {"region": region}}
    )

def set_starter_pokemon(user_id, pokemon_name):
    players.update_one(
        {"user_id": user_id},
        {
            "$set": {"starter_pokemon": pokemon_name},
            "$push": {"pokemons": pokemon_name}
        }
)
