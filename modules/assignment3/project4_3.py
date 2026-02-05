#! usr/bin/env python3
# Feet and Meters Converter
from .conversions import *

def display_title():
    print("Feet and Meters Converter")

def display_menu():
    print("Conversions Menu:\na. Feet to Meters\nb. Meters to Feet")

def main():

    display_title()
    
    while True:    
        display_menu()

        while True:
            choice = input("Select a conversion (a/b): ").lower()
            if choice == "a":
                feet = float(input("\nEnter feet: "))
                print(f"{feet_to_meters(feet)} meters")
                break
            elif choice == "b":
                meters = float(input("\nEnter meters: "))
                print(f"{meters_to_feet(meters)} feet")
                break
            else: 
                print("This is not a valid option")
                display_menu()

        contin = input("\nwould you like to do another conversion? (y/n): ").lower()
        if contin != "y":
            break

    print("Bye!")
if __name__ == "__main__":
    main()
    
    
