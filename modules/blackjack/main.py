#! usr/bin/env python3

# import all the modules
import db
import random
from deck import *
from game_logic import *


# a simple function that displays the opening message when the program loads up
def display_title():
    print("BLACKJACK! \nBlackjack payout is 3:2\n")

# creates deck and shuffles it for the round, deals two cards to the dealer and player, and asks for an initial bet
def start_round(playerMoney):

    deck = initialize_deck()
    random.shuffle(deck)

    print(f"money: {playerMoney}")
    bet = place_bet(playerMoney)

    playerHand = []
    deal_card(playerHand, deck, 2)
    dealerHand = []
    deal_card(dealerHand, deck, 2)

    # include the display of the first data
    print("\nDEALERS SHOW CARD:")
    print(f"{dealerHand[0][1]} of {dealerHand[0][0]}\n")

    print("YOUR CARDS")
    for card in playerHand:
        print(f"{card[1]} of {card[0]}\n")

    return playerHand, dealerHand, bet, deck



def display_result():
    pass



# ==========================================================================================
def main(): 

    display_title()

    playerMoney = db.read_money()
    while playerMoney >= 5:
            
            playerHand, dealerHand, bet, deck = start_round(playerMoney)
            check_for_ace(playerHand)
 
            playerChoice = hit_or_stand(deck, playerHand)

            if playerChoice == "hit":
                deal_card(playerHand, deck)
                check_for_ace(playerHand)

            
            dealer_continue(dealerHand, deck)
            playerTotal = calculate_total(playerHand)
            dealerTotal = calculate_total(dealerHand)

            win_check(playerTotal, dealerTotal, bet, playerMoney, playerHand, dealerHand)
            repeat = input("Go again?")
            if repeat.lower() != "y":
                break

    #buy_chips(playerMoney)
    

if __name__ == "__main__":
    main()