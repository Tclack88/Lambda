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
    dir_list.insert(0,opposite)
    return dir_list

visited = {} # empty dictionary to keep track of available rooms left to travel
traversal_path = [] # Fill this out with directions to walk
# initialize with starting room
exits = player.current_room.get_exits()
current_room = player.current_room.id
visited[current_room] = exits # available directions

possible =  len(exits) # number of untraveled directions from current room
while possible:
    direction = visited[current_room].pop()
    player.travel(direction)
    traversal_path.append(direction) # add moved direction to plan
    current_room = player.current_room.id
    been_here = visited.get(current_room, False) # in visited
    #print('been here results:', been_here)
    if been_here == False:
        exits = player.current_room.get_exits()
        possible =  len(exits) # Technically unnecessary, you can always reverse
        exits = move_to_front(direction, exits) #lower priority of incoming dir 
        visited[current_room] = exits # fill new room with possible directions
    else:
        exits = visited[current_room]
        possible = len(exits)

#print(traversal_path)

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
