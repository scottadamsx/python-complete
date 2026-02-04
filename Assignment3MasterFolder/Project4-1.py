#! usr/bin/env python3
# Even or Odd Checker

# function to check if an integer is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    

def main():

    print("Even or Odd Checker\n")

    number = int(input("Enter an integer:  "))
    print(f"This is an {even_or_odd(number)} number.")

if __name__ == "__main__":
    main()