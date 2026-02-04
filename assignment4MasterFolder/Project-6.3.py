#!usr/bin/env python3
# NTS - Complete

# fxn that displays the title
def display_title():
    print("Contact Manager\n")

# fxn that displays the command menu at the beginning of the program
def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - delete a contact")
    print("exit - Exit program")


# fxn for viewing the list of contacts
def list(contactList):
    for index, contact in enumerate(contactList):
        print(f"{index+1}. {contact[0]}")


# fxn for viewing a contact in the list
def view(contactList):
    while True:
        idx = int(input("Number: ")) - 1
        if idx in range(len(contactList)):
            contact = contactList[idx]
            print(f"Name: {contact[0]} Email: {contact[1]} Phone number: {contact[2]}")
            break
        else:
            print("invalid input, please try again")



# fxn for adding a new contact to contactList
def add(contactList):
    # grab input for newContact
    name = input("Name: ")
    email = input("Email: ")
    phoneNumber = input("Number: ")

    # create instance for newContact and add it to contactList
    newContact = [name, email, phoneNumber]
    contactList.append(newContact)
    print(f"{newContact[0]} was added")


# fxn for deleting a contact from contactList
def delete(contactList):
    while True:
        idx = int(input("Number: ")) - 1
        if idx in range(len(contactList)):
            deletedContact = contactList.pop(idx)
            print(f"{deletedContact[0]} was deleted")
            break
        else:
            print("invalid input, please try again")



def main():

    display_title()
    display_menu()

    contactList = [["Guido van Rossum", "guidovanrossum@gmail.com", "+44 90 6394 0554"],
                   ["Eric Idle", "eric.idle@ericidle.ca", "+44 20 7946 0958"]]

    while True:
        command = input("\nCommand: ").lower()

        if command == "list":
            list(contactList)
        elif command == "view":
            view(contactList)
        elif command == "add":
            add(contactList)
        elif command == "del":
            delete(contactList)
        elif command == "exit":
            break
        else:
            print("That was not a correct command, try again please...")

    print("bye!")

if __name__ == "__main__":

    main()