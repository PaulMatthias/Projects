#!/usr/bin/python3
import math
import argparse
import copy


class Board:
    'Holds all tiles of the puzzle'
    
    def __init__(self, size):
        self.size=size
        self.all_tiles=[]

    def __eq__(self,other):
        for i in range(0,self.size):
            if self.all_tiles[i].value!=other.all_tiles[i].value:
                return False
        return True


    def switch_tile_vals(self, element_one, element_two):
        tmp=self.all_tiles[element_one].value
       # print("switch tile ",element_one," with value ",self.all_tiles[element_one].value," with the tile ",element_two, " with value ",self.all_tiles[element_two].value)
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

#---------------------------------------------------------------------------------------
# BREADTH FIRST SEARCH
#---------------------------------------------------------------------------------------

def Breadth_First_Search(board, goal_board):
    print("Beginning BFS")
    fringe=[]
    explored=[]
    fringe.append(board)
    
    counter=0
    while fringe:
        state=copy.deepcopy(fringe[0])
        explored.append(state)
        #print("Elements in the fringe: ", len(fringe))

        if state==goal_board:
            print("explore ",counter," states to solve the tile puzzle")
            return state

        for i in range(0,state.size):
        #    print("checking tile on the board for moving tile 0 at pos ",i)
            if state.all_tiles[i].value==0:
         #       print("found tile 0")
                for el in range(0,len(state.all_tiles[i].next)):
          #          print("create new states for the ",len(state.all_tiles[i].next), " neighbours, currently ",el)
                    new_state=copy.deepcopy(state)
                    new_state.switch_tile_vals(i, state.all_tiles[i].next[el])
                    is_new=True
                    for ex in range(0,len(explored)):
                        if new_state==explored[ex]:
           #                 print("new state already explored")
                            is_new=False
                    for fr in range(0,len(fringe)):
                        if new_state==fringe[fr]:
            #                print("new state already in the fringe")
                            is_new=False
                    if is_new:
             #           print("add new state to the fringe")
                        fringe.append(new_state)

        counter=counter+1
        #delete first element in the fringe and order the rest accoridngly
        fringe.pop(0)

        #for z in range(0,3):
        #    print(fringe[0].all_tiles[z*3].value, fringe[0].all_tiles[z*3+1].value,fringe[0].all_tiles[z*3+2].value)
        #print("\n")


    return 

#---------------------------------------------------------------------------------------
# DEPTH FIRST SEARCH
#---------------------------------------------------------------------------------------

def Depth_First_Search(board, goal_board):
    print("\n\n")
    print("Beginning DFS")
    fringe=[]
    explored=[]
    fringe.append(board)
    
    counter=0
    while fringe:
        state=copy.deepcopy(fringe[-1])
        fringe.pop(-1)
        explored.append(state)
        #print("Elements in the fringe: ", len(fringe))

        if state==goal_board:
         #   print("used ",counter," moves to solve the tile puzzle")
            return state

        for i in range(0,state.size):
            #print("checking tile on the board for moving tile 0 at pos ",i)
            if state.all_tiles[i].value==0:
             #   print("found tile 0")
                for el in range(len(state.all_tiles[i].next)-1,-1,-1):
              #      print("create new states for the ",len(state.all_tiles[i].next), " neighbours, currently ",el)
                    new_state=copy.deepcopy(state)
                    new_state.switch_tile_vals(i, state.all_tiles[i].next[el])
                    is_new=True
                    for ex in range(0,len(explored)):
                        if new_state==explored[ex]:
                 #           print("new state already explored")
                            is_new=False
                    for fr in range(0,len(fringe)):
                        if new_state==fringe[fr]:
                #            print("new state already in the fringe")
                            is_new=False
                    if is_new:
               #         print("add new state to the fringe")
                        fringe.append(new_state)

        counter=counter+1
        print(counter)
        #if counter>50:
        #    break
        #delete first element in the fringe and order the rest accoridngly

        #for z in range(0,3):
        #    print(fringe[-1].all_tiles[z*3].value, fringe[-1].all_tiles[z*3+1].value,fringe[-1].all_tiles[z*3+2].value)
        #print("\n")


    return 

#------------------------------------------------------------------------------------
#Beginning MAIN program
#------------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("algorithm", action="store")
parser.add_argument("tiles", action="store")
args=parser.parse_args()
print(args.algorithm)
print(args.tiles)

init_dist=[int(x) for x in args.tiles.split(',')]

board=Board(len(init_dist))
for x in range(0,len(init_dist)):
    tile=Tile(x, init_dist[x])
    board.all_tiles.append(tile)

#for i in range (0, board.size):
#    print("pos: ", board.all_tiles[i].pos)
#    print("val: ", board.all_tiles[i].value)

get_neighbours(board)

#for el in board.all_tiles[0].next:
#    print("pos :", board.all_tiles[0].pos, "neighbours: ", el)

#initialze goal board
goal_board=Board(len(init_dist))
for x in range(0,len(init_dist)):
    tile=Tile(x, x)
    goal_board.all_tiles.append(tile)

#for i in range (0, goal_board.size):
#    print("pos: ", goal_board.all_tiles[i].pos)
#    print("val: ", goal_board.all_tiles[i].value, "\n")
#

if args.algorithm=="bfs":
    final_state=Breadth_First_Search(board, goal_board)
elif args.algorithm=="dfs":
    final_state=Depth_First_Search(board, goal_board)





print("Final State:")
for i in range(0,final_state.size):
    print(final_state.all_tiles[i].value)
print("\n")


