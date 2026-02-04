# usr/bin/env python3

# import random
import random

while True:

    # user chooses range
    startNum = int(input("Choose begginning of number range: "))
    endNum = int(input("Choose end of number range: "))
    number = random.randint(startNum, endNum)

    # initialize variables
    guess = 0
    numberOfGuesses = 0


    while guess != number:
        guess = int(input("Guess the number: "))
        numberOfGuesses += 1
        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
       
    print(f"Congradulations! you guessed the number in {numberOfGuesses} guesses :)")

    # ask user to continue
    contin = input("would you like to continue? (y/n): ").lower()
    if contin != "y":
        break
    
print("Bye!")
    
