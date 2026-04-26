# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.3",
#     "polars==1.40.1",
#     "requests==2.33.1",
# ]
# ///

import marimo

__generated_with = "0.23.3"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import requests
    import os

    return mo, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Pokemon Data

    https://pokeapi.co/docs/v2

    Let's figure out what data I need to make a simple battle system replica of a Pokemon game, i.e. turn based pokemon fights. Needs to support different types of moves, and moves with stages and affects, etc.

    First, start with gen 1 systems, no fancy abilities or held items or super advance stuff, just simple gen 1 pokemon battle.


    Let's map out which json fields I need from this api

    I know I need all the Pokemon of each generation

    - [ ] Pokemon
        - [ ] id
        - [ ]
    - [ ] Moves
        - [ ]
    """)
    return


@app.cell
def _(requests):
    r = requests.get("https://pokeapi.co/api/v2/pokemon/1")
    if not r.ok:
        print(f"Error fetching pokemon: {r.status_code} {r.raw}")
        exit(1)

    data = r.json()
    data
    return


if __name__ == "__main__":
    app.run()
