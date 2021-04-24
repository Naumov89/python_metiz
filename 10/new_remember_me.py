
import json

"""
Программа загружает имя пользователяб если оно было сохранено ранее.
В противном случае она запрашивает имя пользователя и сохраняет его.
"""
filename = "/home/oleksandr/Desktop/python_work/10/new_username.json"

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")