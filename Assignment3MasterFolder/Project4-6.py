#! usr/bin/env python3

factors = []

def get_factors(number):
   
  for i in range(1,number + 1):
      if number % i == 0:
        factors.append(i)
      else:
        pass

def is_prime(number):
  if factors[0] == 1 and factors[1] == number:
      print(f"{number} is a prime number")
  else:
    print(f"{number} is NOT a prime number.\nIt has {len(factors)} factors.")

def main():
   
  number = int(input("Please enter an ingeter from 1 to 5000: "))
  get_factors(number)
  is_prime(number)
  print(factors)

if __name__ == "__main__":
     main()