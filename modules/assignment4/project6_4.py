#!usr/bin/env python3
# NTS - done and completed

def get_sales():
    salesList = []
    for i in range(4):
        sale = round(float(input(f"Enter sales for Q{i+1}: ")), 2)
        salesList.append(sale)
            
    return salesList


def get_average(salesList):
    average = round(sum(salesList) / 4, 2)
    return average


def grab_highest_lowest(salesList):
    salesList.sort()
    lowest = salesList[0]
    highest = salesList[-1]
    return highest, lowest


def main():

    salesList = get_sales()
    average = get_average(salesList)
    highest, lowest = grab_highest_lowest(salesList)
    print(lowest, highest)

    print(f"\nTotal:\t\t\t{sum(salesList)}")
    print(f"Average Quarter:\t{average}")
    print(f"Lowest Quarter:\t\t{lowest}")
    print(f"Highest Quarter:\t{highest}")


if __name__ == "__main__":
    main()