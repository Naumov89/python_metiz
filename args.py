
def make_pizza(*topings):    #  * - proizvolnoe kolichestvo elementov(*args- chasto ispolzuyut)
    print(topings)

make_pizza('papperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

###################################################################

def make_pizza(*topings):
    print("\nMaking a pizza with the following toppings:")
    for toping in topings:
        print(f" - {toping}")

make_pizza('papperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

####################################################################

def make_pizza(size, *topings):
    print(f"\nMaking {size}-inch pizza with the following toppings:")
    for toping in topings:
        print(f" - {toping}")

make_pizza(14, 'papperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')