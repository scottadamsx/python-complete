#! usr/bin/env python3

# function that prints the module title
def print_title():
    print("Hike Calculator\n")

# function that converts miles to feet
def miles_to_feet(miles):
    feet = miles * 5280
    return round(feet)

def main():

    print_title()

    miles = float(input("How many miles did you walk?: "))
    print(f"You walked {miles_to_feet(miles)} feet.")


if __name__ == "__main__":
    main()