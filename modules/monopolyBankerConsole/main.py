#! usr/bin/env python3

import random
from .save_game import save_game
from .classes import property, player
# import the make trade function
from . import trade
# import the buy and sell houses functions
from .houses import buy_house_menu, sell_house_menu
# imports the initilize game module which is responsible for creating the board with blank properties
from .initialize_game import initialize_board, initialize_properties, initialize_players, initilize_monopolies
from .special_spots import handle_special_spot


def choose_random_property(properties):
    x = random.randint(0,21)
    property = properties[x]
    name = property.name
    price = property.price
    rent3houses = property.rent3
    print(f"you can buy {name} for {price} and with 3 houses, rent would be {rent3houses}")

def take_turn(currentPlayer, boardSpaces, playerList):
    currentPlace = currentPlayer.boardSpace
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll = roll1 + roll2
    print(f"{currentPlayer.name} rolled {roll1} and {roll2} (Total: {roll})")
    
    doubles = False  # Default no doubles
    
    # If the player rolls doubles, they get an extra turn unless it's the third time in a row
    if roll1 == roll2:
        print("You rolled doubles!")
        doubles = True
        currentPlayer.doubles_count += 1  # Increment doubles count
        
        if currentPlayer.doubles_count > 2:                                                                     # If they roll doubles three times, they go to jail
            print(f"Oops! You rolled doubles three times in a row! {currentPlayer.name} is going to Jail!")
            currentPlayer.boardSpace = 10                                                                       # Jail position
            currentPlayer.doubles_count = 0  # Reset doubles count
            return  # End turn immediately if the player goes to Jail

    # Calculate new position
    landedSpace = (currentPlace + roll) % len(boardSpaces)
    currentPlayer.boardSpace = landedSpace  # Update the player's position
    newSpace = boardSpaces[landedSpace]

    # Check if the player passed Go (i.e., landed on a space with index 0)
    if currentPlayer.boardSpace < currentPlace:
        currentPlayer.wallet += 200  # Add $200 to wallet
        print(f"{currentPlayer.name} passed Go! You collect $200.")

    # If the space is a Property, handle property logic
    if isinstance(newSpace, property):  
        print(f"{currentPlayer.name} landed on {newSpace.name}!")

        # OPTION 1: if no one owns the property, prompt the user to purchase!
        if newSpace.owner == "none":
            while True:
                buy = input(f"Would you like to purchase {newSpace.name} for {newSpace.price}? (y/n): ").lower()
                
                if buy == "y":
                    if currentPlayer.wallet < newSpace.price:
                        print("You cannot afford that! Get your bread up!")
                        break
                    else:
                        newSpace.owner = currentPlayer.name
                        currentPlayer.wallet -= newSpace.price
                        currentPlayer.properties.append(newSpace)
                        print(f"You now own {newSpace.name}.")
                        check_for_monopoly(currentPlayer)
                        break
                elif buy == "n":
                    print("you did not purchase this property!")
                    break
                else:
                    print("invalid option")

        # OPTION 2: if someone does own the property, check if we own it, and it we do... dont pay rent dumbassssss
        elif newSpace.owner == currentPlayer.name: 
            print("you won this venue, enjoy your stay boss!")

        # OPTION 3: property is owned by someone else. pay rent biatchhhhh
        else:

            rent = 10 if newSpace.houses == 0 else getattr(newSpace, f"rent{newSpace.houses}")
            print(f"This is owned by {newSpace.owner}. Rent is {rent}.")
            for player in playerList:
                if player.name == newSpace.owner:
                    landlord = player
                    currentPlayer.wallet -= rent
                    landlord.wallet += rent
            print(f"{currentPlayer.name} paid {landlord.name} {rent} in rent!")
    
    # If the space is NOT a Property, handle special space logic
    else:  
        handle_special_spot(newSpace, currentPlayer, playerList)
    
    # If the player rolled doubles, they get to go again
    if doubles:
        print(f"{currentPlayer.name} gets another turn!")
        take_turn(currentPlayer, boardSpaces, playerList)  # Recursively call take_turn for another roll

                
def switchTurn(currentPlayer, playerList):
    
    index = playerList.index(currentPlayer) + 1
    #print(f"index {index} len {len(playerList)}")     *used for debugging
    if index >= len(playerList):
        currentPlayer = playerList[0]
    else:
        currentPlayer = playerList[index]

    print(f"\nit is now {currentPlayer.name}'s turn!")
    return currentPlayer

