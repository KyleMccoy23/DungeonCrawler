from config import *
from player import Player
from playerManager import playerManager
from battleManager import battleManager
from file import *


class Game:
    def __init__(self) -> None:
        
        self.pManager = playerManager()
        self.player = Player()

        self.battleManager = battleManager()

        self.run()

        
    def run(self) -> None:
        new:str = input('Do you what to start a new game (y/n): ')

        system('cls')

        match(new.lower()):
            case 'y':
                self.newGame()
            case 'n':
                self.loadGame()
            case _:
                try:error("Invalid input (Game.run 'Start')")
                except:self.run()

        # self.battleManager.startBattle(self.player, self.player)
        
    def newGame(self) -> None:
        self.player = self.pManager.makePlayer(self.player)
        system('cls')
        print(self.player)
        savePlayer(self.player)

    def loadGame(self):
        saves = getSaveNames()

        for n,s in enumerate(saves):
            print(f'{n+1}) {s}')

        save = input("Enter File Name: ")

        if save.isnumeric():
            save = saves[(int(save)-1)]

        try:
            self.player = getPlayer(save)
            system('cls')
            print(self.player)
        except:
            logError("no player(main)")
            print("No player of that name")
            sleep(2)
            self.run()



def main() -> None:
    system('cls')
    g = Game()


if __name__ == "__main__":
    main()
