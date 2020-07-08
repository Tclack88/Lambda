# Write a class to hold player information, e.g. what room they are in
# currently.
import os
import time


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = [] # begin a blank list to store items

    def show_inventory(self):
        """ Display items the player has taken"""
        if len(self.items) == 0:
            print("No Items in Inventory")
        else:
            print("Inventory Items:")
        for item in self.items:
            print(f'{item} ::: {item.description}\n')

    def gain_item(self, item):
        """ Adds item to inventory, removes from room,
        perform relevant error checks """
        os.system('clear')
        if item:
            self.current_room.items.remove(item)
            self.items.append(item)
            print(f'Added {item} to inventory')
            print(item.description)
            time.sleep(1)
        else:
            print(f'{item} does not appear to be an item in this room')
            time.sleep(1)

    def lose_item(self, item):
        """Removes item to inventory, Adds to room,
        perform relevant error checks """
        os.system('clear')
        try:
            self.items.remove(item)
            self.current_room.items.append(item)
            print(f"""{item.name} bequeathed to the {self.current_room.name}\n
                    so long for now {item}""")
            time.sleep(1)
        except:
            print(f"You can't lose what you don't have...({item} not in your inventory)")
            time.sleep(1)
