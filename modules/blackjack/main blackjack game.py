import db
import random
from deck import *
from game_logic import *

def display_title():
    print("BLACKJACK! \nBlackjack payout is 3:2\n")

# creates deck and shuffles it for the round, deals two cards to the dealer and player, and asks for an initial bet
def start_round(money):
    deck = initialize_deck()
    random.shuffle(deck)

    print(f"money: {money}")
    bet = place_bet(money)
    playerHand = []
    deal_card(playerHand, deck, 2)
    dealerHand = []
    deal_card(dealerHand, deck, 2)
    
    # includes the initial data 
    print()
    print("DEALERS SHOW CARD:")
    print(f"{dealerHand[0][1]} of {dealerHand[0][0]}\n")
    print("YOUR CARDS:")
    for card in playerHand:
        print(f"{card[1]} of {card[0]}")
    return playerHand, dealerHand, bet, deck

def display_result(dealerHand):
    print("DEALER'S CARDS:")
    for card in dealerHand:
        print(f"{card[1]} of {card[0]}")

def point_total(playerTotal, dealerTotal):
    print(f"YOUR POINTS:\t {playerTotal}")
    print(f"DEALER'S POINTS: {dealerTotal}")

def dealer_continue(dealerTotal, dealerHand, deck):
    while dealerTotal < 17:
            dealerHand.append(deck.pop())
            dealerTotal = calculate_total(dealerHand)
    return dealerTotal

def main(): 
    display_title()
    money = db.read_money()
    
    while True:
        if money < 5:
           money = buy_chips(money)
            
        playerHand, dealerHand, bet, deck = start_round(money)
        check_for_ace(playerHand)
        playerTotal = calculate_total(playerHand)
        dealerTotal = calculate_total(dealerHand)
        
        while playerTotal <= 21:
            playerChoice = hit_or_stand()
            if playerChoice == "hit":
                deal_card(playerHand, deck)
                check_for_ace(playerHand)
                playerTotal = calculate_total(playerHand)
                
                # Display player's updated cards on hit
                print("\nYOUR CARDS:")
                for card in playerHand:
                    print(f"{card[1]} of {card[0]}")
            elif playerChoice == "stand":
                break
            
        # Dealer's turn if player didn't bust
        if playerTotal <= 21:
            dealerTotal = dealer_continue(dealerTotal, dealerHand, deck)
            print()
            display_result(dealerHand)
            print()
            point_total(playerTotal, dealerTotal)
        print()
        money = win_check(playerTotal, dealerTotal, bet, money, playerHand, dealerHand)
        print(f"Money: {money}")
        print()
        
        # Ask if the player would like to play again
        repeat = input("Play again? (y/n): ").lower()
        print()
        if repeat != "y":
                print("Come back soon!")
                print("Bye!")
                break
        
if __name__ =="__main__":
    main()
