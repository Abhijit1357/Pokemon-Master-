from config import MAP_WIDTH, MAP_HEIGHT, START_X, START_Y
from database.db import get_player, update_player_location

# Simple zone layout
zones = {
    (2, 2): "You are in the Center Town. A peaceful place.",
    (2, 1): "A dense forest surrounds you.",
    (2, 3): "You see a tall mountain path.",
    (1, 2): "A river flows gently here.",
    (3, 2): "A wild field filled with tall grass. Pokémon may appear!"
}

def get_current_zone_description(user_id):
    player = get_player(user_id)
    x, y = player.get("x", START_X), player.get("y", START_Y)
    return zones.get((x, y), "You are in an unknown area.")

def move_player(user_id, direction):
    player = get_player(user_id)
    x, y = player.get("x", START_X), player.get("y", START_Y)

    if direction == "⬆️":
        y = max(0, y - 1)
    elif direction == "⬇️":
        y = min(MAP_HEIGHT - 1, y + 1)
    elif direction == "⬅️":
        x = max(0, x - 1)
    elif direction == "➡️":
        x = min(MAP_WIDTH - 1, x + 1)

    update_player_location(user_id, x, y)
    return zones.get((x, y), "You moved into a mysterious place...")
