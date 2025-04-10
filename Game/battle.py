import random
from engine.pokemon_engine import start_battle
from database.db import update_battle_result

def initiate_battle(user_id, player_pokemon, wild_pokemon):
    print(f"Battle started: {player_pokemon} vs {wild_pokemon}")

    # Call the C++ battle engine
    result = start_battle(player_pokemon, wild_pokemon)

    if result == "win":
        update_battle_result(user_id, True)
        return f"You defeated {wild_pokemon} with {player_pokemon}!"
    else:
        update_battle_result(user_id, False)
        return f"{wild_pokemon} defeated your {player_pokemon}..."

def random_wild_encounter(zone_data):
    if not zone_data.get("can_battle"):
        return None
    return random.choice(zone_data["wild_pokemon"])
