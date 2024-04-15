from os import system, listdir, path
from sys import exit
from help import error
from time import sleep

mainPath = "../rsc/playerData/"

try:
    system('python.exe -m pip install --upgrade pip')
    system('pip install -r ../rsc/dependencies.txt')
except Exception as e:
    error(str(e))

classes: list[str] = [
    "Fighter", 
    "Rogue", 
    "Wizard", 
    "Cleric", 
    "Ranger", 
    "Bard", 
    "Paladin", 
    "Barbarian", 
    "Monk", 
    "Sorcerer", 
    "Warlock", 
    "Druid"
]

races: list[str] = [
    "Human", 
    "Elf",
    "Dwarf", 
    "Halfling", 
    "Gnome", 
    "Half-Elf", 
    "Half-Orc", 
    "Tiefling", 
    "Dragonborn", 
    "Aasimar"
]