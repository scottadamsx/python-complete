#! usr/bin/env python3

# Project 3.3 - Change Calculator

def main(): 
    # print title
    print("Change Calculator")

    while True:
        # prompt user for input (int)
        cents = int(input("\nEnter number of cents (0-99): "))

        quarters = cents // 25               # integer division for # of coins
        cents %= 25                          # get remainder of cents
        print(f"\nQuarters: {quarters}")     # print output

        dimes = cents // 10
        cents %= 10
        print(f"Dimes:    {dimes}")

        nickels = cents // 5
        cents %= 5
        print(f"Nickels:  {nickels}")
        print(f"Pennies:  {cents}")

        # ask user to continue
        contin = input("\nContinue? (y/n): ").lower()
        if contin != "y":
            break

    print("\nBye!")
if __name__ == "__main__":
    main()
