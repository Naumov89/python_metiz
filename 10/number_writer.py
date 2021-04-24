
import json

numbers = [2, 3, 5, 7, 9, 11, 13]

filename = "/home/oleksandr/Desktop/python_work/10/numbers.json"

with open(filename, 'w') as f:
    json.dump(numbers, f)    