#! usr/bin/env python3
# Dice Roller

import random

def display_title():
    print("Dice Roller\n")



def roll_die():
    roll = random.randint(1,6)
    return roll



def check_for_special_roll(roll1, roll2):
    if roll1 == 6 and roll2 == 6:
        print("Boxcars!")
    elif roll1 == 1 and roll2 == 1:
        print("Snake Eyes!")



def main():

    display_title()

    while True:
        roll1 = roll_die()
        roll2 = roll_die()
        total = roll1 + roll2
        print(f"Die 1: {roll1}\nDie 2: {roll2}\nTotal: {total}")
        check_for_special_roll(roll1, roll2)

        go_again = input("\nRoll again? (y/n): ")
        if go_again != "y":
            break

if __name__ == "__main__":
    main()

