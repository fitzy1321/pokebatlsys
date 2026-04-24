default:
    @just --list

open-marimo:
    marimo edit --sandbox data/first_gen_marimo_notebook.py --watch
