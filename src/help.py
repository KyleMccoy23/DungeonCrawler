import datetime
mainPath = "../rsc/playerData/"


def statHelp(*args) -> None:
    with open('../rsc/player-stat.txt', 'r') as statHelp:
        for l in statHelp.readlines():
            print(l)

def creationHelp(*args) -> None:
    statHelp()
    print('\nEnter \'q\' to quit')

def error(msg:str ="Error!!!") -> None:
    logged = logError(msg)
    if logged:
        raise Exception(msg)
    else:
        exit(1)

def logError(msg:str) -> bool:
    t = str(datetime.date.today())
    p = 'rsc/logs/'+t+'.txt'
    try:
        f = open(p, 'a')
        f.write(msg+"\n")
        f.close()
        return True
    except:
        return False