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



class PlayerAI(BaseAI):
    def __init__(self):
        self.turn=0
    def getMove(self, grid):
        time=timeit.default_timer()
        time_calc=timeit.default_timer()
        fringe=[]
        fringe.append(grid)
	alpha=-infinity
	beta=+infinity
	depth=8
	
        while time_calc-time<0.09:
            max_list=[]
            fringe_new=[]
            moves_done=[]

            #explore the whole fringe and move the tiles (Players Turn)
            for el in xrange(0,len(fringe)):
	      max(fringe[el], depth, alpha, beta)

            #explore the whole finge and spawn a new tile (Computers Turn)
            for el in xrange(0,len(fringe)):
	      min(fringe[el], depth, alpha, beta)

            index_max=max_list.index(max(max_list))
            fringe.append(fringe_new[index_max])

            return moves_done[index_max]
        time_calc=timeit.default_timer()

#            min_list=[]
#            fringe_new=[]
#            
#            #explore the whole finge and spawn a new tile (Computers Turn)
#            for el in xrange(0,len(fringe)):
#                grid_old=copy.deepcopy(fringe[el])
#                cells = grid_old.getAvailableCells()
#                for cell in cells:
#                    grid_exp=copy.deepcopy(fringe[el])
#                    grid_exp.insertTile(cell, 2)
#                    min_list.append(heur_order(grid_exp))
#                    fringe_new.append(grid_exp)
#                fringe.pop(0)
#
#            index_max=numpy.argmax(max_list)
#            fringe.append(fringe_new[index_max])
        return self.turn

#int max(int tiefe,
#int alpha, int beta) {
#if (tiefe == 0 or keineZuegeMehr(spieler_max))
#return bewerten();
#int maxWert = alpha;
#generiereMoeglicheZuege(spieler_max);
#while (noch Zug da) {
#fuehreNaechstenZugAus();
#int wert = min(tiefe-1, 
#maxWert, beta);
#macheZugRueckgaengig();
#if (wert > maxWert) {
# maxWert = wert;
#if (maxWert >= beta)
#break;
#if (tiefe == anfangstiefe)
#       gespeicherterZug = Zug;
#	      }
#}
#return maxWert;
#}

def max(grid, depth, alpha, beta):
  if(depth==0):
    return move
  maxVal=alpha

  moves=grid.getAvailableMoves()
  for move in moves:
      grid_exp=copy.deepcopy(grid)
      grid_exp.move(move)
      beta=heur_order(grid_exp)
      #max_list.append(heur_order(grid_exp))
      #moves_done.append(move)
      #fringe_new.append(grid_exp)
      val=min(depth-1,maxVal,beta)
      if(val>maxVal):
	maxVal=val
	if(maxVal>beta):
	  break
	if(depth==start_depth):
	  saved_move=move
  return maxVal


def min(grid, depth, alpha, beta):
  if(depth==0):
    return move
  minVal=beta

  moves=grid.getAvailableMoves()
  for move in moves:
      grid_exp=copy.deepcopy(grid)
      grid_exp.move(move)
      beta=heur_order(grid_exp)
      #max_list.append(heur_order(grid_exp))
      #moves_done.append(move)
      #fringe_new.append(grid_exp)
      val=min(depth-1,alpha,minVal)
      if(val<minVal):
	minVal=val
	if(minVal<alpha):
	  break
	if(depth==start_depth):
	  saved_move=move
  return minVal
