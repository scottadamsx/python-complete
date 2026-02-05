#! usr/bin/env python3

# Project 3.1 - Letter Grade Converter

def main(): 

    # print title
    print("Letter Grade Converter\n")


    while True: 
        grade = int(input("\nEnter numerical grade: "))

        # check what letter grade corresponds to the grade
        if 100 >= grade >= 88:
            letterGrade = "A"
        elif 87 >= grade >= 80:
            letterGrade = "B"
        elif 79 >= grade >= 67:
            letterGrade = "C"
        elif 66 >= grade >= 60:
            letterGrade = "D"
        else:
            letterGrade = "F"

        # display output
        print(f"Letter grade: {letterGrade}")

        # ask user to continue
        contin = input("\nContinue? (y/n): ").lower()
        if contin != "y":
            break

    # closing message
    print("\nBye!")
    
if __name__ == "__main__":
    main()
