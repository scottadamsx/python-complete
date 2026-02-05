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
    monthlySales = []
    with open(fileName, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            monthlySales.append(row)

    # loop through every month and change the sales string to an int
    for month in monthlySales:
        month[1] = int(month[1])
    return monthlySales



def update_file(monthlySales,fileName):
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file)
        for row in monthlySales:
            row[1] = str(row[1])
            writer.writerow(row)

    # change them back to int to allow for calculations
    for row in monthlySales:
            row[1] = int(row[1])



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
        match = False
        choice = input("Three-letter Month: ").capitalize()
        for month in monthlySales:
            if choice == month[0]:
                match = True
                break
                
        if match == True:
            break 
        else:       
            print("This is not a valid month, please enter the correct 3 letter month")

    month[1] = int(input("Sale Amount: "))
    print(f"Sale amount for {month[0]} was motified")
    update_file(monthlySales,fileName)



def main():

    fileName = "monthly_sales.csv"

    print("Monthly Sales Program\n")
    monthlySales = read_from_file(fileName)
    display_menu()
    choose_from_commands(monthlySales,fileName)

if __name__ == "__main__":
    main()