
pizza = {
    'crust': 'trick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following toppings:")                       # ecli mnogo teksta mogno zapisuvat tak

for topping in pizza['toppings']:
    print("\t" + topping)