# a function to call the menu once a player is finished rolling, this calls several actions within the menu!
def afterTurnMenu(currentPlayer, playerList, monopolies, properties):

    print("\nMENU OPTIONS")
    print("1. View Properties")
    print("2. Buy Houses")
    print("3. Sell Houses")
    print("4. Buy or Morgage Properties")
    print("5. Make Trade")
    print("6. Save game (Warning this will end the current session)")

    while True:
        print(f"\nplayers turn: {currentPlayer.name}")
        print(f"current balance: {currentPlayer.wallet}")
        print(f"players monopolies: {currentPlayer.monopolies}")

        try:
            action = (input(f"{currentPlayer.name}, what would you like to do? (ENTER to end turn): "))
            if action == "":
                break
            action = int(action)
            if action in range(1,7):
                break
        except ValueError:
            print("invalid option, choose 1-6 please...")
        except Exception as e:
            print(type(e), e)
            

    if action == 1:
        view_properties(currentPlayer)
    elif action == 2:
        print("Buy House Menu!")
        buy_house_menu(currentPlayer, monopolies)
    elif action == 3:
        print("Sell House Menu!")
        sell_house_menu(currentPlayer, monopolies)
    elif action == 4:
        print("buy/morgage properties!")
        
    elif action == 5:
        print("Make trade menu!")
        trade.make_trade(currentPlayer, playerList)

    elif action == 6:
        print("saving game... ")
        save_game.save_game("saveFile.csv", playerList, properties)

    return action
    


def view_properties(currentPlayer):
    properties = currentPlayer.properties
    print()
    for property in properties:
        print(property.name)
        print("====================")
        print("Price...........", property.price)
        print("Color...........", property.color)
        print("House Price.....", property.housePrice)
        print("Houses..........", property.houses)
        print("Rent............", property.rent)
        print("with 1 House....", property.rent1)
        print("with 2 Houses...", property.rent2)
        print("with 3 Houses...", property.rent3)
        print("with 4 Houses...", property.rent4)
        print("with a Hotel....", property.rent5)
        print("Morgage Value...", property.morgageValue)
        print("owned by........", property.owner)
        print()

def check_for_monopoly(currentPlayer):
    # List of properties owned by the current player
    properties = currentPlayer.properties
    propertyNames = [property.name for property in properties]

    # Define color groups for monopolies
    monopolies = {
        "Brown": {"Mediterranean Avenue", "Baltic Avenue"},
        "Light Blue": {"Oriental Avenue", "Vermont Avenue", "Connecticut Avenue"},
        "Pink": {"St. Charles Place", "States Avenue", "Virginia Avenue"},
        "Orange": {"St. James Place", "Tennessee Avenue", "New York Avenue"},
        "Red": {"Kentucky Avenue", "Indiana Avenue", "Illinois Avenue"},
        "Yellow": {"Atlantic Avenue", "Ventnor Avenue", "Marvin Gardens"},
        "Green": {"Pacific Avenue", "North Carolina Avenue", "Pennsylvania Avenue"},
        "Blue": {"Park Place", "Boardwalk"}
    }

    # Iterate through each color group
    for color, group in monopolies.items():
        owned_properties = set(propertyNames).intersection(group)
        
        # Check if the player owns all properties in the color group
        if owned_properties == group:
            # If the player already has this monopoly, skip adding it
            if color not in currentPlayer.monopolies:
                currentPlayer.monopolies.append(color)
                print(f"Congrats, you have a {color} monopoly!")
    
    # The function does not need to print anything if no new monopolies are found.



    
def main():

    newOrLoad = input("Would you like to load up a previous game? NEW or LOAD (n/l): ").lower()

    # load game from file
    if newOrLoad == "l":
        playerList, properties = save_game.load_game("saveFile.csv")
        mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk = properties
        boardSpaces = initialize_board(mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk)
        currentPlayer = playerList[0]

    # Start new Game
    else:
        # initializes all the properties using the property class using the initialize property function
        mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk = initialize_properties()
        # assigns them all to a boardSpace
        properties =  (mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk)
        boardSpaces = initialize_board(mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk)
        # initializes players using the initialize players function
        playerList = initialize_players()
        monopolies = initilize_monopolies(mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk)
        # sets player1 to tge first player, can be changed later in the code
        currentPlayer = playerList[0]

    

    # MAIN TURN LOGIC
    while True:

        startTurn = input(f"{currentPlayer.name}, press ENTER to roll")

        take_turn(currentPlayer, boardSpaces, playerList)

        while True:
            turnAction = afterTurnMenu(currentPlayer, playerList, monopolies, properties)
            

            if turnAction == "":
                currentPlayer = switchTurn(currentPlayer, playerList)
                break


if __name__ == '__main__':
    main()