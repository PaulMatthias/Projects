from BaseAI import BaseAI

class PlayerAI(BaseAI):
    def __init__(self):
        self.turn=0
    def getMove(self, grid):
        self.turn+=1
        return self.turn%4
