
from random import choices

lottery = [1, 2, 5, 6, 8, 10, 38, 24, 58, 19, 'a', 'f', 'y', 'o', 't']
my_ticket = [2, 8, 'a', 't']
number_combinations = 0

print(f"My ticket: {my_ticket}")

while True:
    win_lottery = choices(lottery, k=4)
    my_ticket != win_lottery
    number_combinations +=1
    if my_ticket == win_lottery:
        print('You win!')
        print(f"Number combinations: {number_combinations}")
        break

print(f"Wining combinations: {win_lottery}")