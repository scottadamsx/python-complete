#! usr/bin/env python3

from classes import property, player
    
def initialize_properties():
    mediterranean_avenue = property("Mediterranean Avenue", 60, "Purple", 50, 0, 2, 10, 30, 90, 160, 250, 30)
    baltic_avenue = property("Baltic Avenue", 60, "Purple", 50, 0, 4, 20, 60, 180, 320, 450, 30)
    oriental_avenue = property("Oriental Avenue", 100, "Light Blue", 50, 0, 6, 30, 90, 270, 400, 550, 50)
    vermont_avenue = property("Vermont Avenue", 100, "Light Blue", 50, 0, 6, 30, 90, 270, 400, 550, 50)
    connecticut_avenue = property("Connecticut Avenue", 120, "Light Blue", 50, 0, 8, 40, 100, 300, 450, 600, 60)
    st_charles_place = property("St. Charles Place", 140, "Violet", 100, 0, 10, 50, 150, 450, 625, 750, 70)
    states_avenue = property("States Avenue", 140, "Violet", 100, 0, 10, 50, 150, 450, 625, 750, 70)
    virginia_avenue = property("Virginia Avenue", 160, "Violet", 100, 0, 12, 60, 180, 500, 700, 900, 80)
    st_james_place = property("St. James Place", 180, "Orange", 100, 0, 14, 70, 200, 550, 750, 950, 90)
    tennessee_avenue = property("Tennessee Avenue", 180, "Orange", 100, 0, 14, 70, 200, 550, 750, 950, 90)
    new_york_avenue = property("New York Avenue", 200, "Orange", 100, 0, 16, 80, 220, 600, 800, 1000, 100)
    kentucky_avenue = property("Kentucky Avenue", 220, "Red", 150, 0, 18, 90, 250, 700, 875, 1050, 110)
    indiana_avenue = property("Indiana Avenue", 220, "Red", 150, 0, 18, 90, 250, 700, 875, 1050, 110)
    illinois_avenue = property("Illinois Avenue", 240, "Red", 150, 0, 20, 100, 300, 750, 925, 1100, 120)
    atlantic_avenue = property("Atlantic Avenue", 260, "Yellow", 150, 0, 22, 110, 330, 800, 975, 1150, 130)
    ventnor_avenue = property("Ventnor Avenue", 260, "Yellow", 150, 0, 22, 110, 330, 800, 975, 1150, 130)
    marvin_gardens = property("Marvin Gardens", 280, "Yellow", 150, 0, 24, 120, 360, 850, 1025, 1200, 140)
    pacific_avenue = property("Pacific Avenue", 300, "Green", 200, 0, 26, 130, 390, 900, 1100, 1275, 150)
    north_carolina_avenue = property("North Carolina Avenue", 300, "Green", 200, 0, 26, 130, 390, 900, 1100, 1275, 150)
    pennsylvania_avenue = property("Pennsylvania Avenue", 320, "Green", 200, 0, 28, 150, 450, 1000, 1200, 1400, 160)
    park_place = property("Park Place", 350, "Blue", 200, 0, 35, 175, 500, 1100, 1300, 1500, 175)
    boardwalk = property("Boardwalk", 400, "Blue", 200, 0, 50, 200, 600, 1400, 1700, 2000, 200)

    return mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk

