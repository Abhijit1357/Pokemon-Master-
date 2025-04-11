import ctypes
import os

# Load the shared library
lib_path = os.path.join(os.path.dirname(__file__), "pokemon_engine.so")
battle_lib = ctypes.CDLL(lib_path)

# Set return type
battle_lib.start_battle.restype = ctypes.c_char_p

def start_battle(player_pokemon, wild_pokemon):
    result = battle_lib.start_battle(player_pokemon.encode(), wild_pokemon.encode())
    return result.decode()
