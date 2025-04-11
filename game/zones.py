zones = {
    "town": {
        "desc": "You're in the Center Town. Visit shops, rest, or chat with other players.",
        "can_battle": False,
        "npc": ["healer", "shopkeeper"]
    },
    "forest": {
        "desc": "Tall trees surround you. Wild Pokémon may attack anytime!",
        "can_battle": True,
        "wild_pokemon": ["Pikachu", "Bulbasaur", "Caterpie"]
    },
    "mountain": {
        "desc": "The cold wind howls. Only the strong survive here.",
        "can_battle": True,
        "wild_pokemon": ["Onix", "Geodude"]
    },
    "river": {
        "desc": "The river is peaceful, but you spot ripples in the water...",
        "can_battle": True,
        "wild_pokemon": ["Magikarp", "Poliwag"]
    },
    "field": {
        "desc": "Open grassland. Perfect for finding new Pokémon.",
        "can_battle": True,
        "wild_pokemon": ["Rattata", "Oddish", "Pidgey"]
    }
}

def get_zone_info(x, y):
    zone_map = {
        (2, 2): "town",
        (2, 1): "forest",
        (2, 3): "mountain",
        (1, 2): "river",
        (3, 2): "field"
    }
    zone_id = zone_map.get((x, y), "unknown")
    return zones.get(zone_id, {"desc": "An uncharted zone.", "can_battle": False})
