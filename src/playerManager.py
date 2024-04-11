from config import *
from player import Player
from help import getSkill

class playerManager:

    def makePlayer(self, player: Player) -> object:
        self.player = player
        self.maxStats = 30

        self.player.setIdentity('race', self.playerRace())
        self.player.setIdentity('class', self.playerClass())
        self.player.setIdentity('name', self.playerName())
        

        self.playerStats()

        self.player.setAttributes(self.playerPhysicalAttributes())

        self.bonuses()


        self.player.setStatPoints(self.maxStats)

        return self.player

    def playerPhysicalAttributes(self) -> tuple:
        return self.makePlayerHealth(), self.makePlayerMana(), self.makePlayerStamina()
    
    def playerStats(self) -> None:
        for s in self.player.stats:
            print("How many point do you want to put into your stats (Max is 10)")
            print(f"Remaining Stat Points: {self.maxStats}")
            for ss in self.player.stats:
                if self.player.stats[ss] is not None:
                    print(f'{ss} : {self.player.getStats(ss)}')
            statPoints = input(f"{s}: ")
            if statPoints == '': statPoints = 1
            elif statPoints == 'q': exit(0)
            else: statPoints = int(statPoints)
            self.setStats(s, statPoints)
            system('cls')

    def setStats(self, stat, points) -> None:
        if points > 10: 
            points = 10
            self.maxStats-=points
            self.player.setStats(stat, points)
        elif points > self.maxStats:
            self.maxStats-=self.maxStats
            self.player.setStats(stat, points)
        else:
            self.maxStats-=points
            self.player.setStats(stat, points)

    def makePlayerHealth(self) -> int:
        return 10 + self.player.getStats('Con') * self.player.level

    def makePlayerMana(self) -> int:
        return 5 + self.player.getStats('Int') * self.player.level
    
    def makePlayerStamina(self) -> int:
        return 10 + (self.player.getStats('Con')*self.player.level) * self.player.level
    
    def playerClass(self) -> str:
        while True:
            for n, c in enumerate(classes):
                print(n+1, c)
            selectedClass = input('Enter your class(number): ')
            if selectedClass != '':
                selectedClass = int(selectedClass)
                break
            system('cls')
        system('cls')
        return classes[selectedClass-1]

    def playerRace(self) -> str:
        while True:
            for n, r in enumerate(races):
                print(n+1, r)
            selectedRace = input('Enter your race(number): ')
            if selectedRace != '':
                selectedRace = int(selectedRace)
                break
            system('cls')
        system('cls')
        return races[selectedRace-1]
    
    def playerName(self):
        name = input("Enter your players name: ")
        system('cls')
        return str(name)

    def bonuses(self) -> None:
        self.player.applyBonus_stat('Con', 10)
        self.player.applyBonus_skill(getSkill('000'))

