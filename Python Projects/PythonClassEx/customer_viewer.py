#! usr/bin/env python3

import csv
from employee_class import Customer

FILENAME = "customers.csv"


def title():
    print("Customer Lookup")


def read_customers(filename):
    customers = {}
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if your CSV has headers
        for row in reader:
            if row:  # Check if the row is not empty
                customerID, firstName, lastName, companyName, address, city, state, zipcode = row
                customer = Customer(customerID, firstName, lastName, companyName, address, city, state, zipcode)
                customers[customerID] = customer
    return customers


def main():

    employees_dict = read_customers(FILENAME)

if __name__ == '__main__':
    main()