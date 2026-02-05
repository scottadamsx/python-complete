#! usr/bin/env python3
# Project 2.3 - Tip Calculator

def main():
    # print title
    print("Tip Calculator\n")

    # prompt for cost of meal and tip percentage
    mealCost = float(input("Cost of meal: "))
    tipPercent = float(input("Tip Percent:  "))

    # perform calculations for tip amount and total amount
    tipAmount = round(mealCost * (tipPercent / 100), 2)
    totalCost = round(mealCost + tipAmount, 2)

    # display output of tipAmount and Total Amount
    print(f"\nTip Amount: {tipAmount}")
    print(f"Total amount: {totalCost}")

    #NTS - code completed and debugged
if __name__ == "__main__":
    main()

