from config import *
from player import Player
import pickle
from help import error

mainPath = "rsc/playerData/"

def getPlayer(name:str) -> Player|None:
    try:
        p= pickle.load(open(f"{mainPath}{name}", 'rb'))
        return p
    except:
        error("\nno player(file)")

def savePlayer(player) -> None:
    filePath = f"{mainPath}{player.getName()}"
    try:
        pickle.dump(player, open(filePath, 'wb'))
    except:
        open(filePath, 'x')
        savePlayer(player)

def getSaveNames() -> list[str]:
    names= []
    files = listdir(mainPath)
    for f in files:
        names.append(f)
    return names

def getData(file:str) -> str:
    if not path.isfile(file):
        error(f"No file named : {file} (file.getDate())")
    data = ''
    with open(str(file), 'r') as f:
        data = f.read()
    return data