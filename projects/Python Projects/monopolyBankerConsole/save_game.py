import csv
from classes import player, property

def save_game(FILENAME, playerList, propertyList):
    with open(FILENAME, "w") as file:
        # Save players with their properties and monopolies
        for player in playerList:
            property_names = [prop.name for prop in player.properties]
            monopoly_names = player.monopolies
            player_line = f"{player.name},{player.wallet},{player.boardSpace}," \
                          f"{'|'.join(property_names)},{'|'.join(monopoly_names)}\n"
            file.write(player_line)

        # Add a marker to separate players and properties
        file.write("===PROPERTIES===\n")

        # Save properties
        for prop in propertyList:
            property_line = f"{prop.name},{prop.price},{prop.color},{prop.housePrice},{prop.houses}," \
                            f"{prop.rent},{prop.rent1},{prop.rent2},{prop.rent3},{prop.rent4},{prop.rent5}," \
                            f"{prop.morgageValue},{prop.owner or 'none'}\n"
            file.write(property_line)

        
            

            
def load_game(FILENAME):
    with open(FILENAME, "r") as file:
        playerList = []
        property_dict = {}

        lines = file.readlines()
        section = "players"  # To track which section we're processing

        for line in lines:
            line = line.strip()

            # Switch to property parsing after the marker
            if line == "===PROPERTIES===":
                section = "properties"
                continue

            if section == "players":
                # Parse player data
                name, wallet, boardSpace, player_properties, player_monopolies = line.split(",", maxsplit=4)
                player_properties = player_properties.split("|") if player_properties else []
                player_monopolies = player_monopolies.split("|") if player_monopolies else []
                playR = player(name, int(wallet), int(boardSpace), player_properties, player_monopolies)  # Temporarily hold property names
                playerList.append(playR)

            elif section == "properties":
                # Parse property data
                fields = line.split(",")
                (
                    name, price, color, housePrice, houses, rent, rent1, rent2, rent3, rent4, rent5,
                    mortgageValue, owner
                ) = fields
                prop = property(
                    name,
                    int(price),
                    color,
                    int(housePrice),
                    int(houses),
                    int(rent),
                    int(rent1),
                    int(rent2),
                    int(rent3),
                    int(rent4),
                    int(rent5),
                    int(mortgageValue),
                    owner if owner != "none" else None
                )
                property_dict[name.replace(" ", "_").lower()] = prop

        # Assign properties to players
        for player_obj in playerList:
            player_props = []
            for prop_name in player_obj.properties:  # Temporary property names
                formatted_name = prop_name.replace(" ", "_").lower()
                if formatted_name in property_dict:
                    player_props.append(property_dict[formatted_name])
            player_obj.properties = player_props  # Replace names with actual property objects

        # Return all player data and property variables individually
        return (
            playerList,
            *property_dict.values()  # Expand dictionary values into individual return values
        )

            