#! usr\bin\env python3
# project 2.5 - Time Travel Calculator

def main():
      # print title
      print("Time Travel Calculator\n")

      # prompt user for miles and mph
      miles = int(input("Enter miles: "))
      milesPerHour = int(input("Enter miles per hour: "))

      # perform calculations
      estimatedTravel = round(miles / milesPerHour * 60) #60 to turn it to minutes

      # print output
      print(f"\nEstimated travel time\nHours: {estimatedTravel // 60}\n"
            + f"Minutes: {estimatedTravel % 60}")

      #NTS - code finished and debugged
      
if __name__ == "__main__":
    main()