def initialize_board(mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk):
    boardSpaces = [None] * 40  # There are 40 spaces on the Monopoly board, so we initialize with None

    # Assigning each property dictionary to the respective board space index
    boardSpaces[0] = "go"
    boardSpaces[1] = mediterranean_avenue
    boardSpaces[2] = "community chest"
    boardSpaces[3] = baltic_avenue
    boardSpaces[4] = "income tax"
    boardSpaces[5] = "railway 1"
    boardSpaces[6] = oriental_avenue
    boardSpaces[7] = "chance"
    boardSpaces[8] = vermont_avenue
    boardSpaces[9] = connecticut_avenue
    boardSpaces[10] = "just visiting"
    boardSpaces[11] = st_charles_place
    boardSpaces[12] = "electric company"
    boardSpaces[13] = states_avenue
    boardSpaces[14] = virginia_avenue
    boardSpaces[15] = "railway 2"
    boardSpaces[16] = st_james_place
    boardSpaces[17] = "chance"
    boardSpaces[18] = tennessee_avenue
    boardSpaces[19] = new_york_avenue
    boardSpaces[20] = "free parking"
    boardSpaces[21] = kentucky_avenue
    boardSpaces[22] = "chance"
    boardSpaces[23] = indiana_avenue
    boardSpaces[24] = illinois_avenue
    boardSpaces[25] = "railway 3"
    boardSpaces[26] = atlantic_avenue
    boardSpaces[27] = ventnor_avenue
    boardSpaces[28] = "water works"
    boardSpaces[29] = marvin_gardens
    boardSpaces[30] = "go to jail"
    boardSpaces[31] = pacific_avenue
    boardSpaces[32] = north_carolina_avenue
    boardSpaces[33] = "community chest"
    boardSpaces[34] = pennsylvania_avenue
    boardSpaces[35] = "railway 4"
    boardSpaces[36] = "chance"
    boardSpaces[37] = park_place
    boardSpaces[38] = "luxury tax"
    boardSpaces[39] = boardwalk

    return boardSpaces

def initialize_players():
    wallet = int(input("Enter the starting cash value for all players: "))
    while True:
        numPlayers = int(input("How many players would you like to have for your game:"))
        if numPlayers <=6 and numPlayers >= 1:
            break
        else:
            print("Choose 2 to 6 player: ")
    playerList = []
    if numPlayers  > 1:
        name = input("Enter the name for Player 1: ")
        player1 = player(name, wallet, [], [])
        playerList.append(player1)
    if numPlayers  >= 2:
        name = input("Enter the name for Player 2: ")
        player2 = player(name, wallet, [], [])
        playerList.append(player2)
    if numPlayers  >= 3:
        name = input("Enter the name for Player 3: ")
        player3 = player(name, wallet, [], [])
        playerList.append(player3)
    if numPlayers  >= 4:
        name = input("Enter the name for Player 4: ")
        player4 = player(name, wallet, [], [])
        playerList.append(player4)
    if numPlayers  >= 5:
        name = input("Enter the name for Player 5: ")
        player5 = player(name, wallet, [], [])
        playerList.append(player5)
    if numPlayers  == 6:
        name = input("Enter the name for Player 6: ")
        player6 = player(name, wallet, [], [])
        playerList.append(player6)
    return playerList

def initilize_monopolies(mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue, st_charles_place, states_avenue, virginia_avenue, st_james_place, tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue, pennsylvania_avenue, park_place, boardwalk):
    # Define the monopolies dictionary here
    monopolies = {
        "Brown": {
            "Mediterranean Avenue": mediterranean_avenue,
            "Baltic Avenue": baltic_avenue
        },
        "Light Blue": {
            "Oriental Avenue": oriental_avenue,
            "Vermont Avenue": vermont_avenue,
            "Connecticut Avenue": connecticut_avenue
        },
        "Pink": {
            "St. Charles Place": st_charles_place,
            "States Avenue": states_avenue,
            "Virginia Avenue": virginia_avenue
        },
        "Orange": {
            "St. James Place": st_james_place,
            "Tennessee Avenue": tennessee_avenue,
            "New York Avenue": new_york_avenue
        },
        "Red": {
            "Kentucky Avenue": kentucky_avenue,
            "Indiana Avenue": indiana_avenue,
            "Illinois Avenue": illinois_avenue
        },
        "Yellow": {
            "Atlantic Avenue": atlantic_avenue,
            "Ventnor Avenue": ventnor_avenue,
            "Marvin Gardens": marvin_gardens
        },
        "Green": {
            "Pacific Avenue": pacific_avenue,
            "North Carolina Avenue": north_carolina_avenue,
            "Pennsylvania Avenue": pennsylvania_avenue
        },
        "Blue": {
            "Park Place": park_place,
            "Boardwalk": boardwalk
        }
    }

    return monopolies
