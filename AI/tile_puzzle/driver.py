#!/usr/bin/python3
import math
import argparse
import copy
import timeit
import resource 


class Board:
    'Holds all tiles of the puzzle'
    
    def __init__(self, size):
        self.size=size
        self.all_tiles=[]
        self.parent_state=self
        self.pos_in_explored=0

    def __eq__(self,other):
        for i in range(0,self.size):
            if self.all_tiles[i].value!=other.all_tiles[i].value:
                return False
        return True

    def print_state(self):
        for i in range(0,int(math.sqrt(self.size))):
            print(self.all_tiles[i*int(math.sqrt(self.size))].value,self.all_tiles[i*int(math.sqrt(self.size))+1].value,self.all_tiles[i*int(math.sqrt(self.size))+2].value )
        print("\n")
        

    def store_parent(self, state, pos):
        self.parent_state=state
        self.pos_in_explored=pos

    def switch_tile_vals(self, element_one, element_two):
        tmp=self.all_tiles[element_one].value
        self.all_tiles[element_one].value=self.all_tiles[element_two].value;
        self.all_tiles[element_two].value=tmp
        return


class Tile:
    'One tile of the puzzle'

    def __init__(self, pos, value):
        self.pos=pos
        self.value=value
        self.next=[]

    def save_neighbours(self, neighbour_tile):
        self.next.append(neighbour_tile);

def get_neighbours(board):
    width=math.sqrt(board.size)
    tiles=board.all_tiles
    for i in range (0, board.size):
        if i-width>=0:
            tiles[i].save_neighbours(int(i-width))
        if i+width<board.size:
            tiles[i].save_neighbours(int(i+width))
        if i-1>=0:
            if i%width!=0:
                tiles[i].save_neighbours(i-1)
        if i+1<board.size:
            if (i+1)%width!=0:
                tiles[i].save_neighbours(i+1)
    return

#returns path to goal
#apparently reaches maximum recursion depth while running complex inits
def parents_list(start_state, goal_state, explored):
    path_to_goal=[]
    path_to_goal.append(goal_state)
    while not path_to_goal[-1]==start_state:
        path_to_goal.append(path_to_goal[-1].parent_state)
    path_to_goal=list(reversed(path_to_goal))
    return path_to_goal


def get_list_of_moves(path):
    list_of_moves=[]
    width=int(math.sqrt(path[0].size))
    for i in range(0,len(path_to_goal)-1):
        for tile in range(0,len(path_to_goal[i].all_tiles)):
            if path_to_goal[i].all_tiles[tile].value==0:
                for tile_next in range(0,len(path_to_goal[i+1].all_tiles)):
                    if path_to_goal[i+1].all_tiles[tile_next].value==0:
                        if tile==tile_next+1:
                            list_of_moves.append('Left')
                        if tile==tile_next-1:
                            list_of_moves.append('Right')
                        if tile==tile_next+width:
                            list_of_moves.append('Up')
                        if tile==tile_next-width:
                            list_of_moves.append('Down')
    return list_of_moves




#---------------------------------------------------------------------------------------
# BREADTH FIRST SEARCH
#---------------------------------------------------------------------------------------


def Breadth_First_Search(board, goal_board):
    print("\n")
    print("\n")
    print("Beginning BFS")
    print("\n")
    fringe=[]
    explored=[]
    fringe.append(board)
    board.store_parent(board, 0)
    
    max_fringe_size=1
    nodes_exp=1
    while fringe:
        state=copy.deepcopy(fringe[0])
        explored.append(state)

        if state==goal_board:
            print("explore ",nodes_exp," states to solve the tile puzzle")
            return state

        for i in range(0,state.size):
        #    print("checking tile on the board for moving tile 0 at pos ",i)
            if state.all_tiles[i].value==0:
         #       print("found tile 0")
                for el in range(0,len(state.all_tiles[i].next)):
                    new_state=copy.deepcopy(state)
                    new_state.switch_tile_vals(i, state.all_tiles[i].next[el])
                    is_new=True
                    for ex in range(0,len(explored)):
                        if new_state==explored[ex]:
                            is_new=False
                    for fr in range(0,len(fringe)):
                        if new_state==fringe[fr]:
                            is_new=False
                    if is_new:
                        fringe.append(new_state)
                        new_state.store_parent(state, len(explored))
                        nodes_exp=nodes_exp+1
                        if max_fringe_size<len(fringe):
                            max_fringe_size=len(fringe)
                        if new_state==goal_board:
                            print("max_fringe_size:", max_fringe_size)
                            print("nodes_expanded:", nodes_exp)
                            return parents_list(board, new_state, explored)

        #delete first element in the fringe and order the rest accoridngly
        fringe.pop(0)

    return 

