#! usr/bin/env python3
import csv

sinfulFile = "prospects.csv"
holyFile = "prospects_clean.csv"

# code to read an entire csv file and turn it into a single list
def read_prospects(sinfulFile):
    prospects = []                                                # creates an empty list to place values
    with open(sinfulFile, "r", newline="") as file:               # opens file 
        reader = csv.reader(file)                                 # creates reader
        for row in reader:                                        # for every row in the file, it will extend the list
            prospects.extend(row)                                  
    
    return prospects                                              # returns the values
# ====================================================================================================================


def clean_prospects(prospects):
    cleanedProspects = []
    for prospect in prospects:
            if "@" in prospect:
                prospect = prospect.lower()
                cleanedProspects.append(prospect)
            else:
                prospect = prospect.title().strip()
                cleanedProspects.append(prospect)
    return cleanedProspects


def write_prospects(prospects, holyFile):
    with open(holyFile, "w", newline="") as file:
        writer = csv.writer(file)
        
        row = []
        for i in prospects:
            row.append(i)
            if len(row) == 3:
                writer.writerow(row)
                row = []
    print("\nsuccessfully updated file to prospects_clean.csv\n")
        
 
def main():

    prospects = read_prospects(sinfulFile)
    cleanedProspects = clean_prospects(prospects)
    write_prospects(cleanedProspects, holyFile)

if __name__ == "__main__":
    main()