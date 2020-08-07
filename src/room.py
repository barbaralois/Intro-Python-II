# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    
    def list_items(self):
        print(f"\nIn this room you can see the following:")
        for id, item in enumerate(self.items, 1):
            print(f"{id}) {item}")
        print("Want to (take) an item?\n")
        
    def __str__(self):
        return f"{self.name}\n{self.description}"