from datetime import date
from config import mainPath
from file import getData

def statHelp():
    with open('rsc\player-stat.txt', 'r') as statHelp:
        for l in statHelp.readlines():
            print(l)

def creationHelp():
    statHelp()
    print('\nEnter \'q\' to quit')

def error(msg="Error!!!"):
    logError(msg)
    raise Exception(msg)

def logError(msg):
    t = str(date.today())
    p = '../rsc/logs/'+t+'.txt'
    try:
        f = open(p, 'w')
        f.write(msg)
        f.close()
    
    except:
        f = open(p, 'x')
        logError(msg)

def getSkill(statNum):
    data = getData(f'{mainPath}/{statNum}.txt')
    return data.split(',')