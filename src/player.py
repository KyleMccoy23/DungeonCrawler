from config import *

class Player:
    def __init__(self) -> None:
        self.health = None
        self.mana = None
        self.stamina = None

        self.statPoints = 30

        self.level = 1
        self.exp = 0

        self.status = ""

        self.stats: dict[str, int] = {
            'Str':0,
            'Dex':0,
            'Con':0,
            'Int':0,
            'Wis':0,
            'Cha':0
        }
        
        self.skills = [

        ]

        self.attribute = None

        self.identity: dict[str,str] = {
            'race':"",
            'class':"",
            'name':"",
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

    def getStats(self, stat: str) -> int:
        return self.stats[stat]
    
    def applyBonus_stat(self, stat: str, bonus: int) -> None:
        self.stats[stat] += bonus

    def applyBonus_skill(self, skillName: str, skillDesc: str, damage:str) -> None: # type: ignore
        s = [skillName, skillDesc, damage]
        self.skills.append(s)
    
    def applyBonus_skill(self, skill: list[str]) -> None: # type: ignore
        self.skills.append(skill)

    def applyBonus_skill(self, *args: None) -> None:
        try:    
            error("Skill Not Found (file.getData -> help.GetSkill -> playerManager.bonuses -> player.applyBonus_skill)")
        except:
            print("Skill Not Found")

    def setStatPoints(self, sp: int) -> None:
        self.statPoints = sp

    def getName(self) -> str|None:
        return self.identity['name']
    
    def addSkill(self, skill) -> None:
        self.skills.append(skill)