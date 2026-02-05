# usr/bin/env python3

# Project 3.4 - Shipping Calculator

def main(): 
    # print title
    border = "========================================================"
    print(border)
    print("Shipping Calculator")
    print(border)

    while True:

    # validate input to be positive
        while True:
            cost_of_items_ordered = float(input("Cost of items ordered:  "))
            if cost_of_items_ordered >= 0:
                break
            else:
                print("You must enter a positive number. Please try again.")

        # determine shipping cost
        if cost_of_items_ordered < 30:
            shipping_cost = 5.95
        elif 30.00 <= cost_of_items_ordered <= 49.99:
            shipping_cost = 7.95
        elif 50.00 <= cost_of_items_ordered <= 74.99:
            shipping_cost = 9.95
        else:
            shipping_cost = 0.00

        # display output
        print(f"Shipping cost:\t\t{shipping_cost}")
        print(f"Total cost:\t\t{round(shipping_cost + cost_of_items_ordered, 2)}")

        # ask user to continue
        contin = input("\nContinue? (y/n): ").lower()
        print(border)
        if contin != "y":
            break


    print("Bye!")
if __name__ == "__main__":
    main()
