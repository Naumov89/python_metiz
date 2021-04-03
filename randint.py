
from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def show_sides(self):
        print(f"Now is: {self.sides}")

    def roll_die(self):
        self.sides = randint(1, 6)
        print(f"You roled: {self.sides}")

    def dice_roll(self):
        randoms = []
        for dice in range(10):
            randoms.append(randint(1, 6))
        print(f"You roled: {randoms}")

my_die = Die()

my_die.show_sides()
my_die.roll_die()
my_die.dice_roll()
