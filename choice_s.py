
from random import choice, choices

lottery = [1, 2, 5, 6, 8, 10, 38, 24, 58, 19, 'a', 'f', 'y', 'o', 't']
win_lottery = []

for win_number in range(5):
    win_lottery.append(choice(lottery))

print(f"Winning ticket: {win_lottery}")

############################################################################

lottery = [1, 2, 5, 6, 8, 10, 38, 24, 58, 19, 'a', 'f', 'y', 'o', 't']
my_ticket = choices(lottery, k=4)
print(f"Winning tickets: {my_ticket}")
