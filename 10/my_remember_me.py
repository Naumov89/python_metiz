import json

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
    """
    Проверяет имя пользователя если оно верно, приведствует пользователя по имени.
    Если нет, запрашивает новое имя пользователя.
    """
    username = get_stored_username()
    name = input(f"Hello, you are - {username}. (y/n)? ")
    if name == 'y':
            print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()