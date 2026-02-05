#! usr/bin/env python3
# Champion Counter

def title():
    print("Champion Counter\n")

def read_data():
    FILENAME = "world_cup_champions.txt"
    with open(FILENAME, newline="") as file:
        countries = {}
        next(file)
        for line in file:
            things = line.split(",")
            if things[1] in countries:
                countries[things[1]]["years"].append(things[0])
                countries[things[1]]["Coach"].append(things[2])
                countries[things[1]]["Captain"].append(things[3])
            else:
                countries[things[1]] = {"years":[things[0]], "Coach":[things[2]], "Captain":[things[3]]}

    return countries       
    
def display_data(countries):
    print("Countries       Wins    Years")
    print("=========       ====    =====")
    
    countriesAlphebatically = sorted(countries.keys())
    for country in countriesAlphebatically:

        years = countries[country]["years"]
        years = ", ".join(years)

        if len(country) < 9:
            print(f"{country}\t\t{len(countries[country]["years"])}\t{years}")
        else:
            print(f"{country}\t{len(countries[country]["years"])}\t{years}")


def main():

    title()
    countries = read_data()
    display_data(countries)

if __name__ == "__main__":
    main() 