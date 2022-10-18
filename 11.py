# «Dice»

import random

def roll_of_dice():
    count_roll = 0

    while count_roll < 1000:
        number1 = random.randint(1, 6)
        print(number1)
        number2 = random.randint(1, 6)
        print(number2)
        sum_number = number1 + number2
        print("You have", sum_number)
        count_roll += 1

    return

roll_of_dice()
