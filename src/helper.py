from datetime import date
from time import ctime, sleep
from file import getData
mainPath = "../rsc/playerData/"

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
    msg = str(ctime())+': '+msg+'\n'
    try:
        f = open(p, 'a')
        f.write(msg)
        f.close()
    
    except:
        f = open(p, 'x')
        logError(msg)

def getSkill(statNum):
    data = getData(f'{mainPath}/{statNum}.txt')
    print(data)
    sleep(2)
    return data.split(',')