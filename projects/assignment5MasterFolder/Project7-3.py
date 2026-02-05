#! usr/bin/env python3
import csv

def display_title():
    print("Contact Manager\n")

def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")




def read_contacts():
    contacts = []
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)

    return contacts
    


def list(contacts):
    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact[0]}")



def view(contacts):
    listIdx = int(input("Number: ")) - 1
    if listIdx in range(len(contacts)):
        contact = contacts[listIdx]
        print(f"Name: {contact[0]}")
        print(f"Email: {contact[1]}")
        print(f"Phone Number: {contact[2]}\n")



def add(contacts):
    name = input("Name: ")
    email = input("Email: ")
    Phone = input("Phone: ")

    contact = [name, email, Phone]
    contacts.append(contact)
    print(f"{name} was added.")

    update_list(contacts)



def update_list(contacts):
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)



def delete(contacts):
    while True:

        number = int(input("Number: ")) - 1

        if 0 < number <= len(contacts):
            print(f'{contacts[number][0]} was dropped.')
            contacts.remove(contacts[number])
            update_list(contacts)
            break

        else:
            print("this is not a valid option! Please try again")


def main():
    
    contacts = read_contacts() 
    display_title()
    display_menu()


    while True:
        option = input("Command: ").lower()

        if option == "list":
            list(contacts)
        elif option == "view":
            view(contacts)
        elif option == "add":
            add(contacts)
        elif option == "del":
            delete(contacts)
        elif option == "exit":
            print("bye!")
            break
        else:
            print("this is not a valid command, please see valid options")
            display_menu()



    
 

if __name__ == "__main__":
    main()