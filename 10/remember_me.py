
import json

username = input("What is your name? ")

filename = "/home/oleksandr/Desktop/python_work/10/username.json"
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")