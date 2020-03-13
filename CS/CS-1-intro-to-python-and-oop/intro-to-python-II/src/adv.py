import os
from room import Room
from player import Player
from item import Item
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
item = {
        'stick' : Item('stick', "It's a stick... what else do you want to know?"),

        'mudball' : Item('mudball', """Nothing screams \"I've got my shit together\" 
            more than carrying a ball of mud with you"""),

        'towel' : Item('towel', """A towel is just about the most massively useful
            thing a hitchhiker can carry. Partly because it has great practical
        value. You can wrap it around you for warmth, you can lie on it, you can
        sleep under it, use it to sail a miniraft, wet it in hand-to-hand combat
        wrap it around your head to ward off noxious fumes or avoid the gaze
        of ravenous creatures. You can wave your towel in emergencies as a distress
        signal an ofcourse you can dry yourself off with it it it seems to be
        clean enough. Most importantly a towel has immense psychological value.
        Any man who can struggle agains terrible odds and still knows where
        his towel is, is clearly a man to be reckoned with"""),

        'sword' : Item('sword', """It's a weapon, not as versatile as a towel
        but it gets the job done""")
        }

player = Player('test player', room['outside'])
room['outside'].items = [item['stick'], item['mudball']]
room['treasure'].items = [item['towel']]
room['overlook'].items = [item['sword']]

#player.current_room = room['outside'] # Maybe unecessary, set this to default
resp = 'the game has begun' # Filler start, doesn't actually matter
while resp[0] != 'q':
    
    print(f"Current room:{player.current_room.name} \
            \n{player.current_room.description} \
            \nitems in room: {', '.join([item.name for item in player.current_room.items])}")
    print("\nIn which direction would you like to head traveller?")
    # Give a GUI for actions and movement
    print(f"""
        n       i(inventory - {len(player.items)}       ACTIONS         NOUNS
    w       e   q(quit)             (take, drop)      (item)
        s""")
    resp = input("~~~~~~~~~~~: ")
    # Parse response into verbs and nouns. Beyond two inputs are ignored
    verb_noun = ['verb','noun']
    resp_list = resp.split()
    verb_noun_dict = dict(zip(verb_noun,resp_list))
    verb, noun = verb_noun_dict.get('verb', False), verb_noun_dict.get('noun', False)
    try:
        if noun: # Check if 2nd argument is made, if so, assume it's a noun
            if verb == 'take':
                player.gain_item(item.get(noun, False)) # return False if not exist
            elif verb == 'drop':
                player.lose_item(item.get(noun, False))
            else:
                raise AttributeError
        else: # If eval fails, exec will not change
            next_room = eval(f'player.current_room.{verb}_to')
            if next_room != None:
                exec(f'player.current_room = player.current_room.{verb}_to')
                os.system('clear')
            else:
                os.system('clear')
                print("Can't Move in this direction")
                time.sleep(1)
    except AttributeError:
        if resp[0] == 'q':
            print("Goodbye for now")
        elif resp[0] == 'i':
            os.system('clear')
            player.show_inventory()
            time.sleep(1)
        else:
            os.system('clear')
            print(f'invalid option, "{resp}" not understood, try again...')
            time.sleep(1)


