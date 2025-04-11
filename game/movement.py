from config import MAP_WIDTH, MAP_HEIGHT
from database.db import get_player, update_player_location

def can_move_to(x, y):
    return 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT

def move(user_id, direction):
    player = get_player(user_id)
    x, y = player.get("x"), player.get("y")

    if direction == "⬆️":
        new_x, new_y = x, y - 1
    elif direction == "⬇️":
        new_x, new_y = x, y + 1
    elif direction == "⬅️":
        new_x, new_y = x - 1, y
    elif direction == "➡️":
        new_x, new_y = x + 1, y
    else:
        return x, y

    if can_move_to(new_x, new_y):
        update_player_location(user_id, new_x, new_y)
        return new_x, new_y
    return x, y
