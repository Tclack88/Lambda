# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = [] # Initialize room with empty item list

    n_to, s_to, e_to, w_to = None, None, None, None
