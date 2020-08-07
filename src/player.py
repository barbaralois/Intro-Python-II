# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, inventory=[]):
        self.location = location
        self.inventory = []
    
    def __str__(self):
        return f"\nYou find yourself in the {self.location}"

    def add_to_inventory(self, item):
        self.inventory.append(item)
        self.print_inventory()

    def print_inventory(self):
        print("\nYour inventory contains the following:\n",[f"{item}" for item in self.inventory])