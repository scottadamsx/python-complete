#! usr/bin/env python3

def main():

    print("Pay Check Calculator\n")

    # prompt user for hours worked and hourly pay rate
    hoursWorked = float(input("Hours worked:\t"))
    hourlyRate = float(input("Hourly Pay Rate:"))
    taxRate = 0.18

    # calculate the gross pay, tax amount and take home pay
    grossPay = round(hoursWorked * hourlyRate, 2)
    taxAmount = round(grossPay * taxRate, 2)
    takeHomePay = round(grossPay - taxAmount, 2)

    # display all 4 results
    print(f"\nGross Pay:\t{grossPay}")
    print(f"Tax Rate:\t{round(taxRate*100)}%")
    print(f"Tax Amount:\t{taxAmount}")
    print(f"Gross Pay:\t{takeHomePay}")

    #NTS - code finished and debugged



if __name__ == "__main__":
    main()