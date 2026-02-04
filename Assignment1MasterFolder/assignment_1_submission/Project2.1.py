#! usr/bin/env python3
# Project2.1 - student registration

# print title
print("Registration Form\n")

# prompt user for first name and last name
firstName = input("First name:\t")
lastName = input("Last name:\t")
birthYear = input("Birth year:\t")

# create temp password variable 
tempPass = firstName + "*" + birthYear
fullName = firstName + " " + lastName

# print output
print(f"\nWelcome {firstName} {lastName}!")
print("Your registration is complete.")
print(f"Your temporary password is: {tempPass}")

# NTS - code completed and debugged