suits = ["Clubs","Diamonds","Hearts","Spades"]
ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]


import random
def initialize_deck(suits,rank):
    cards = []
    for suit in suits:
        for rank in ranks:
            if rank == "King" or rank == "Queen" or rank == "Jack":
                value = 10
            elif rank == "Ace":
                value = 0
            else:
                value = int(rank)

            card = [suit,rank,value]
            cards.append(card)

    return cards

cards = initialize_deck(suits, ranks)
numOfCards = 0


random.shuffle(cards)

for card in cards:
    numOfCards += 1
    print(f"card is {card[1]} of {card[0]}. value: {card[2]}. total cards: {numOfCards}")



