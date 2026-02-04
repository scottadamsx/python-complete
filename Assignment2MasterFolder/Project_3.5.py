#! usr/bin/env python3

# print title
print("Table of Powers\n")

while True:
    startNumber = int(input("Start number: "))
    endNumber = int(input("Stop number: "))
    if startNumber < endNumber:
        break
    else:
        print("ERROR: your start number must be less than your end number, please try again...")


print("Number\t\tSquared\t\tCubed")
print("======\t\t=======\t\t=====")

for i in range(startNumber,endNumber + 1):
    print(f"{i}\t\t{i ** 2}\t\t{i ** 3}")
