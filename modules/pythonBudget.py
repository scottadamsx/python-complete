#! usr/bin/env python3
#Scott's Python Budget
from datetime import datetime, timedelta
import csv

#===============================================================================================================================
def display_title():
    print("SCOTT's BUDGET APPLICATION")

#===============================================================================================================================
def menu(expensesList, values):
    print("\nMENU OPTIONS")
    print("1. View Expenses")
    print("2. Overview")
    print("3. Add Expense")
    print("4. Remove Expense")
    print("5. Add Pay Amount")
    print("6. Future Savings Calculator")
    print("7. Edit Values")
    print("8. Exit")
    menuOption = get_menu_option(expensesList, values)
    return menuOption

#===============================================================================================================================
def get_menu_option(expensesList, values):
    try:
        while True:
            option = int(input(f"\n okay {values[0]}, Pick an option [1-7]: "))

            if option == 1:
                print("option 1 chosen")
                view_expenses(expensesList)
                break
            elif option == 2:
                print("option 2 chosen")
                show_overview(expensesList)
                break
            elif option == 3:
                print("option 3 chosen")
                add_expense(expensesList)
                break
            elif option == 4:
                print("option 4 chosen")
                remove_expense(expensesList)
                break
            elif option == 5:
                print("option 5 chosen")
                add_pay_amount()
                break
            elif option == 6:
                print("option 6 chosen")
                future_savings_calculator()
                break
            elif option == 7:
                print("option 7 chosen")
                edit_values(values)
                break
            elif option == 8:
                print("option 8 chosen")
                break
            else:
                print("This is not a valid option, Try again")
        return option

    except ValueError:
        print("*Not a valid integer, please try again*")
    except Exception as e:
        print(type(e), e)

#===============================================================================================================================
def view_expenses(expensesList):
    # Prompt user for end date
    endDate = input("Enter an end date for the list (YYYY-MM-DD): ")
    try:
        # Parse endDate into a datetime object
        endDate = datetime.strptime(endDate, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return  # Exit if date is invalid

    reoccuringInstancesList = []

    # Handle recurring expenses
    for expense in expensesList:
        if expense["reoccuring"]:
            repeatValue = expense["repeat"]

            # Ensure expense date is a datetime object
            if isinstance(expense["date"], str):
                expense_date = datetime.strptime(expense["date"], '%Y-%m-%d')
            else:
                expense_date = expense["date"]

            while True:
                expense_date += timedelta(days=repeatValue)
                if expense_date > endDate:
                    break
                reoccuringInstancesList.append({
                    "name": expense["name"],
                    "amount": expense["amount"],
                    "date": expense_date.strftime('%Y-%m-%d'),  # Convert back to string
                    "reoccuring": expense["reoccuring"],
                    "repeat": repeatValue,
                })

    # Combine and sort all expenses by date
    allExpenses = expensesList + reoccuringInstancesList
    allExpenses = sorted(allExpenses, key=lambda x: datetime.strptime(x["date"], '%Y-%m-%d'))

    # Display expenses
    for expense in allExpenses:
        print(f"Expense: {expense['name']}, Date: {expense['date']}, Amount: {expense['amount']}")

def edit_values(values):
    print(f"current savings value: {values[0]}")
    print(f"current debt value: {values[1]}")
    print(f"current spending value: {values[2]}")
    print(f"current investments value: {values[3]}")

    savings = input("Please enter new savings value: ")
    debt = input("Please enter new debt value: ")
    toy = input("Please enter new spending value: ")
    investments = input("Please enter new investments value: ")
    values[0] = savings
    values[1] = debt
    values[2] = toy
    values[3] = investments
    return values
#===============================================================================================================================
def add_expense(expensesList):
    expenseName = str(input("What is this expense called: ")).strip().lower()
    expenseAmount = round(float(input("How much is this expense: ")), 2)
    date_input = input("Enter a date (YYYY-MM-DD): ")
    try:
        expenseDate = datetime.strptime(date_input, '%Y-%m-%d')
        print("Entered date:", expenseDate)
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    while True:
        reoccuringOrNot = input("Is this a reoccuring expense? (y/n):").lower()
        if reoccuringOrNot == "y":
            reoccuringOrNot = True
            while True:
                repeat = input("is this a monthly (m), biweekly (b) or once a year (y): ")
                if repeat == "m":
                    repeatValue = 30
                    break
                elif repeat == "b":
                    repeatValue = 14
                    break
                elif repeat == "y":
                    repeatValue = 365
                    break
                else:
                    print("*Not a valid option*")
            break
        elif reoccuringOrNot == "n":
            reoccuringOrNot = False
            repeatValue = 0
            break
        else:
            print("invalid option")

    expense = {
        "name": expenseName,
        "amount": expenseAmount,
        "date": expenseDate.strftime('%Y-%m-%d'),  # Save date as a string for consistency
        "reoccuring": reoccuringOrNot,
        "repeat": repeatValue
    }
    expensesList.append(expense)
    print(f"Successfully added your new expense: {expense['name']} for {expense['amount']}")

#===============================================================================================================================
def remove_expense(expensesList):
    expenseName = input("Enter the name of the expense to remove: ").strip().lower()
    removed = False
    for expense in expensesList:
        if expense["name"] == expenseName:
            expensesList.remove(expense)
            print(f"Successfully removed the expense: {expenseName}")
            removed = True
            break
    if not removed:
        print(f"Expense with the name '{expenseName}' not found.")

#===============================================================================================================================
def show_overview(expensesList):
    total_expenses = sum(expense["amount"] for expense in expensesList)
    print(f"Total number of expenses: {len(expensesList)}")
    print(f"Total expense amount: ${total_expenses:.2f}")

#===============================================================================================================================
def add_pay_amount():
    pay = float(input("Enter your pay amount: "))
    print(f"Your pay amount of ${pay:.2f} has been recorded. (Feature not fully implemented yet.)")

#===============================================================================================================================
def future_savings_calculator():
    print("Future savings calculator feature is not yet implemented.")

#===============================================================================================================================
def load_data(FILENAME):
    expensesList = []
    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                row["reoccuring"] = row["reoccuring"] == "True"
                row["repeat"] = int(row["repeat"])
                expensesList.append(row)
    except FileNotFoundError:
        print(f"{FILENAME} not found. Starting with an empty expense list.")
    return expensesList

#===============================================================================================================================
def save_data(FILENAME, expensesList):
    try:
        with open(FILENAME, "w", newline="") as file:
            fieldnames = ["name", "amount", "date", "reoccuring", "repeat"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expensesList)
        print(f"Data saved to {FILENAME}")
    except Exception as e:
        print(f"Error saving data: {e}")




def load_values(FILENAME):
    values = []
    with open(FILENAME) as file:
        reader = csv.reader(file)
        for row in reader:
            values.append(row)
        name = values[0]
        savingsValue = values[1]
        debtValue = values[2]
        spendingValue = values[3]
        investmentsValue = values[4]
        print(name, savingsValue, debtValue, spendingValue, investmentsValue)
    return values

def save_values(FILENAME, values):
    with open(FILENAME, "w") as file:
        writer = csv.writer(file)
        for i in values:
            writer.writerow()
    print(f"values saved to file!")

        


#===============================================================================================================================
def main():
    FILENAME = "expenses.csv"
    display_title()
    expensesList = load_data("expenses.csv")
    values = load_values("values.csv")

    while True:
        menuOption = menu(expensesList, values)
        if menuOption == 8:
            save_data(FILENAME, expensesList)
            save_values(FILENAME, values)
            break

    print("bye!")

if __name__ == "__main__":
    main()
