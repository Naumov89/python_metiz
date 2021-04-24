
import json

filename = "/home/oleksandr/Desktop/python_work/10/numbers.json"

with open(filename) as f:
    numbers = json.load(f)

print(numbers)