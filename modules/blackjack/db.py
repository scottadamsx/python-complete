def read_money():
    try:
        with open("data/money.txt", "r") as file:
            money = float(file.read())
    except FileNotFoundError:
        print("Error: Money file not found. Starting with $100.")
    return money

def write_money(money):
    with open("data/money.txt", "w") as file:
        file.write(str(round(money, 2)))
