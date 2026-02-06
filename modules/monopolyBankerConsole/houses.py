#! usr/bin/env python3
"""

from classes import property, player
from initialize_game import initialize_board, initialize_properties, initialize_players, initilize_monopolies

oriental_avenue = property("Oriental Avenue", 100, "Light Blue", 50, 0, 6, 30, 90, 270, 400, 550, 50)
vermont_avenue = property("Vermont Avenue", 100, "Light Blue", 50, 0, 6, 30, 90, 270, 400, 550, 50)
connecticut_avenue = property("Connecticut Avenue", 120, "Light Blue", 50, 0, 8, 40, 100, 300, 450, 600, 60)

currentPlayer = player("Scotty", 2400, [oriental_avenue, vermont_avenue, connecticut_avenue], ["Light Blue"])

"""

# FAKE PLAYER WITH A LIGHT BLUE MONOPOLY
#==================================================================================================================
def buy_house_menu(currentPlayer, monopolies):
    if len(currentPlayer.monopolies) == 0:
        print("You do not own any monopolies to add houses onto! Try again later...")
        return 

    # Display available monopolies
    print("Available monopolies:")
    for idx, monopoly in enumerate(currentPlayer.monopolies, 1):
        print(f"{idx}. {monopoly}")
    
    # Select a monopoly
    monopoly_idx = int(input(f"What would you like to buy houses on? 1-{len(currentPlayer.monopolies)}: ")) - 1
    if monopoly_idx < 0 or monopoly_idx >= len(currentPlayer.monopolies):
        print("Invalid choice!")
        return

    # Get chosen monopoly
    chosenMonopolyName = currentPlayer.monopolies[monopoly_idx]
    chosenMonopoly = monopolies[chosenMonopolyName]

    # Display properties and houses
    print("\nProperties in this monopoly:")
    for name, prop in chosenMonopoly.items():
        print(f"{name}: {prop.houses} houses")
    
    # Show player balance and house cost
    house_price = next(iter(chosenMonopoly.values())).housePrice  # Assuming all properties in the group have the same house price
    print(f"\nYour current balance: ${currentPlayer.wallet}")
    print(f"Cost per house: ${house_price}\n")

    # Ask how many houses to buy
    houses_to_buy = int(input("How many houses would you like to buy?: "))
    total_owned_houses = sum(prop.houses for prop in chosenMonopoly.values())
    house_cost = houses_to_buy * house_price
    print(f"Total cost for {houses_to_buy} houses: ${house_cost}")

    # Validate house purchase
    if houses_to_buy + total_owned_houses > 15:
        print(f"You currently own {total_owned_houses} houses. You can only buy up to {15 - total_owned_houses} more houses.")
        return
    elif house_cost > currentPlayer.wallet:
        print("You do not have enough money to make this purchase!")
        return

    # Deduct cost and place houses
    currentPlayer.wallet -= house_cost
    houses_remaining = houses_to_buy

    while houses_remaining > 0:
        print(f"\nHouses to place: {houses_remaining}")
        print("Properties:")
        for idx, (name, prop) in enumerate(chosenMonopoly.items(), 1):
            print(f"{idx}. {name} - Houses: {prop.houses}")
        
        # Select a property to place a house
        property_idx = int(input(f"Which property would you like to place a house on? (1-{len(chosenMonopoly)}): ")) - 1
        if property_idx < 0 or property_idx >= len(chosenMonopoly):
            print("Invalid property choice! Try again.")
            continue

        property_list = list(chosenMonopoly.values())
        chosen_property = property_list[property_idx]

        # Validate house placement
        if all(abs(chosen_property.houses + 1 - other.houses) <= 1 for other in property_list):
            chosen_property.houses += 1
            houses_remaining -= 1
        else:
            print("Cannot place a house here as it violates the placement rule!")

    print("\nHouse placement complete!")
    print(f"Your remaining balance: ${currentPlayer.wallet}")


#====================================================================================================================
def sell_house_menu(currentPlayer, monopolies):
    if len(currentPlayer.monopolies) == 0:
        print("You do not own any monopolies with houses to sell!")
        return 

    # Display available monopolies
    print("Available monopolies to sell houses:")
    for idx, monopoly in enumerate(currentPlayer.monopolies, 1):
        print(f"{idx}. {monopoly}")
    
    # Select a monopoly
    monopoly_idx = int(input(f"Which monopoly would you like to sell houses from? 1-{len(currentPlayer.monopolies)}: ")) - 1
    if monopoly_idx < 0 or monopoly_idx >= len(currentPlayer.monopolies):
        print("Invalid choice!")
        return

    # Get chosen monopoly
    chosenMonopolyName = currentPlayer.monopolies[monopoly_idx]
    chosenMonopoly = monopolies[chosenMonopolyName]

    # Display properties and houses
    print("\nProperties in this monopoly:")
    for name, prop in chosenMonopoly.items():
        print(f"{name}: {prop.houses} houses")
    
    # Ask how many houses to sell
    houses_to_sell = int(input("How many houses would you like to sell?: "))
    total_owned_houses = sum(prop.houses for prop in chosenMonopoly.values())
    house_sell_price = next(iter(chosenMonopoly.values())).housePrice // 2  # Sell at half the original price
    total_sell_value = houses_to_sell * house_sell_price
    print(f"Total sell value for {houses_to_sell} houses: ${total_sell_value}")

    # Validate house selling
    if houses_to_sell > total_owned_houses:
        print(f"You only have {total_owned_houses} houses in this monopoly. Cannot sell more than that.")
        return

    # Sell houses
    houses_remaining = houses_to_sell
    while houses_remaining > 0:
        print(f"\nHouses to sell: {houses_remaining}")
        print("Properties:")
        for idx, (name, prop) in enumerate(chosenMonopoly.items(), 1):
            print(f"{idx}. {name} - Houses: {prop.houses}")
        
        # Select a property to remove a house
        property_idx = int(input(f"Which property would you like to sell a house from? (1-{len(chosenMonopoly)}): ")) - 1
        if property_idx < 0 or property_idx >= len(chosenMonopoly):
            print("Invalid property choice! Try again.")
            continue

        property_list = list(chosenMonopoly.values())
        chosen_property = property_list[property_idx]

        # Temporarily decrement the house count
        chosen_property.houses -= 1
        min_houses = min(prop.houses for prop in property_list)
        max_houses = max(prop.houses for prop in property_list)

        # Validate the new distribution
        if max_houses - min_houses > 1:
            # Revert the change if it violates the rule
            chosen_property.houses += 1
            print("Cannot sell a house from this property as it violates the placement rule!")
        else:
            # Confirm the sale
            houses_remaining -= 1
            currentPlayer.wallet += house_sell_price
            print(f"Sold 1 house from {list(chosenMonopoly.keys())[property_idx]} for ${house_sell_price}.")

    print("\nHouse selling complete!")
    print(f"You received ${total_sell_value}. Your new balance: ${currentPlayer.wallet}")


#==============================================================================================================


def main():
    '''
    # THIS IS TEST CODE TO ENSURE THE VALUES WORK 
    
    # initializes all the properties using the property class using the initialize property function
    mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk = initialize_properties()
    # assigns them all to a boardSpace
    boardSpaces = initialize_board(mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk)
    monopolies = initilize_monopolies(mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk)

    buy_house_menu(currentPlayer, monopolies)
    sell_house_menu(currentPlayer, monopolies)
    '''
    

    
if __name__ == "__main__":
    main()