import csv
import os
import time

import requests


def fetch(url, retries=3):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r.json()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(1)


def fetch_gen(gen, id_range, writer):
    print(f"\n── Gen {gen} ──────────────────")
    for pid in id_range:
        p = fetch(f"https://pokeapi.co/api/v2/pokemon/{pid}")

        stats = {s["stat"]["name"]: s["base_stat"] for s in p["stats"]}  # type: ignore
        types = [
            t["type"]["name"].capitalize()
            for t in sorted(p["types"], key=lambda t: t["slot"])  # type: ignore
        ]

        writer.writerow(
            {
                "id": pid,
                "name": p["name"].capitalize(),  # type: ignore
                "type1": types[0],
                "type2": types[1] if len(types) > 1 else "",
                "hp": stats["hp"],
                "atk": stats["attack"],
                "def": stats["defense"],
                "spa": stats["special-attack"],
                "spd": stats["special-defense"],
                "spe": stats["speed"],
            }
        )
        print(f"  #{pid:03d} {p['name'].capitalize()}")  # type: ignore
        time.sleep(0.1)  # be polite to the API


if __name__ == "__main__":
    GENS = {
        1: range(1, 152),  # Bulbasaur → Mew
        2: range(152, 252),  # Chikorita → Celebi
        3: range(252, 387),  # Treecko   → Deoxys
    }
    FIELDS = ["id", "name", "type1", "type2", "hp", "atk", "def", "spa", "spd", "spe"]
    OUT = "data"
    os.makedirs(OUT, exist_ok=True)

    print("Fetching data from pokeapi\n\n")

    for gen, id_range in GENS.items():
        path = f"{OUT}/gen{gen}.csv"
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()
            fetch_gen(gen, id_range, w)
        print(f"→ wrote {path}")

    print("\ndone.")
