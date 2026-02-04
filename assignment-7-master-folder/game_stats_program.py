#! usr/bin/env python3
# Game Stats Program

def title():
    print("Game Stats Program\n")


players = {"elizabeth": {"Wins":41, "Losses":3, "Ties":22},
            "joel": {"Wins":32, "Losses":14, "Ties":17},
            "mike": {"Wins":8, "Losses":19, "Ties":11}}



def list_all_players(players):
    playerList = sorted(players.keys())
    print("ALL PLAYERS:")
    for player in playerList:
        print(player.capitalize())



def get_stats(players): 
    player = input("\nEnter a player name: ")
    if player in players:
        print("Wins:   ", players[player]["Wins"])
        print("Losses: ", players[player]["Losses"])
        print("Ties:   ", players[player]["Ties"])
    else:
        print(f"There is no player named {player}")



#==================================================================

def main():

    title()
    list_all_players(players)
    
    while True:

        get_stats(players)

        go_again = input("\nContinue? (y/n): ").lower()
        if go_again != "y":
            print("\nBye!\n")
            break

if __name__ == "__main__":
    main()