#! usr/bin/env python3
import csv


class Customer:
    def __init__(self, customerID, firstName, lastName, company, address, city, state, zipcode):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

        def __str__(self):
            return self.firstName + self.lastName