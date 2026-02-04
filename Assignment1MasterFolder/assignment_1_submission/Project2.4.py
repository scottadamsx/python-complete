#! usr/bin/env python3
# Project2.4 - price comparison

# print title
print("Price Comparison")

# prompt user for price for 64 and 32 oz
price64 = float(input("Price of 64 oz size: "))
price32 = float(input("Price of 32 oz size: "))

# calculate pricePeroz
pricePer64 = round(price64 / 64, 2) 
pricePer32 = round(price32 / 32, 2) 

# print output 
print(f"\nPrice per oz (64 oz): {pricePer64}")
print(f"Price per oz (32 oz): {pricePer32}")
