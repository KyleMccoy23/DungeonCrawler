from config import *

class Battle:
    
    def startBattle(self, player, enemy):
        self.player = player
        self.enemy = enemy

        self.a()

    def a(self):
        print(self.enemy)
        print(self.player)