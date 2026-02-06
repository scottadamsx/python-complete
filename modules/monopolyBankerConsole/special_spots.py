import random

def handle_special_spot(newSpace, currentPlayer, playerList):
    chance_deck = [
    {"message": "Advance to Go (Collect $200)", "effect": "go"},
    {"message": "Go back three spaces", "effect": "move_back", "spaces": 3},
    {"message": "Pay $50 to each player", "effect": "pay_players", "amount": 50},
    {"message": "Advance to Boardwalk", "effect": "move_to_space", "space": 39},
    {"message": "Bank pays you dividend of $50", "effect": "collect_money", "amount": 50},
    {"message": "Move forward to the nearest railroad", "effect": "move_to_nearest_railroad"},
    {"message": "Get out of jail free", "effect": "get_out_of_jail"},
    {"message": "Pay $100 in taxes", "effect": "pay_tax", "amount": 100},
    {"message": "Collect $150 for passing Go", "effect": "collect_money", "amount": 150},
    {"message": "Advance to Illinois Avenue", "effect": "move_to_space", "space": 24},
    {"message": "Pay $25 for car repairs", "effect": "pay_money", "amount": 25},
    {"message": "Move to nearest utility", "effect": "move_to_nearest_utility"}
    # Add 18 more cards as per the standard rules or create new ones as needed
        ]

    community_chest_deck = [
    {"message": "Advance to Go (Collect $200)", "effect": "go"},
    {"message": "Bank error in your favor, collect $200", "effect": "collect_money", "amount": 200},
    {"message": "Doctor's fee, pay $50", "effect": "pay_money", "amount": 50},
    {"message": "You inherit $100", "effect": "collect_money", "amount": 100},
    {"message": "Pay school fees of $150", "effect": "pay_money", "amount": 150},
    {"message": "Get out of jail free", "effect": "get_out_of_jail"},
    {"message": "You have won second prize in a beauty contest, collect $10", "effect": "collect_money", "amount": 10},
    {"message": "Go directly to Jail", "effect": "go_to_jail"},
    {"message": "You are assessed for street repairs, pay $40", "effect": "pay_money", "amount": 40},
    {"message": "Receive $25 from a lawsuit", "effect": "collect_money", "amount": 25},
    {"message": "Collect $100 for passing Go", "effect": "collect_money", "amount": 100},
    {"message": "Move to nearest railroad", "effect": "move_to_nearest_railroad"}
    # Add 18 more cards as per the standard rules or create new ones as needed
        ]
    if newSpace == "chance":
        draw_card(chance_deck, currentPlayer, playerList)
    elif newSpace == "community chest":
         draw_card(community_chest_deck, currentPlayer, playerList)
    elif newSpace == "income tax":
        print("You landed on income tax! pay 100$ to the bank!")
        currentPlayer.wallet -= 100
    elif newSpace == "just visiting":
        print("Just Visiting! say hi to all the convicted felons. ")
    elif newSpace == "free parking":
        print("Free Parking! take a rest. ")
    elif newSpace == "luxury tax":
        print("You landed on luxury tax! pay 100$ to the bank!")
        currentPlayer.wallet -= 100
    else:
        print(f"{currentPlayer.name} landed on {newSpace}. This is a special space. More development coming soon!")



def draw_card(deck, player, playerList):

    card = random.choice(deck)

    

    print(f"{player.name} landed on \n{player.name} drew a card: {card['message']}")
    
    if card["effect"] == "go":
        player.wallet += 200
        print(f"{player.name} collects $200 for passing Go!")
    elif card["effect"] == "move_back":
        # Logic for moving back spaces can go here (this is a simplified version)
        print(f"{player.name} moves back {card['spaces']} spaces.")
    elif card["effect"] == "pay_players":
        # Assume this is paying every other player $50
        for other_player in playerList:
            if other_player != player:
                player.wallet -= 50
                other_player.wallet += 50
                print(f"{player.name} pays $50 to {other_player.name}.")
    elif card["effect"] == "collect_money":
        player.wallet += card["amount"]
        print(f"{player.name} collects ${card['amount']}!")
    elif card["effect"] == "move_to_space":
        # Assuming we know the space index (just an example)
        print(f"{player.name} moves to space {card['space']}.")
    elif card["effect"] == "pay_tax":
        player.wallet -= card["amount"]
        print(f"{player.name} pays ${card['amount']} in taxes.")
    elif card["effect"] == "get_out_of_jail":
        print(f"{player.name} gets out of jail free!")
    elif card["effect"] == "pay_money":
        player.wallet -= card["amount"]
        print(f"{player.name} pays ${card['amount']}.")
    elif card["effect"] == "go_to_jail":
        print(f"{player.name} goes directly to Jail!")
    elif card["effect"] == "move_to_nearest_railroad":
        # Here we can add logic to move to the nearest railroad
        print(f"{player.name} moves to the nearest railroad.")
    elif card["effect"] == "move_to_nearest_utility":
        # Logic for moving to the nearest utility
        print(f"{player.name} moves to the nearest utility.")
