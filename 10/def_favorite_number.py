
import json

def get_stored_number():
    filename = "/home/oleksandr/Desktop/python_work/10/d_favorite_number.json"
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def new_number():
    favorite_number = input("Give me your favorite number: ")
    filename = "/home/oleksandr/Desktop/python_work/10/d_favorite_number.json"
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def greet_number():
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"Your favorite number is {favorite_number}!")  
    else:
        favorite_number = new_number()
        print("I memorized your favorite number!")    

greet_number()
