#! usr/bin/env python3
line = "+---+---+---+"
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]



def display_board(board):
    print()
    for row in board:
        print(line)
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print(line)



def switch_turn(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player



def take_turn(player, board):
    print(f"{player}'s turn!!")
    while True:
        # grab the row variable and check that it is in range of the board
        while True:
            row = int(input("Pick a row (1, 2, 3): ")) - 1
            if row in range(len(board)):
                break
            else: 
                print("This is not a correct option, please try again")
        # once the row is valid, grab the column variable and check that it is in range of the board
        while True:        
            column = int(input("Pick a column (1, 2, 3): ")) - 1
            if column in range(len(board[row])):
                break
            else: 
                print("This is not a correct option, please try again")


        if board[row][column] == " ":
            board[row][column] = player
            break
        else: 
            print("this spot is taken, pick a new one")



def win_check(board):
    win = False
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            win = True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            win = True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        win = True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        win = True

    return win
    
def is_tie(board):
    blankSpaceCounter = 0
    for row in board:
        for column in row:
            if column == " ":
                blankSpaceCounter += 1
    if blankSpaceCounter == 0:
        return True
    else:
        return False


def main():

    line = "+---+---+---+"
    board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    player = "X"
    win = win_check(board)

    while True:

        display_board(board)
        take_turn(player, board)
        win = win_check(board)

        if win == True:
            display_board(board)
            print(f"{player} has won the game!")
            break
        elif is_tie(board):
            print("it is a tie!")
            break
        else:
            player = switch_turn(player)

if __name__ == "__main__":
    main()