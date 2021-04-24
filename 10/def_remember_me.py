
import json

################################################################################# 1

# def greet_user():
#     """Приведствует пользователя по имени!"""
#     filename = "/home/oleksandr/Desktop/python_work/10/new_username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username}!")
#     else:
#         print(f"Welcome back, {username}!")

# greet_user()

################################################################################### 2

# def get_stored_username():
#     """Получает имя пользователя если оно есть."""
#     filename = "/home/oleksandr/Desktop/python_work/10/new_username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def greet_user():
#     """Приветствует пользователя по имени."""
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username}!")

# greet_user()

################################################################################### 3

def get_stored_username():
    """Получает имя пользователя если оно есть."""
    filename = "/home/oleksandr/Desktop/python_work/10/n_username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = "/home/oleksandr/Desktop/python_work/10/n_username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Приведствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()