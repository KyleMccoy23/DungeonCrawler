from os import system, listdir
# from sys import exit
from helper import *
from time import sleep

try:
    system('python.exe -m pip install --upgrade pip')
    system('pip install -r ../rsc/dependencies.txt')
except Exception as e:
    error(e)

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

mainPath = "../rsc/playerData/"