class Menu:
    def __init__(self, title="Main Menu"):
        self.title = title
        self.options = []
        self.functions = {}

    def add_option(self, option_text, function):
        self.options.append(option_text)
        self.functions[len(self.options)] = function

    def display(self):
        print(f"\n{self.title}")
        print("=" * len(self.title))
        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")
        print("0. Exit")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    print("Exiting menu.")
                    break
                elif choice in self.functions:
                    self.functions[choice]()
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Please enter a valid number.")

# TEST CODE BELOW TO FUCK AROUND W IT
#========================================================================
# these are just random functions so you can call the menu and test it out
def view_items():
    print("Viewing items...")

# these are just random functions so you can call the menu and test it out
def add_item():
    print("Adding an item...")

# these are just random functions so you can call the menu and test it out
def remove_item():
    print("Removing an item...")

if __name__ == "__main__":
    menu = Menu("Example Menu")
    menu.add_option("View Items", view_items)
    menu.add_option("Add Item", add_item)
    menu.add_option("Remove Item", remove_item)
    # so now instead of creating the entire men u structure you can
    # create a menu object and add options and then run it when you 
    # need it

    menu.run()
