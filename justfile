default:
    @just --list

open-marimo:
    marimo edit --sandbox data/pokedata_notebook.py --watch

compile-c:
    @mkdir -p c/build
    cc -std=c11 -Wall -Werror c/src/main.c -o c/build/main
