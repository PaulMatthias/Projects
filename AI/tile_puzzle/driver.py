#!/usr/bin/python3
import math
import argparse
import copy


class Board:
    'Holds all tiles of the puzzle'
    
    def __init__(self, size):
        self.size=size
        self.all_tiles=[]


    def switch_tile_vals(self, element_one, element_two):
        tmp=self.all_tiles[element_one].value
        print("switch tile ",element_one," with value ",self.all_tiles[element_one].value," with the tile ",element_two, " with value ",self.all_tiles[element_two].value)
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


def Breadth_First_Search(board, goal_board):
    print("Beginning BFS")
    fringe=[]
    explored=[]
    fringe.append(board)
    
    counter=0
    while fringe:
        state=fringe[0]
        explored.append(state)
        print("Elements in the fringe: ", len(fringe))

        if state==goal_board:
            return state

        for i in range(0,state.size):
            print("checking tile on the board for moving tile 0 at pos ",i)
            if state.all_tiles[i].value==0:
                print("found tile 0")
                for el in range(0,len(state.all_tiles[i].next)):
                    print("create new states for the ",len(state.all_tiles[i].next), " neighbours, currently ",el)
                    new_state=copy.deepcopy(state)
                    new_state.switch_tile_vals(i, state.all_tiles[i].next[el])
                    if new_state not in explored:
                        print("add new state to the fringe")
                        fringe.append(new_state)
        counter=counter+1
        #if counter==5:
        #    break
            

    
        

    return FAILURE









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

Breadth_First_Search(board, goal_board)















