from item import Item
from items import fists
from config import *

class Player:
    def __init__(self) -> None:
        self.health = 0
        self.healthMax = 0
        self.mana = 0
        self.manaMax = 0
        self.stamina = 0
        self.staminaMax = 0

        self.statPoints = 30

        self.level = 1
        self.exp = 0

        self.status = ""

        self.defaultWeapon = fists

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

        self.inventory: list[list] = [
            [fists, 1]
        ]

        self.inHand = self.defaultWeapon

        self.healthBar = None
        self.manaBar = None
        self.staminaBar = None

        self.bars = []
        
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
        self.healthMax = self.health
        self.manaMax = self.mana
        self.staminaMax = self.stamina

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

    def setBars(self, hbar, mBar, sBar) -> None:
        self.healthBar = hbar
        self.manaBar = mBar
        self.staminaBar = sBar

        self.bars = [self.healthBar, self.manaBar, self.staminaBar]

    def attack(self, target):
        target.health -= self.inHand.damage # type: ignore
        target.health = max(target.health, 0)
        target.healthBar.update()

        print(f'{self.identity.get('name')} attacked with {self.inHand.name}')
    
    def useSkill(self, skill) -> None:
        raise NotImplementedError("SKills are not a thing yet")
    
    def hasItem(self, item: str) -> bool:
        for i in self.inventory:
            if i[0].name == item:
                return True
        return False
    
    def getItem(self, item: str):
        for i in self.inventory:
            if i[0].name == item:
                return i[0]

    def changeWeapons(self, item: str) -> None:
        if not self.hasItem(item):
            return None
        itemObj: Item = self.getItem(item) # type: ignore
        if not itemObj.type == "weapon":
            input('not weapon')
            return None
        self.inHand = itemObj

    def unequip(self) -> None:
        self.inHand = self.defaultWeapon
