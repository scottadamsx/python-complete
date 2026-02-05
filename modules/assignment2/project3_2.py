#! usr/bin/env python3

# Project 3.2 - Tip Calculator

def main(): 
    # print title
    print("Tip Calculator\n")

    # prompt for a cost of meal (only 2 decimal places)
    cost_of_meal = round(float(input("Cost of meal: ")), 2)

    # initialize list of percentages
    tip_percentages = [15, 20, 25]

    # for loop, using list to determine the results and output them
    for i in tip_percentages:
        tip_amount = cost_of_meal * (i / 100) 
        print(f"\n{i}%")
        print(f"Tip amount: {round(tip_amount, 2)}")
        print(f"Total amount: {round(cost_of_meal + tip_amount, 2)}")

if __name__ == "__main__":
    main()


