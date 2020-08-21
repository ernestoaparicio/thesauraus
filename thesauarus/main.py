import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def get_matches(word):
    for match in get_close_matches(word, data.keys(), n=3, cutoff=0.8):
        print_definition(match)


def print_definition(key):
    if key in data:
        print(f"Did you mean {key}? {data[key]}")
    else:
        print(f"{key} doesn't exist.")


get_matches(input("Enter word: ").lower())
