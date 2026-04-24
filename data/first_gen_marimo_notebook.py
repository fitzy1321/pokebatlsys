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
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl

    df = pl.read_csv("data/FirstGenPokemon.csv")

    df
    return


@app.cell
def _():
    import requests

    r = requests.get("https://pokeapi.co/api/v2/pokemon/1")
    if not r.ok:
        print(f"Error fetching pokemon: {r.status_code} {r.raw}")
        exit(1)

    data = r.json()
    data["stats"]
    return


if __name__ == "__main__":
    app.run()
