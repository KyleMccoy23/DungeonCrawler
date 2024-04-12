from config import *

class battleManager:
    
    def startBattle(self, player, enemy) -> None:
        self.player = player
        self.enemy = enemy

        self.battling = True

        system('cls')

        self.battle()

    def battle(self):

        while self.battling:

            self.enemy.attack(self.player)

            for bar in self.enemy.bars:
                bar.draw()

            print("-"*20)

            for bar in self.player.bars:
                bar.draw()

            self.checkHealth()

            input()

            system('cls')

    def checkHealth(self):
        if self.enemy.health == 0 and self.player.health == 0:
            self.battling = False
            print(f"THIS BATTLE IS A DRAW")

        elif self.enemy.health == 0:
            self.battling = False
            print(f"THIS BATTLE IS WON BY THE PLAYER")

        elif self.player.health == 0:
            self.battling = False
            print(f"THIS BATTLE IS WON BY THE ENEMY")