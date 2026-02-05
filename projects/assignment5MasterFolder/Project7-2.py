#! usr/bin/env python3
# NTS - COMPLETED 
import random

def display_title():
    print("The Wizard Inventory Program")



def display_menu():
    print("COMMAND MENU")
    print("walk - walk down the path")
    print("show - Show all items")
    print("drop - drop an item")
    print("exit - Exit program\n")



def show(list):
    index = 1
    for x in list:
        print(f"{index}. {x}")
        index += 1
    


def walk(list):
    with open("wizard_all_items.txt", "r") as file:
        items = file.read().splitlines()
        unequipedItems = [item for item in items if item not in list]
        
        option = random.choice(unequipedItems)
        print(f"While walking down a path, you see a {option}")

        pickUp = input("would you like to grab it? (y/n): ").lower()
        if pickUp == "y" and len(list) < 4:
            list.append(option)
            print(f"you picked up {option}")
            update_file(list)
        elif pickUp == "y" and len(list) == 4:
            print("you can't carry any more items. Drop something first.")
        else: 
            print(f"You did not pick up the {option}")



def drop(list):
    while True:

        number = int(input("Number: "))

        if 0 < number <= len(list):
            print(f'{list[number-1]} was dropped.')
            list.remove(list[number-1])

            with open("wizard_inventory.txt", "w") as file:
                for i in list:
                    file.write(f"{i}\n")
            break
        else:
            print("this is not a valid option! Please try again")



def update_file(list):
    with open("wizard_inventory.txt", "w") as file:
        for i in list:
            file.write(f"{i}\n")



def menu(list):
    menuOption = input("\nCommand: ").lower()

    if menuOption == "walk":
        walk(list)
    elif menuOption == "show":
        show(list)
    elif menuOption == "drop":
        drop(list)
    elif menuOption == "exit":
        update_file(list)
    return menuOption


    
def main():

    with open("wizard_inventory.txt", "r") as file:
        inventory = file.read().splitlines()

    display_title()
    display_menu()

    while True:
        option = menu(inventory)
        if option == "exit":
            break

if __name__ == "__main__":
    main()
    


