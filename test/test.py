
def listToDict(list:list):
    counts:dict = {}
    for i in list:
        counts[i] = counts.get(i, 0) + 1
    return counts

myList: list[int] = [1, 2, 3, 4, 1, 2]

print(listToDict(myList))