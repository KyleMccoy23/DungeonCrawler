from config import *
from weapons import ironSword

class battleManager:
    
    def startBattle(self, player, enemy) -> None:
        self.player = player
        self.enemy = enemy

        self.player.inventory.append((ironSword, 1))

        self.battling = True

        system('cls')
        print(self.player.inventory[0][0].name)

        self.player.changeWeapons("Iron Sword")

        self.battle()

    def battle(self):

        while self.battling:

            self.player.attack(self.enemy)

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