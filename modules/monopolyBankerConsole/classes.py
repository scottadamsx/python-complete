class player:
    def __init__(self, name, wallet, properties=[], monopolies=[], boardSpace=0):
        self.name = name
        self.wallet = wallet
        self.properties = properties
        self.monopolies = monopolies  # List of monopolies the player owns
        self.boardSpace = boardSpace
        self.doubles_count = 0  # Initialize doubles count to 0
        



class property:
    def __init__(self, name, price, color, housePrice, houses, rent, rent1, rent2, rent3, rent4, rent5, morgageValue, owner="none"):
        self.name = name
        self.price = price
        self.color = color
        self.housePrice = housePrice
        self.houses = houses
        self.rent = rent
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4
        self.rent5 = rent5
        self.morgageValue = morgageValue
        self.owner = owner

    def __str__(self):
        return self.name  # Will print the property name


    def payRent(self, player):
        if self.houses == 0:
            rent = self.rent
        elif self.houses == 1:
            rent = self.rent1
        elif self.houses == 2:
            rent = self.rent2
        elif self.houses == 3:
            rent = self.rent3
        elif self.houses == 4:
            rent = self.rent4
        elif self.houses == 5:
            rent = self.rent5

        player.wallet -= rent
        return player.wallet