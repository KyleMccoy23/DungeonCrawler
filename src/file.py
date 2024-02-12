from config import *
import pickle
mainPath = "../rsc/playerData/"


def getPlayer(name):
    try:
        p= pickle.load(open(f"{mainPath}{name}", 'rb'))
        return p
    except Exception as e:
        error(str(str(e)+"\nno player(file)"))

def savePlayer(player):
    filePath = f"{mainPath}{player.getName()}"
    try:
        pickle.dump(player, open(filePath, 'wb'))
    except:
        open(filePath, 'x')
        savePlayer(player)

def getSaveNames():
    names= []
    files = listdir(mainPath)
    for f in files:
        names.append(f)
    return names

def getData(file):
    data = ''
    with open(file, 'r') as f:
        data = f.read()
    return data