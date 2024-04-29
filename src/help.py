import datetime
from os import system
mainPath = "rsc/playerData/"


def statHelp(*args) -> None:
    with open('rsc/player-stat.txt', 'r') as statHelp:
        for l in statHelp.readlines():
            print(l)

def help() -> None:
    while True:
        print('''\t\tDungeon Crawlers Help Menu

'#' means needs case sensitive input
'>' input is optional
              
Enter 'q' or 'quit' to exit
''')
        h = input("> ").lower()

        match h:
            case 'q' | 'quit':
                system('cls')
                break

        system('cls')

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