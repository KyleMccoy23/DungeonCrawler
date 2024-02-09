from config import *
from player import *
from playerManager import *
from file import *


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

        savePlayer(self.player)

    def loadGame(self):

        save = input(getSaveNames()+"Enter File Name:")

        try:
            self.player = getPlayer(save)
            system('cls')
            print(self.player)
        except:
            print("no player(main)")



system('cls')
g = Game()
