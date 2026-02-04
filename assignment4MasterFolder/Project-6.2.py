#! usr/bin/env python3
# NTS - COMPLETED 

def display_title():
    print("The Wizard Inventory Program")

def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab in item")
    print("edit - Edit an item")
    print("exit - Exit program\n")

def show(list):
    index = 1
    for x in list:
        print(f"{index}. {x}")
        index += 1
    
def edit(list):
    number = int(input("Number: "))
    updatedName = input("Updated name: ")
    list[number - 1] = updatedName
    print(f"item number {number} was updated.")

def drop(list):
    number = int(input("Number: "))
    print(f'{list[number-1]} was dropped.')
    list.remove(list[number-1])
    

def grab(list):
    if len(list) == 4:
        print("You can't carry any more items. Drop something first.")
    else:    
        name = input("Name: ")
        list.append(name)
        print(f"{name} was added.")

def menu(list):
    menuOption = input("\nCommand: ").lower()

    if menuOption == "show":
        show(list)
    elif menuOption == "grab":
        grab(list)
    elif menuOption == "edit":
        edit(list)
    elif menuOption == "drop":
        drop(list)
    return menuOption

    
def main():

    inventory = ["wooden staff", "wizard hat", "cloth shoes", "potion of invisibility"]

    display_title()
    display_menu()

    while True:
        option = menu(inventory)
        if option == "exit":
            break
    
    print("thanks for playing :)")


if __name__ == "__main__":
    main()
    



    



