from config import *
from player import *
from playerManager import *


class Game:
    def __init__(self):
        
        self.pManager = playerManager()
        self.player = Player()

        # 

        self.run()

        
    def run(self):
        self.player = self.pManager.makePlayer(self.player)
        system('cls')
        print(self.player)
        

system('cls')
g = Game()