#---------------------------------------------------------------------------------------
# DEPTH FIRST SEARCH
#---------------------------------------------------------------------------------------

def Depth_First_Search(board, goal_board):
    print("\n\n")
    print("Beginning DFS")
    print("\n")
    fringe=[]
    explored=[]
    fringe.append(board)
    
    nodes_exp=1
    max_fringe_size=1

    while fringe:
        state=copy.deepcopy(fringe[-1])
        fringe.pop(-1)
        explored.append(state)

        if state==goal_board:
            return state

        for i in range(0,state.size):
            if state.all_tiles[i].value==0:
                for el in range(len(state.all_tiles[i].next)-1,-1,-1):
                    new_state=copy.deepcopy(state)
                    new_state.switch_tile_vals(i, state.all_tiles[i].next[el])
                    is_new=True
                    for ex in range(0,len(explored)):
                        if new_state==explored[ex]:
                            is_new=False
                    for fr in range(0,len(fringe)):
                        if new_state==fringe[fr]:
                            is_new=False
                    if is_new:
                        fringe.append(new_state)
                        new_state.store_parent(state, len(explored))
                        nodes_exp=nodes_exp+1
                        if max_fringe_size<len(fringe):
                            max_fringe_size=len(fringe)
                        if new_state==goal_board:
                            print("max_fringe_size:", max_fringe_size)
                            print("nodes_expanded:", nodes_exp)
                            return parents_list(board, new_state, explored)

    return 

#------------------------------------------------------------------------------------
#Beginning MAIN program
#------------------------------------------------------------------------------------
start_time=timeit.default_timer()

#reading input from console
parser = argparse.ArgumentParser()
parser.add_argument("algorithm", action="store")
parser.add_argument("tiles", action="store")
args=parser.parse_args()

#initialising start state
init_dist=[int(x) for x in args.tiles.split(',')]

board=Board(len(init_dist))
for x in range(0,len(init_dist)):
    tile=Tile(x, init_dist[x])
    board.all_tiles.append(tile)

#get neighbours for creating the next states for the search space
get_neighbours(board)

#initialze goal state
goal_board=Board(len(init_dist))
for x in range(0,len(init_dist)):
    tile=Tile(x, x)
    goal_board.all_tiles.append(tile)


#Calling the specified algorithms
nodes_exp=0
max_fringe_size=0
if args.algorithm=="bfs":
    path_to_goal=Breadth_First_Search(board, goal_board)
elif args.algorithm=="dfs":
    path_to_goal=Depth_First_Search(board, goal_board)

#printing the solution step by step
#for i in range(0,len(path_to_goal)):
#    path_to_goal[i].print_state()

list_of_moves=get_list_of_moves(path_to_goal)

#for bfs and dfs search_depth is equal to cost_of_path
search_depth=len(list_of_moves)
if args.algorithm=="bfs":
    maximum_search_depth=search_depth


#output of wanted parameters:
#for move in list_of_moves:
print(list_of_moves)
print("cost_of_path:", len(list_of_moves))


#code ending 
end_time=timeit.default_timer()
print("Maximal RAM Usage:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.)

print("Total Computing Time:", end_time-start_time)
