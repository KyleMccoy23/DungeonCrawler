from config import *
from playerManager import playerManager
from battleManager import battleManager
from file import *
from help import help


class Game:
    def __init__(self) -> None:
        
        self.pManager = playerManager()
        self.player = Player()
        self.enemy = Player()

        self.enemy = getPlayer("test")

        self.battleManager = battleManager()

        self.menu = True

        self.run()

        
    def run(self) -> None:
        while self.menu:
            print(f"1. Start New Game\n"
                f"2. Load Game\n"
                f"3. Help\n"
                f"4. Quit")

            new:str = input("# ")

            system('cls')

            if new == '': self.run()

            match(new):
                case '1':
                    self.menu = False
                    self.newGame()
                case '2':
                    self.menu = False
                    self.loadGame()
                case '3':
                    help()
                    self.run()
                case '4':
                    self.menu = False
                    quit(0)
                case _:
                    print(new)
                    input("HELP ME PLZ GONNA KMS")
                    try:error("Invalid input (Game.run 'Start')")
                    except:self.run()

        # self.pManager.giveitem([stick, iron, iron], player=self.player)
        self.battleManager.startBattle(self.player, self.enemy)
        
    def newGame(self) -> None:
        self.player = self.pManager.makePlayer(self.player)
        system('cls')
        print(self.player)
        savePlayer(self.player)

    def loadGame(self) -> None:
        saves = getSaveNames()

        for n,s in enumerate(saves):
            print(f'{n+1}) {s}')

        save:str = input("Enter File Name: ")

        if save.isnumeric():
            save = saves[(int(save)-1)]

        try:
            self.player = getPlayer(save)
            system('cls')
            print(self.player)
        except Exception as e:
            error("no player(main)")
            print("No player of that name:", e)
            sleep(2)
            self.run()

def main() -> None:
    system('cls')
    g = Game()

if __name__ == "__main__":
    main()
