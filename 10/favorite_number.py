
import json

favorite_number = input("Give me your favorite number: ")
filename = "/home/oleksandr/Desktop/python_work/10/favorite_number.json"

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print("I memorized your favorite number!")
