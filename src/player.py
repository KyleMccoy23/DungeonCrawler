from config import *

class Player:
    def __init__(self) -> None:
        self.health = None
        self.mana = None
        self.stamina = None

        self.statPoints = 30

        self.level = 1

        self.stats: dict[str, None|int] = {
            'Str':None,
            'Dex':None,
            'Con':None,
            'Int':None,
            'Wis':None,
            'Cha':None
        }
        
        self.skills = [

        ]

        self.attribute = None

        self.identity: dict[str:str|None] = {
            'race':None,
            'class':None,
        }

        self.inventory = [
            
        ]

    def __str__(self) -> str:
        info = f'Health: {self.health}\nMana: {self.mana}\nStamina: {self.stamina}\n\nLevel: {self.level}\nClass: '+self.identity['class']+'\nRace: '+self.identity['race']+'\nSkills\n'
        for s in self.skills:
            info += f'{str(s)}\n'
        info += '\n'
        for stat in self.stats:
            info += f'{stat}: {self.stats[stat]}\n'
        return info
    
    def setIdentity(self, id: str, info:str) -> None:
        self.identity[id] = info

    def setAttributes(self, att:tuple) -> None:
        self.health, self.mana, self.stamina = att

    def setStats(self, stat:str, points: int) -> None:
        self.stats[stat] = points

    def getStats(self, stat: str) -> None | int:
        return self.stats[stat]
    
    def applyBonus_stat(self, stat: str, bonus: int) -> None:
        self.stats[stat] += bonus

    def applyBonus_skill(self, skillName: str, skillDesc: str) -> None:
        s = [skillName, skillDesc]
        self.skills.append(s)

    def setStatPoints(self, sp: int) -> None:
        self.statPoints = sp

