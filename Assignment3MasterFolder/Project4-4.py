#! usr/bin/env python3

import sales

def display_title():
    print("Sales Tax Calculator\n")


 
def grab_input():
    print("ENTER ITEMS (ENTER 0 TO END)")
    item_cost = ""
    total = 0
    while item_cost != 0:
        item_cost = float(input("Cost of item: "))
        total += round(item_cost, 2)

    return total

 

def calculations(total):
    tax_amount = round(sales.get_tax_amount(total), 2)
    total_after_tax = round(sales.get_total_cost(total), 2)

    print(f"Total:\t\t {total}")
    print(f"Sales tax:\t {tax_amount}")
    print(f"Total after tax: {total_after_tax}")



def main():

    display_title()

    while True:
        total = grab_input()
        calculations(total)

        go_again = input("\nAgain? (y/n): ").lower()
        if go_again != "y":
            break

    print("\nThanks, bye!")


if __name__ == "__main__":
    main()