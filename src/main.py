from config import *
from player import *
from playerManager import *


class Game:
    def __init__(self) -> None:
        
        self.pManager = playerManager()
        self.player = Player()

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

        
    def newGame(self) -> None:
        self.player = self.pManager.makePlayer(self.player)
        system('cls')
        print(self.player)

    def loadGame(self) -> None:
        raise NotImplementedError()


def main() -> None:
    system('cls')
    g = Game()


if __name__ == "__main__":
    main()