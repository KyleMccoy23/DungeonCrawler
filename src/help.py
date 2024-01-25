
def statHelp():
    with open('assets\player-stat.txt', 'r') as statHelp:
        for l in statHelp.readlines():
            print(l)

def creationHelp():
    statHelp()
    print('\nEnter \'q\' to quit')