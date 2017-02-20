from BaseAI import BaseAI
import timeit
import copy

def heur_order(grid):
    val=0
    tmp=0
    for i in xrange(0,grid.size):
        for j in xrange(0,grid.size-1):
            if grid.map[i][j+1]:
                tmp=grid.map[i][j+1]-grid.map[i][j]
            else:
                tmp=-grid.map[i][j]
            if grid.map[j+1][i]:
                tmp+=grid.map[j+1][i]-grid.map[j][i]
            else:
                tmp=-grid.map[i][j]


            val+=tmp
    return val

def heur_smooth(grid):
    val=0
    tmp=0
    for i in xrange(0,grid.size):
        for j in xrange(0,grid.size-1):
            if grid.map[i][j+1]>grid.map[i][j]:
                tmp+=1
            if grid.map[j+1][i]>grid.map[j][i]:
                tmp+=1
            val+=tmp
    return val

def calc_heur(grid):
    fac_order=0.7
    fac_smooth=0.2
    val=fac_order*heur_order(grid)
    val+=fac_smooth*heur_smooth(grid)
    return val

global start_depth
start_depth=2

class PlayerAI(BaseAI):
    def __init__(self):
        self.turn=0

    def getMove(self, grid):
        time=timeit.default_timer()
	alpha=-float("inf")
	beta=float("inf")
	saved_move=0
	time_calc=timeit.default_timer()
	depth=4
	
        #while time_calc-time<0.09:
	#  depth+=1
	[value_of_grid, saved_move]=max(grid, start_depth, alpha, beta, saved_move)
	time_calc=timeit.default_timer()
	
        return saved_move

def max(grid, depth, alpha, beta, saved_move):
  if(depth==0):
    return [calc_heur(grid), saved_move]

  maxVal=alpha

  moves=grid.getAvailableMoves()
  for move in moves:
      grid.move(move)
      li=min(grid, depth-1,maxVal,beta, saved_move)
      val=li[0]
      saved_move=li[1]
      if move%2==0:
	grid.move(move+1)
      else:
	grid.move(move-1)
      #print("Max", depth, val, maxVal, alpha, beta, saved_move)
      if(val>maxVal):
	maxVal=val
	if(maxVal>beta):
	  break
	if(depth==start_depth):
	  saved_move=move
  return [maxVal, saved_move]


def min(grid, depth, alpha, beta, saved_move):
  if(depth==0):
    return [calc_heur(grid),saved_move]

  minVal=beta

  cells=grid.getAvailableCells()
  for cell in cells:
      #ignore 4 spawns for now
      grid.setCellValue(cell, 2)
      #[val, saved_move]=max(grid, depth-1, alpha, minVal, saved_move)
      val=max(grid, depth-1, alpha, minVal, saved_move)
      grid.setCellValue(cell, 0)
      #print("Min", depth, val, minVal, alpha, beta, saved_move)
      if(val<minVal):
	minVal=val
	if(minVal<alpha):
	  break
  return [minVal, saved_move]

