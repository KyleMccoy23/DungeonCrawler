from os import system, listdir
from sys import exit
from help import *

try:
    system('python.exe -m pip install --upgrade pip')
    system('pip install -r assets/dependencies.txt')
except Exception as e:
    print(e)
    exit(0)

import pickle

classes = [
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

races = [
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