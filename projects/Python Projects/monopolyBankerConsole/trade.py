from main import check_for_monopoly
def make_trade(currentPlayer, playerList):
    trader = currentPlayer
    print(f"\n{trader.name}'s turn to create an offer!")

    # Step 3: Tradee creates an ask
    tradee = select_tradee(trader, playerList)  # A function to select a tradee
    tradee_properties_to_trade = []
    tradee_money = 0
    
    # Step 1: Trader creates an offer
    trader_properties_to_trade = []
    trader_money = 0

    # Trader selects properties and money for the offer
    print(f"\n{trader.name}, choose properties and money for your offer:")
    
    print(f"\n{trader.name}'s properties:")
    for i, property in enumerate(trader.properties, 1):
        print(f"{i}. {property.name} - Price: {property.price}")
    print(f"Wallet balance: ${trader.wallet}")
    while True:
        property_choice = input("Select a property by number to offer (or 'ENTER' to finish): ")
        if property_choice.lower() == '':
            break
        try:
            property_index = int(property_choice) - 1
            if 0 <= property_index < len(trader.properties):
                property_to_trade = trader.properties[property_index]
                if property_to_trade not in trader_properties_to_trade:
                    trader_properties_to_trade.append(property_to_trade)
                    print(f"{property_to_trade.name} added to your offer.")
                else:
                    print(f"{property_to_trade.name} is already in your offer list.")
            else:
                print("Invalid choice. Please select a valid property.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Trader offers money
    while True:
        try:
            trader_money = int(input(f"How much money would you like to offer? (Available balance: ${trader.wallet}): "))
            if trader_money <= trader.wallet:
                break
            else:
                print("You don't have enough money.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    

   

    

    print(f"\n{trader.name}, it's time to create an ask!")
    # Tradee selects properties and money for their ask
   
    print(f"\n{tradee.name}'s properties:")
    for i, property in enumerate(tradee.properties, 1):
        print(f"{i}. {property.name} - Price: {property.price}")
    print(f"Wallet balance: ${tradee.wallet}")
    while True:    
        property_choice = input("Select a property by number to ask (or ENTER to finish): ")
        if property_choice.lower() == '':
            break
        try:
            property_index = int(property_choice) - 1
            if 0 <= property_index < len(tradee.properties):
                property_to_trade = tradee.properties[property_index]
                if property_to_trade not in tradee_properties_to_trade:
                    tradee_properties_to_trade.append(property_to_trade)
                    print(f"{property_to_trade.name} added to your ask.")
                else:
                    print(f"{property_to_trade.name} is already in your ask list.")
            else:
                print("Invalid choice. Please select a valid property.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Tradee offers money
    while True:
        try:
            tradee_money = int(input(f"How much money would you like to ask for? (Available balance: ${tradee.wallet}): "))
            if tradee_money <= tradee.wallet:
                break
            else:
                print("You don't have enough money.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

     # Step 2: Show the offer and calculate the total value
    trader_offer_value = trader_money + sum([property.price for property in trader_properties_to_trade])
    print(f"\n{trader.name}'s offer:")
    print(f"Properties: {[property.name for property in trader_properties_to_trade]}")
    print(f"Money: ${trader_money}")
    print(f"Total offer value: ${trader_offer_value}") 

    # Step 4: Show the ask and calculate the total value
    tradee_ask_value = tradee_money + sum([property.price for property in tradee_properties_to_trade])
    print(f"\n{trader.name}'s ask:")
    print(f"Properties: {[property.name for property in tradee_properties_to_trade]}")
    print(f"Money: ${tradee_money}")
    print(f"Total ask value: ${tradee_ask_value}")

    # Step 5: Compare the values of the offer and ask
    print("\nComparing the offer and the ask:")
    if trader_offer_value == tradee_ask_value:
        print("Both the offer and the ask have the same total value.")
    elif trader_offer_value > tradee_ask_value:
        print(f"{trader.name}'s offer is higher by ${trader_offer_value - tradee_ask_value}.")
    else:
        print(f"{trader.name}'s ask is higher by ${tradee_ask_value - trader_offer_value}.")

    # Step 6: Tradee decides
    print(f"\n{tradee.name}, do you want to accept the offer, make a counteroffer, or decline?")
    decision = input("Enter 'a' - (accept), 'c' - (counter offer), or 'd' - (decline): ").lower()

    # handles the logic for the decision for the trade
    if decision == 'a':
        print("Trade accepted! Finalizing the exchange...")
        finalize_trade(trader, tradee, trader_properties_to_trade, tradee_properties_to_trade, trader_money, tradee_money)
    elif decision == 'c':
        print(f"{tradee.name} is making a counteroffer!")
        make_trade(tradee, playerList)  # Allow tradee to make a counteroffer
    elif decision == 'd':
        print("Trade declined. No exchange will happen.")
    else:
        print("Invalid decision. Trade canceled.")

def select_tradee(trader, playerList):
    """Helper function to select the tradee from the player list."""
    print("\nSelect the player to trade with:")
    for i, player in enumerate(playerList):
        if player != trader:
            print(f"{i + 1}. {player.name}")
    
    while True:
        try:
            tradee_choice = int(input(f"Choose a player to trade with (1-{len(playerList)}): ")) - 1
            if 0 <= tradee_choice < len(playerList) and playerList[tradee_choice] != trader:
                return playerList[tradee_choice]
            else:
                print("Invalid choice. Please select a valid player.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def finalize_trade(trader, tradee, trader_properties, tradee_properties, trader_money, tradee_money):
    """Helper function to finalize the trade."""
    # Money exchange
    trader.wallet -= trader_money
    tradee.wallet += trader_money
    tradee.wallet -= tradee_money
    trader.wallet += tradee_money

    # Property exchange
    for property in trader_properties:
        trader.properties.remove(property)
        tradee.properties.append(property)
        property.owner = tradee.name
    check_for_monopoly(tradee)

    for property in tradee_properties:
        tradee.properties.remove(property)
        trader.properties.append(property)
        property.owner = trader.name
    check_for_monopoly(trader)    

    print("\nTrade completed successfully!")
