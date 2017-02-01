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
        self.neighbours=[[] for _ in xrange(size)]
        self.parent_state=self
        self.pos_in_explored=0

    def __eq__(self,other):
        if self.all_tiles==other.all_tiles:
            return True
        return False
    
    def __hash__(self):
      return hash(frozenset(self.all_tiles)) 

    def print_state(self):
        for i in range(0,int(math.sqrt(self.size))):
            print(self.all_tiles[i*int(math.sqrt(self.size))],self.all_tiles[i*int(math.sqrt(self.size))+1],self.all_tiles[i*int(math.sqrt(self.size))+2])
        print("\n")
        

    def store_parent(self, pos):
        #self.parent_state=state
        self.pos_in_explored=pos

    def switch_tile_vals(self, element_one, element_two):
        tmp=self.all_tiles[element_one]
        self.all_tiles[element_one]=self.all_tiles[element_two];
        self.all_tiles[element_two]=tmp
        return

    def save_neighbours(self, tile_number, neighbour_tile):
        self.neighbours[tile_number].append(neighbour_tile);


#END OF CLASS DECLARATION:

def get_neighbours(board):
    width=math.sqrt(board.size)
    for i in range (0, board.size):
        if i-width>=0:
            board.save_neighbours(i,int(i-width))
        if i+width<board.size:
            board.save_neighbours(i,int(i+width))
        if i-1>=0:
            if i%width!=0:
                board.save_neighbours(i,i-1)
        if i+1<board.size:
            if (i+1)%width!=0:
                board.save_neighbours(i,i+1)
    return

#returns path to goal
#apparently reaches maximum recursion depth while running complex inits
def parents_list(start_state, goal_state, explored):
    path_to_goal=[]
    path_to_goal.append(goal_state)
    path_to_goal.append(explored[-path_to_goal[-1].pos_in_explored-1])

    while not path_to_goal[-1]==start_state:
      path_to_goal.append(explored[-path_to_goal[-1].pos_in_explored-1])
      if path_to_goal[-1].pos_in_explored-1==0:
	path_to_goal.append(start_state)
    
    path_to_goal=list(reversed(path_to_goal))
    return path_to_goal


def get_list_of_moves(path):
    list_of_moves=[]
    width=int(math.sqrt(path[0].size))
    for i in range(0,len(path_to_goal)-1):
        for tile in range(0,len(path_to_goal[i].all_tiles)):
            if path_to_goal[i].all_tiles[tile]==0:
                for tile_next in range(0,len(path_to_goal[i+1].all_tiles)):
                    if path_to_goal[i+1].all_tiles[tile_next]==0:
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
    board.store_parent(0)
    
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
            if state.all_tiles[i]==0:
         #       print("found tile 0")
                for el in range(0,len(state.neighbours[i])):
                    new_state=copy.deepcopy(state)
                    new_state.switch_tile_vals(i, el)
                    is_new=True
                    for ex in range(0,len(explored)):
                        if new_state==explored[ex]:
                            is_new=False
                    for fr in range(0,len(fringe)):
                        if new_state==fringe[fr]:
                            is_new=False
                    if is_new:
                        fringe.append(new_state)
                        new_state.store_parent(len(explored))
                        nodes_exp=nodes_exp+1
                        if max_fringe_size<len(fringe):
                            max_fringe_size=len(fringe)
                        if new_state==goal_board:
                            print("max_fringe_size:", max_fringe_size)
                            print("nodes_expanded:", nodes_exp)
                            return parents_list(board, new_state, explored)

        counter=counter+1
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
    f=open('time_for_step', 'w')
    fringe=[]
    explored_set=set()
    fringe.append(board)
    
    board.pos_in_explored=0

    nodes_exp=1
    max_fringe_size=1

    while fringe:
	time_start=timeit.default_timer()
        state=copy.deepcopy(fringe[-1])
        fringe.pop(-1)

        time_copy_acc=0
        time_move_acc=0
        time_explore_acc=0
        time_explore_set_acc=0
        time_fringe_acc=0
        time_final_acc=0

	time_init_stop=timeit.default_timer()

        for i in xrange(0,state.size):
            if state.all_tiles[i]==0:
                for el in xrange(len(state.neighbours[i])-1,-1,-1):
                #for el in xrange(0,len(state.neighbours[i])):
                    time=timeit.default_timer()
                    new_state=copy.deepcopy(state)
                    time_copy=timeit.default_timer()
                    new_state.switch_tile_vals(i, state.neighbours[i][el])
                    is_new=True
                    time_move=timeit.default_timer()
                    if new_state in explored_set:
                        is_new=False
                    time_explore=timeit.default_timer()
                    if new_state in fringe:
                        is_new=False
                    time_fringe=timeit.default_timer()
                    if is_new:
                        fringe.append(new_state)
                        new_state.pos_in_explored=len(explored_set)
                        nodes_exp=nodes_exp+1
                        if max_fringe_size<len(fringe):
                            max_fringe_size=len(fringe)
		    time_final=timeit.default_timer()

                        # would include exploring of child nodes instantaneous
                        #if new_state==goal_board:
                        #    print("max_fringe_size:", max_fringe_size)
                        #    print("nodes_expanded:", nodes_exp)
                        #    return parents_list(board, new_state, explored)
                    time_copy_acc+=time_copy-time
                    time_move_acc+=time_move-time_copy
                    time_explore_acc+=time_explore-time_move
                    time_fringe_acc+=time_fringe-time_explore
                    time_final_acc+=time_final-time_fringe
        #print("time for init: ",time_init_stop-time_start)
        #print("time for copy: ",time_copy_acc)
        #print("time for move: ",time_move_acc)
        #print("time for explore: ",time_explore_acc)
        #print("time for fringe: ",time_fringe_acc)
        #print("time for is_new: ",time_final_acc)
	
	explored_set.add(state)

	time_end=timeit.default_timer()
        #print("time for explore one state: ",time_end-time_start)
        #print("max_fringe_size:", max_fringe_size)
        #print("explored size:", len(explored))
        print("nodes_expanded:", nodes_exp)
	ne=str(nodes_exp)+" "+str(time_end-time_start)+"\n"
	s=str(ne)
	f.write(s)
        #print("\n")
        if fringe[-1].all_tiles==goal_board.all_tiles:
	    explored_set.add(fringe[-1])
	    explored_list=list(explored_set)
            return parents_list(board, fringe[-1], explored_list)

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
for x in init_dist:
    board.all_tiles.append(x)

#get neighbours for creating the next states for the search space
get_neighbours(board)

#initialze goal state
goal_board=Board(len(init_dist))
for x in range(0,len(init_dist)):
    goal_board.all_tiles.append(x)


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
