#include <stdio.h>

// Gen 1 Type Enum (matches internal game values)
typedef enum {
    NORMAL   = 0x00,
    FIGHTING = 0x01,
    FLYING   = 0x02,
    POISON   = 0x03,
    GROUND   = 0x04,
    ROCK     = 0x05,
    BIRD     = 0x06, // Unused placeholder
    BUG      = 0x07,
    GHOST    = 0x08,
    // 0x09 - 0x13: Unused "Normal" placeholders
    FIRE     = 0x14,
    WATER    = 0x15,
    GRASS    = 0x16,
    ELECTRIC = 0x17,
    PSYCHIC  = 0x18,
    ICE      = 0x19,
    DRAGON   = 0x1A
} PokemonType;

// Structure for a single Pokémon in the party or box
typedef struct {
    unsigned int species;        // Species ID
    unsigned int hp;             // Current HP (low byte)
    unsigned int level;          // Current level
    unsigned int status;         // Status condition (e.g., sleep, poison)
    unsigned int type1;          // Primary type (PokemonType)
    unsigned int type2;          // Secondary type (PokemonType)
    unsigned int catch_rate;     // Catch rate (for wild Pokémon)
    unsigned int moves[4];       // Four move IDs
    unsigned int dv;            // Determinant Values (combined Attack, Defense, Speed, Special)
    unsigned int max_hp;        // Max HP
    unsigned int attack;        // Attack stat
    unsigned int defense;       // Defense stat
    unsigned int speed;         // Speed stat
    unsigned int special;       // Special stat (used for Spc Attack/Defense)
    unsigned int pp[4];          // PP for each move
} Pokemon;

// Structure for the player's party
typedef struct {
    unsigned int count;          // Number of Pokémon in party (0-6)
    Pokemon pokemon[6];     // Array of 6 Pokémon
    // Followed by box data in memory
} PartyData;

int main() {
    printf("Welcome to Pokémon Battle CLI!\n");

    return 0;
}
