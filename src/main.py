from config import *
from player import *
from playerManager import *


class Game:
    def __init__(self):
        
        self.pManager = playerManager()
        self.player = Player()

        self.run()

        
    def run(self):
        new = input('Do you what to start a new game (y/n): ')

        system('cls')

        match(new):
            case 'y':
                self.newGame()
            case 'n':
                self.loadGame()
            case _:
                try:
                    error("Invalid input")
                except:
                    pass

        
    def newGame(self):
        self.player = self.pManager.makePlayer(self.player)
        system('cls')
        print(self.player)

    def loadGame(self):
        pass

system('cls')
g = Game()
