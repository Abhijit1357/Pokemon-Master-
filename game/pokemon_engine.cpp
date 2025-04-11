#include <string>
#include <cstdlib>
#include <ctime>

extern "C" {
    const char* start_battle(const char* player_pokemon, const char* wild_pokemon) {
        srand(time(0));
        int result = rand() % 2;
        return result == 0 ? "win" : "lose";
    }
}
