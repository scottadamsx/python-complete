#! usr/bin/env python3

def display_title():
    print("Tip Calculator\n")



def grab_input():
    # get input for cost of meal
    print("INPUT")
    while True:
        try:
            costOfMeal = float(input("Cost of meal: "))
            if costOfMeal > 0:
                break
            else:
                print("Must be greater than 0. Please try again.")
        except ValueError:
            print("Must be a valid decimal number. Please try again.")
        except Exception as e:
            print(type(e), e)

    # get input for tip percent
    while True:

        try:
            tipPercent = int(input("Tip Percent: "))
            if tipPercent > 0:
                break
            else:
                print("Must be greater than 0. Please try again.")
        except ValueError:
            print("Must be a valid integer. Please try again.")

    return costOfMeal, tipPercent



# preform calculations to the user inputs
def perform_calculations(costOfMeal, tipPercent):
    tipAmount = round(costOfMeal * tipPercent / 100, 2)
    totalAmount = round(costOfMeal + tipAmount, 2)
    return tipAmount, totalAmount
    


# display the output 
def display_output(costOfMeal, tipPercent, tipAmount, totalAmount):
    print("\nOUTPUT")
    print(f"Cost of meal: {costOfMeal}")
    print(f"Tip percent:  {tipPercent}")
    print(f"Tip amount:   {tipAmount}")
    print(f"Total amount: {totalAmount}\n")



def main():

    display_title()
    costOfMeal, tipPercent = grab_input()
    tipAmount, totalAmount = perform_calculations(costOfMeal, tipPercent)
    display_output(costOfMeal, tipPercent, tipAmount, totalAmount)

if __name__ == "__main__":
    main()