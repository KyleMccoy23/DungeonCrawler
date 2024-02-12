from config import *

class Player:
    def __init__(self):
        self.health = None
        self.mana = None
        self.stamina = None

        self.statPoints = 30

        self.level = 1
        self.exp = 0

        self.status = ""

        self.stats = {
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

        self.identity = {
            'race':None,
            'class':None,
            'name':"",
        }

        self.inventory = [
            
        ]

    def __str__(self):
        info = f'Health: {self.health}\nMana: {self.mana}\nStamina: {self.stamina}\n\nLevel: {self.level}\nClass: '+self.identity['class']+'\nRace: '+self.identity['race']+'\nSkills\n'
        for s in self.skills:
            info += f'{str(s)}\n'
        info += '\n'
        for stat in self.stats:
            info += f'{stat}: {self.stats[stat]}\n'
        return info
    
    def setIdentity(self, id, info):
        self.identity[id] = info

    def setAttributes(self, att):
        self.health, self.mana, self.stamina = att

    def setStats(self, stat, points):
        self.stats[stat] = points

    def getStats(self, stat):
        return self.stats[stat]
    
    def applyBonus_stat(self, stat, bonus):
        self.stats[stat] += bonus

    def applyBonus_skill(self, skillName, skillDesc):
        s = [skillName, skillDesc]
        self.skills.append(s)

    def setStatPoints(self, sp):
        self.statPoints = sp
    
    def getName(self):
        return self.identity['name']