# template for label widget: 
#
# labelName = tk.Label(window*, text="")
# labelName.pack()

# template for Entry widget: 
#
# players = tk.Entry()
# players.pack()

players = 0
startingValue = 0

def name_players(playersInput,startingValueInput):
    global players
    global startingValue
    players = playersInput.get()
    startingValue = startingValueInput.get()

    playerNames = tk.Tk()
    playerNames.geometry("500x500")
    playerNames.title("name players:")

    playerVarNames = ["player1","player2","player3","player4","player5","player6",]
    for i in range(players):
        playerVarNames[i] = tk.Label(playerNames, text=f"Enter Name for player {i}")
        playerVarNames[i].pack()
        
        playerVarNames[i] = tk.Entry(playerNames)
        playerVarNames[i].pack()
        
    playerNames.mainloop()



# labelName.pack()


# monopoly GUI 
import tkinter as tk
from properties_board import *

# create an opening window with a start game option
StartingScreen = tk.Tk()
StartingScreen.geometry("400x300")
StartingScreen.title("Monopoly Banker GUI")

# create a label and button
StartingScreenLabel = tk.Label(StartingScreen, text="Welcome to Monopoly BAnker GUI, Would you like to start a game?")
StartingScreenLabel.pack()

def start_button():

    initialize_board = tk.Tk()
    initialize_board.geometry("400x300")
    initialize_board.title("Starting Values")

    playersLabel = tk.Label(initialize_board, text="Pick The Number of Players:")
    playersLabel.pack()

    playersInput= tk.Entry(initialize_board)
    playersInput.pack()

    startingValueLabel = tk.Label(initialize_board, text="Pick The starting value:")
    startingValueLabel.pack()

    startingValueInput = tk.Entry(initialize_board)
    startingValueInput.pack()

    submitButton = tk.Button(initialize_board, text="continue", command=lambda: name_players(playersInput,startingValueInput))
    submitButton.pack()

    initialize_board.mainloop()




startButton = tk.Button(StartingScreen, text="Start Game!", command=start_button)
startButton.pack()

StartingScreen.mainloop()
