# Pokémon Battle System

I thought I'd build a silly project.

Replicate a monster style fighting system, the back and forth, type based, etc.

I'll probably go with gen 1 - 3, since that's what I played, and I'm not trying to accuratley simulate anything.

**THIS IS A FUNNY PROJECT. USE AT YOUR OWN RISK!!**

## Requirements

- [ ] Pokemon data
  - id ?
  - name
  - properties
    - attack
    - defense
    - speed
    - special(s)
    - etc
  - type of pokemon
  - move list
    - each move has type
    - each has pp per pokemon
  - status effects
  - hp
  - is_wild or is_owned ? i.e. is a wild pokemon and can capture vs trainer owned pokemon
  - do I care about level right now?
- [ ] Top level battle system
  - takes in 2-4 pokemon
  - prefered to be behind some generic interface or something. i.e. the battle doesn't actually care what pokemon are on the field.
  - arena effects
  - determine who goes first
  - determine phase order
  - able moves
- [ ] Moves
  - switch pokemon
  - select move from pokemon move list
    - moves have type
    - can able status effects
    - can have side effects
    - can have stages (fly, surf, dig, rollout, etc)
    - can have multipliers from pokemons typing and move typing
  - use item
    - pokeball
    - health / recovery item
    - etc
  - try to run

How does this data get saved per pokemon, and per instance in a user's roaster? And per opponent pokemon list?

## Data

Gen 1 pokemon data source: <https://www.kaggle.com/datasets/dizzypanda/gen-1-pokemon?resource=download/>
