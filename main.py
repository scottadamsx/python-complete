#! usr/bin/env python3
# Project2.1 - MAIN APP 

import time 

def timer():
    print("")
    secs = 5
    while secs > 0:
        time.sleep(1)
        print(f"back to menu in {secs} seconds...")
        secs -= 1


# Import the blackjack main module
#from modules.blackjack import main as blackjack_main

# Assignment 1 Imports
from modules.assignment1 import project2_1 as P21
from modules.assignment1 import project2_2 as P22
from modules.assignment1 import project2_3 as P23
from modules.assignment1 import project2_4 as P24
from modules.assignment1 import project2_5 as P25

# Assignment 2 Imports
from modules.assignment2 import project3_1 as P31
from modules.assignment2 import project3_2 as P32
from modules.assignment2 import project3_3 as P33
from modules.assignment2 import project3_4 as P34
from modules.assignment2 import project3_5 as P35
from modules.assignment2 import project3_6 as P36

# Assignment 3 Imports
from modules.assignment3 import project4_1 as P41
from modules.assignment3 import project4_2 as P42
from modules.assignment3 import project4_3 as P43
from modules.assignment3 import project4_4 as P44
from modules.assignment3 import project4_5 as P45
from modules.assignment3 import project4_6 as P46

# tipCalculatorGui Import
#from modules.tipCalculatorGui import main as GUI

# Wordle Imports
from modules.wordle_project import wordle_simulator_v1 as WDL
from modules.wordle_project import wordle_helper_Variant1 as WDH





def printTitle():
    print("SCOTTY's ALL IN ONE PROJECT DIRECTORY\n\nWelcome, "
          "user! I hope you enjoy these projects, "
          "I made them all in school and so its "
          "a big deal to see them all.")

def mainMenu():
    print("\nMAIN PROJECT DIRECTORY\nPlease enter a valid project code: ")
    print("BJ: BlackJack (broken)")
    print("GUI: My first Tkinter GUI")
    print("WDL: Wordle Simulator v1")
    print("WDH: Wordle Helper v1")
    print("P21: Resistration Form")
    print("P22: Paycheck Calculator")
    print("P23: Tip Calculator")
    print("P24: Price Size Comparison (32oz/64oz)")
    print("P25: Time Travel Calculator")
    print("P31: Letter Grade Calculator")
    print("P32: Tip Calculator")
    print("P33: Change Calculator (coins and cents)")
    print("P34: Shipping Calculator")
    print("P35: Table of Powers")
    print("P36: Guess The Number Game")
    print("P41: Even or Odd Checker")
    print("P42: Hike Calculator")
    print("P43: Feet and Meters Converter")
    print("P44: Sales Tax Calculator")
    print("P45: Dice Roller")
    print("P46: Get the Factors of a Number")
    print("Q: Quit")

    while True:
        option = input("\nWhat would you like to choose: ").upper()
        
        if option == "BJ":
#            blackjack_main.main()  # Runs the main() from blackjack/main.py
            mainMenu()  # Return to menu

        elif option == "GUI":
            #GUI.main()
            print("broken")
        
        # WORDLE PROJECTS ==============
        elif option == "WDL":
            WDL.main()

        elif option == "WDL":
            WDH.main()
        # ==============================

        # ASSIGNMENT 1 =================
        elif option == "P21":          
            P21.main()

        elif option == "P22":
            P22.main()

        elif option == "P23":
            P23.main()

        elif option == "P24":
            P24.main()

        elif option == "P25":
            P25.main()
        # ==============================
         
        # ASSIGNMENT 2 =================
        elif option == "P31":
            P31.main()

        elif option == "P32":
            P32.main()
            
        elif option == "P33":
            P33.main()

        elif option == "P34":
            P34.main()

        elif option == "P35":
            P35.main()

        elif option == "P36":
            P36.main()
        # =============================

        # ASSIGNMENT 3 ================
        elif option == "P41":
            P41.main()

        elif option == "P42":
            P42.main()
            
        elif option == "P43":
            P43.main()

        elif option == "P44":
            P44.main()

        elif option == "P45":
            P45.main()

        elif option == "P46":
            P46.main()
        # =============================
        

        elif option == "Q":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Please try again.")

        timer()
        mainMenu()

def main():
    printTitle()
    mainMenu()

if __name__ == "__main__":
    main()