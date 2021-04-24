
import json

filename = "/home/oleksandr/Desktop/python_work/10/favorite_number.json"

with open(filename) as f:
    favorite_number = json.load(f)
    print(f"Your favorite number is {favorite_number}!")