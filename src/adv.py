import sys
from room import Room
from player import Player
from item import Item 

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the mouth of a cave beckons.", [Item("rocks", "A number of palm sized rocks"), Item("lantern", "A lantern with an unlit candle"), Item("branch", "A slightly unwieldy stick")]),

    'foyer': Room("Foyer", "Dim light filters in from the opening to the south. Dusty passages run north and east.", [Item("fork", "A rudimentary eating utensil"), Item("handkerchief", "A dirty scrap of fabric")]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", [Item("sweater", "An abandoned blue pullover"), Item("matches", "A small book of matches, slightly damp")]),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The heavy smell of gold permeates the air.", [Item("glasses", "A pair of wire-rimmed glasses"), Item("torch", "A burning torch"), Item("goblet", "A cracked wooden goblet")]),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", [Item("chest", "A small, empty chest"), Item("ruby", "A tiny, but shimmering, red ruby"), Item("boot", "A brown leather boot")]),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player(room['outside'])

print("Hello, and welcome to a new adventure!")

while True:
    print(player)
    player.location.list_items()
    command = input("Which way will you go? (N, S, E, W)\nInventory (I) - Quit (Q)\n> ").split(',')

    if len(sys.argv) == 1:
        if command[0] == 'q':
            break
        elif command[0] == 'i' or command[0] == 'inventory':
            player.print_inventory()
        elif command[0] == 'n':
            # see if player can move north, if so move them
            if hasattr(player.location, 'n_to'):
                player.location = player.location.n_to
            # if not, inform them and let them make another choice
            else:
                print('\nYou try to move North, but find the path impassible.')
                continue
        elif command[0] == 'e':
            # see if player can move east, if so move them
            if hasattr(player.location, 'e_to'):
                player.location = player.location.e_to
            # if not, inform them and let them make another choice
            else:
                print('\nYou try to move East, but find the path impassible.')
                continue
        elif command[0] == 's':
            # see if player can move south, if so move them
            if hasattr(player.location, 's_to'):
                player.location = player.location.s_to
            # if not, inform them and let them make another choice
            else:
                print('\nYou try to move South, but find the path impassible.')
                continue
        elif command[0] == 'w':
            # see if player can move west, if so move them
            if hasattr(player.location, 'w_to'):
                player.location = player.location.w_to
            # if not, inform them and let them make another choice
            else:
                print('\nYou try to move West, but find the path impassible.')
                continue
    else:
        print(sys.argv)
        # if command[0] == 'take':
        #     print('take')
        # elif command[0] == 'drop':
        #     print('drop')

    
