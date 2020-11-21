from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def get(self):
        return self.stack
    def size(self):
        return len(self.stack)

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

# print(f'room_graph: {room_graph}')
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = ['w','w','e','e','e','e','w','w','s','s','n','n', 'n','n']


# TRAVERSAL TEST

visited_rooms = set() # create a store to save the visited rooms
player.current_room = world.starting_room #  set the first room  to be 000
# visited_rooms.add(player.current_room)

# Store the final list of movements 
traversal_path = [] 

# Store the possible direstions for each room
traversal_graph = dict() 

# Will implement DFT so will use a stack to keep track of the room navigation path
s = Stack()

# Push the first room into the stack 
s.push([player.current_room]) 

# Loop while there are still rooms into the stack
while s.size() > 0:

    # Extract the last added room from the stack
    path = s.pop()
    # print(f'path[-1]: {path[-1]}')

    # Take the last room from the path and explore it 
    exploring_room = path[-1]

    # If the exploring_room is nit in the visited rooms set
    if exploring_room not in visited_rooms:

        # We add it to the set
        visited_rooms.add(exploring_room)

        # Add the exploring rooms' id as a key in the traversal_graph and give the '?' values     
        traversal_graph[exploring_room.id] = {"n": "?", "s": "?", "e": "?", "w": "?", }

        # Get all the exits/neighbors rooms of the players' current_room
        exits = player.current_room.get_exits()

        for exit_room in exits:
           
            # Get the neighbor room of the exploring room 
            neighbor_room = exploring_room.get_room_in_direction(exit_room)

            # If there is a neighbor room
            if neighbor_room != None:

                # Append the direction to the neighbor room to the traversal_path
                traversal_path.append(exit_room)
                
                # Change the '?' from the traversal_graph to the neighbor_room id
                traversal_graph[exploring_room.id][exit_room] = neighbor_room.id

            
                # Set the next room to explore the neighbor room
                next_room = neighbor_room

                # Create a copy of the path and add to it the next room to it
                new_path = [*path, next_room]

                # Add the new path to the stack to be explored. 
                s.push(new_path)

            # Else if there is no neighbor room
            else:
                # Change the rest of the '?' in the traversal_graph to be None
                traversal_graph[exploring_room.id][exit_room] = None



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
