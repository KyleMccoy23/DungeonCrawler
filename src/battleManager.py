from config import *

class battleManager:
    
    def startBattle(self, player, enemy) -> None:
        self.player = player
        self.enemy = enemy

        self.battling = True

        system('cls')

        self.player.changeWeapons("Iron Sword")

        self.battle()

    def battle(self):

        while self.battling:

            self.enemy.bars[0].draw()
            print("-"*20)
            for bar in self.player.bars:
                bar.draw()
            self.checkHealth()

            if not self.battling:
                break

            self.attacks(self.player, self.enemy)

            input("> ")

            system('cls')

    def attacks(self, character, enemy):
        character.attack(enemy)

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