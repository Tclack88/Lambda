from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
def move_to_front(direction, dir_list):
    # Helper function moves last direction to front of dir_list
    # The strategy here is if we enter a room from a certain direction
    # we want to guarantee we search all other directions before returning
    # back the way we came
    dir_map = dict(zip(list('nsew'),list('snwe')))
    opposite = dir_map[direction]
    dir_list.remove(opposite)
    random.shuffle(dir_list) # a little randomness added
    dir_list.insert(0,opposite)
    return dir_list

def find_traversal_path():
    player = Player(world.starting_room)
    visited = {} # empty dict - keeps track of available rooms left to travel
    traversal_path = [] # Fill this out with directions to walk
    exits = player.current_room.get_exits() # initialize with starting room
    random.shuffle(exits)
    current_room = player.current_room.id
    visited[current_room] = exits # available directions

    possible =  len(exits) # number of untraveled directions from current room
    while possible and len(visited) < len(world.rooms):

        direction = visited[current_room].pop()
        player.travel(direction)
        traversal_path.append(direction) # add moved direction to plan
        current_room = player.current_room.id
        been_here = visited.get(current_room, False) # in visited
        #print('been here results:', been_here)
        if been_here == False:
            exits = player.current_room.get_exits()

            # Technically unnecessary, you can always reverse
            possible =  len(exits)

            #lower priority of incoming dir 
            exits = move_to_front(direction, exits)

            # fill new room with possible directions
            visited[current_room] = exits 
        else:
            exits = visited[current_room]
            possible = len(exits)
    return traversal_path

# an attempt to find good seeds
"""
best_seed = 0
shortest_path = list(range(976))
for i in range(100000,100000):
    seed = i#random.random()
    random.seed(seed)
    path = find_traversal_path()
    if len(path) < len(shortest_path):
        print(len(path))
        shortest_path = path
        best_seed = seed
#seed = 42399
#random.seed(seed)
shortest_path = find_traversal_path()
# 1500 - 979
# 42399 - 976
# 64593 - 972
"""
seed = 64593
random.seed(seed)
traversal_path = find_traversal_path()
print(traversal_path)
print(len(traversal_path))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# print(best_seed)
# 0.17099177144031374 #986
# 0.06258836739297668 # 983
# 0.2553686938100177 # 982
# 0.9055836619636203 # 980
# 0.05763736522638174 # 976
# 0.9138485912232297 # 975
# 0.38443917323287535 # 973
# 0.7619292885115568 # 972
# 0.4682849504758828 # 971
# 0.3400765161574655 # 968
# 
#######
# UNCOMMENT TO WALK AROUND
#######
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""


# Best path I've found - 968 steps
"""

['w', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w', 'w', 's', 'n', 'w', 's', 's', 's', 'w', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'e', 's', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 's', 's', 's', 's', 'w', 's', 's', 's', 'n', 'n', 'w', 's', 'w', 'e', 's', 'w', 'e', 'n', 'n', 'e', 'n', 'e', 's', 's', 's', 's', 'w', 'e', 'n', 'e', 's', 'n', 'e', 's', 's', 's', 'w', 'e', 'n', 'e', 'w', 'n', 'n', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 's', 'w', 'w', 'w', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 's', 's', 's', 'e', 'w', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'n', 'n', 'n', 'n', 'e', 'n', 'n', 'e', 'e', 's', 'w', 's', 'n', 'e', 'n', 'e', 'n', 'w', 'w', 'n', 's', 'w', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'n', 'w', 'w', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', 'w', 'w', 'e', 'e', 'e', 's', 'n', 'n', 'e', 'n', 's', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'n', 'w', 'e', 'n', 'n', 's', 'w', 'n', 'n', 'n', 'w', 'n', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 's', 'w', 'n', 's', 'e', 's', 'w', 'w', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'w', 'w', 'e', 'e', 'n', 'n', 'n', 'n', 'w', 'e', 'n', 'n', 's', 's', 's', 's', 's', 'w', 'w', 'w', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'e', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 'e', 'n', 'n', 's', 's', 'e', 's', 'e', 's', 'e', 'e', 'e', 'e', 'e', 'e', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'e', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 'e', 'n', 'n', 's', 'e', 'e', 'w', 's', 'n', 'w', 's', 'w', 's', 'w', 's', 's', 'e', 'e', 'w', 'n', 'e', 'n', 's', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'w', 's', 'w', 'w', 'w', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 'n', 'w', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'n', 'w', 'w', 'e', 'e', 's', 'w', 's', 's', 's', 'w', 'w', 'w', 'w', 'w', 'n', 's', 'w', 'n', 's', 'e', 'e', 's', 'w', 'e', 'n', 'e', 'n', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 's', 's', 'e', 'e', 'n', 'n', 's', 'w', 'n', 's', 'e', 's', 'e', 'e', 'n', 'n', 's', 's', 'w', 's', 'e', 'w', 's', 's', 'e', 'e', 'w', 'w', 's', 'w', 'n', 'n', 'w', 'n', 'e', 'w', 'w', 'e', 's', 'e', 's', 's', 'e', 's', 's', 's', 'n', 'w', 's', 's', 'e', 's', 's', 's', 's', 'w', 'w', 's', 'w', 'e', 's', 's', 'w', 'e', 's', 'w', 'e', 's', 'e', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's', 'w', 'w', 's', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'w', 's', 'n', 'e', 's', 'n', 'n', 'w', 'n', 's', 'e', 'e', 'n', 'n', 'n', 'w', 'w', 's', 'n', 'e', 'e', 'n', 'n', 'w', 'e', 'e', 'e', 's', 'e', 's', 's', 'n', 'n', 'e', 's', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 's', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'e', 's', 'e', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 'n', 'n', 'w', 'w', 's', 's', 's', 'e', 's', 's', 's', 'e', 's', 'e', 'e', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'e', 'e', 'n', 'e', 's', 's', 'n', 'n', 'e', 'e', 'w', 's', 's', 's', 's', 'n', 'n', 'e', 'w', 'n', 'n', 'w', 'w', 's', 'w', 'w', 'w', 's', 's', 'w', 's', 'n', 'e', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 's', 'n', 'w', 'n', 'e', 'w', 'w', 's', 'w', 'e', 'n', 'n', 's', 'e', 'n', 'e', 'e', 'e', 'e', 's', 'n', 'e', 's', 'e', 'e', 'e', 'n', 's', 'e', 'w', 'w', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'e', 'n', 'e', 'n', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 'e', 'e', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'e', 'w', 'n', 'e', 'w', 's', 'w', 'w', 's', 'n', 'w', 's', 'w', 's', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 's', 'w', 's', 'e', 's', 's', 'e', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 'e', 'e', 's', 'n', 'e', 'w', 'w', 'w', 's', 's', 's', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'w', 'w', 'n', 'n', 'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'w', 'w', 'n', 'w', 's', 's', 'n', 'n', 'n', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 'e', 'n', 'n', 'e', 'n', 'n', 'e', 'n', 's', 'e', 'n', 's', 'e', 'n', 's', 'e', 'w', 'w', 'w', 'w', 's', 's', 'w', 'n', 's', 's', 's', 'w', 's', 'w', 's', 'w', 's', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'w', 'n', 'w', 'e', 's', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'e', 'n', 'n', 's', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'n', 's', 's', 'w', 'w', 'e', 's']
"""
