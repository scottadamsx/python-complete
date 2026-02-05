#! usr/bin/env python3

import csv
import sys

# Displays menu in 5 print statements
def display_menu():
    print("Command Menu")
    print("monthly - View monthly sales")
    print("yearly - View yearly sales")
    print("edit - Edit sales for a month")
    print("Exit - Exit program\n")
  



def choose_from_commands(monthlySales,fileName):
    # loop until valid input
    while True:

        command = input("Command: ").lower()
        if  command == "monthly":
            monthly(monthlySales)
        elif command == "yearly":
            yearly(monthlySales)
        elif command == "edit":
            edit(monthlySales,fileName)
        elif command == "exit":
            print("\nbye!\n")
            sys.exit()
        else:
            print("this is not a valid command,  please try again...")


        
def read_from_file(fileName):
    monthlySales = {}
    with open(fileName, newline="") as file:
        for row in file:
            row = row.replace("\r\n", "").split("\t")
            print(row)
            monthlySales[row[0]] = row[1]
    print(monthlySales)
    return monthlySales
            



def update_file(monthlySales,fileName):
    with open(fileName, "w") as file:
        for month,sale in monthlySales.items():
            file.write(f"{month}\t{sale}\r")

    # change them back to int to allow for calculations
    for row in monthlySales:
            int(monthlySales[row])



def monthly(monthlySales):
    for month in monthlySales:
        print(f"{month[0]} - {round(month[1], 2)}")



def yearly(monthlySales):
    total = 0
    for row in monthlySales:
        total += row[1]

    average = round(total / 12, 2)

    print(f"Yearly total:\t {total}")
    print(f"Monthly average:{average}")



def edit(monthlySales,fileName):
    while True:
        choice = input("Three-letter Month: ").capitalize()
        if choice in monthlySales:
            monthlySales[choice] = int(input("Sale Amount: "))
            print(f"Sale amount for {choice} was motified")
            update_file(monthlySales,fileName)
            break
        
        else:       
            print("This is not a valid month, please enter the correct 3 letter month")




def main():

    fileName = "monthly_sales.txt"

    print("Monthly Sales Program\n")
    monthlySales = read_from_file(fileName)
    display_menu()
    choose_from_commands(monthlySales,fileName)

if __name__ == "__main__":
    main()