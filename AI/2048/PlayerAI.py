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
    fac_order=0.5
    fac_smooth=0.5
    val=fac_order*heur_order(grid)
    val+=fac_smooth*heur_smooth(grid)
    return val


class PlayerAI(BaseAI):
    def __init__(self):
        self.turn=0

    def getMove(self, grid):
        time=timeit.default_timer()
	alpha=-float("inf")
	beta=float("inf")
	depth=1
	saved_move=0
	time_calc=timeit.default_timer()
	
        #while time_calc-time<0.09:
	#depth+=1
	[value_of_grid, saved_move]=max(grid, depth, alpha, beta, saved_move)
	print("Saved move return ", saved_move)
	time_calc=timeit.default_timer()
	
	print("Searched Depth ", depth, "alpha ", alpha, "beta ", beta)

        return saved_move

def max(grid, depth, alpha, beta, saved_move):
  if(depth==0):
    return calc_heur(grid)
  start_depth=depth

  maxVal=alpha

  moves=grid.getAvailableMoves()
  for move in moves:
      grid.move(move)
      #[val, saved_move]=min(grid, depth-1,maxVal,beta, saved_move)
      val=min(grid, depth-1,maxVal,beta, saved_move)
      if move%2==0:
	grid.move(move+1)
      else:
	grid.move(move-1)
      #print("Max", depth, val, maxVal, alpha, beta)
      if(val>maxVal):
	maxVal=val
	if(maxVal>beta):
	  break
	if(depth==start_depth):
	  saved_move=move
	  print("Saved move ", saved_move)
  #return [maxVal, saved_move_max]
  return [maxVal, saved_move]


def min(grid, depth, alpha, beta, saved_move):
  if(depth==0):
    return calc_heur(grid)
  start_depth=depth

  minVal=beta

  cells=grid.getAvailableCells()
  for cell in cells:
      #ignore 4 spawns for now
      grid.setCellValue(cell, 2)
      #[val, saved_move]=max(grid, depth-1, alpha, minVal, saved_move)
      val=max(grid, depth-1, alpha, minVal, saved_move)
      grid.setCellValue(cell, 0)
      #print("Min", depth, val, minVal, alpha, beta)
      if(val<minVal):
	minVal=val
	if(minVal<alpha):
	  break
  return [minVal, saved_move]



#def Depth_First_Search(grid, goal_board):
#    fringe=[]
#    explored=[]
#    fringe.append(grid)
#    
#    grid.pos_in_explored=0
#
#    max_search_depth=10
#
#    while fringe:
#	time_start=timeit.default_timer()
#        state=fringe[-1].clone()
#        fringe.pop(-1)
#	explored.append(state)
#	max_search_depth-=1
#
##Players turn
#	moves=state.getAvailableMoves()
#	for el in xrange(len(moves)-1,-1,-1):
#	    new_state=copy.clone()
#	    new_state.move(moves[el])
#	    fringe.append(new_state)
#	    new_state.pos_in_explored=len(explored)
#	    nodes_exp=nodes_exp+1
#	
#
#        state=fringe[-1].clone()
#        fringe.pop(-1)
#	explored.append(state)
#	max_search_depth-=1
#
##Computers turn
#	new_state=copy.deepcopy(state)
#	cells = new_state.getAvailableCells()
#	for cell in cells:
#	    cpu_new_state=copy.clone()
#	    cpu_new_state.insertTile(cell, 2)
#	    fringe.append(cpu_new_state)
#	    cpu_new_state.setCellValue(cell, 4)
#	    fringe.append(cpu_new_state)
#	
#	if max_search_depth<=0:
#	 
#
#	time_end=timeit.default_timer()
#        #print("time for explore one state: ",time_end-time_start)
#        #print("max_fringe_size:", max_fringe_size)
#        #print("explored size:", len(explored))
#        print("nodes_expanded:", nodes_exp)
#
#    return 
