
import json

filename = "/home/oleksandr/Desktop/python_work/10/username.json"
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")