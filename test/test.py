
def listToDict(list:list):
    counts:dict[object,int] = {}
    for i in list:
        counts[i] = counts.get(i, 0) + 1
    return counts

myList: list[int] = [1, 2, 3, 4, 1, 2]
alphaList: list[str] = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'c', 'e'] 

print(listToDict(myList))
print(listToDict(alphaList))