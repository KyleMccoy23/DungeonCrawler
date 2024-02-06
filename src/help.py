import time

def statHelp():
    with open('assets\player-stat.txt', 'r') as statHelp:
        for l in statHelp.readlines():
            print(l)

def creationHelp():
    statHelp()
    print('\nEnter \'q\' to quit')

def error(msg="Error!!!"):
    logError(msg)
    raise Exception(msg)

def logError(msg):
    t = time.ctime().replace(" ", "").replace(':',"-")
    p = 'E:/Code/DungeonCrawler/rsc/logs/'+t+'.txt'
    try:
        f = open(p, 'w')
        f.write(msg)
        f.close()
    
    except:
        f = open(p, 'x+')
        f.write(msg)
        f.close()